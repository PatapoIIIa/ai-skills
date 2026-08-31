# Пайплайн деплоя: EventScripts, rust-g (glibc!), tgui

## EventScripts

TGS перед/после компиляции запускает скрипты из
`Configuration/EventScripts/`. За основу берутся `tools/tgs_scripts/*.sh` из
репозитория, но их надо адаптировать (в assets/ этого скилла лежат рабочие
версии с Vibelin):

- `InstallDeps.sh` — apt-зависимости (i386-библиотеки для 32-битного BYOND,
  libssl:i386, zlib:i386, git, curl) + rustup. Вызывается из двух других.
- `PreCompile.sh` — главный: подхватывает `dependencies.sh` из репо
  (версии BYOND/rust-g/Bun), ставит Bun, добывает `librust_g.so`,
  собирает tgui.
- `WatchdogLaunch.sh` — просто перепроверяет зависимости при каждом
  старте сервера.

Не забудь `chmod +x` на все три.

## rust-g и ловушка glibc — читай перед первым деплоем

SS13 грузит `librust_g.so` (32-битную!) в рантайме через BYOND FFI. Есть два
способа её получить, и у обоих есть подводные камни:

### Вариант А: prebuilt с GitHub releases

`https://github.com/tgstation/rust-g/releases/download/<версия>/librust_g.so`
(версия — `RUST_G_VERSION` из `dependencies.sh`, у Vibelin — 6.1.0).

**Ловушка:** релизные бинарники собираются на свежей Ubuntu и требуют
glibc 2.38/2.39. Контейнер `tgstation/server` — Debian bookworm с glibc
**2.36**. Библиотека молча не грузится, и симптомы выглядят совсем не как
"файл не подходит":

- runtime'ы `log_write` и прочих rust-g-процов при старте мира;
- `SSassets` не регистрирует ассеты → у клиентов URL ассетов генерируются
  пустыми → тонны запросов на **голый корень** asset-CDN (`GET /` → 404
  в access-логе nginx), tgui частично сломан.

**Проверка совместимости** (внутри контейнера, `libc6-i386` уже стоит после
InstallDeps.sh):

```bash
docker exec tgs ldd /tgs_instances/<Имя>/Game/Live/librust_g.so
# если в выводе есть "GLIBC_2.3X not found" — бинарник не подходит
```

### Вариант Б: сборка из исходников в контейнере (надёжный)

Собирает под glibc контейнера — несовместимости нет по построению.
На машине с 4+ ГБ RAM это просто и занимает ~5-10 минут:

```bash
docker exec tgs bash -c '
  set -ex
  # тулчейн (rustup уже стоит после InstallDeps.sh, добавляем 32-бит таргет)
  ~/.cargo/bin/rustup target add i686-unknown-linux-gnu
  apt-get install -y gcc-multilib libc6-dev-i386
  # исходники той же версии, что в dependencies.sh
  cd /tgs_instances/<Имя>/Configuration/EventScripts
  git clone --depth 1 --branch 6.1.0 https://github.com/tgstation/rust-g
  cd rust-g
  env PKG_CONFIG_ALLOW_CROSS=1 ~/.cargo/bin/cargo build \
    --release --target=i686-unknown-linux-gnu --ignore-rust-version
'
```

Готовый файл: `target/i686-unknown-linux-gnu/release/librust_g.so`.

- `PKG_CONFIG_ALLOW_CROSS=1` — иначе pkg-config откажется искать
  i386-библиотеки (openssl) при кросс-сборке.
- `--ignore-rust-version` — rust в контейнере может быть чуть старше/младше
  `rust-version` крейта; для rust-g это безопасно.
- **На машине с <4 ГБ RAM** линковку release-профиля убивает OOM-killer:
  добавь swap/zram (см. SKILL.md) и `CARGO_BUILD_JOBS=1`.

Собранную `librust_g.so` положи в `Configuration/EventScripts/` и пусть
`PreCompile.sh` копирует её в билд вместо скачивания — приложенный
`assets/PreCompile.sh` именно так и устроен: качает prebuilt, проверяет его
через `ldd`, при несовместимости берёт локально собранную копию.

## tgui (Bun)

Vibelin собирает tgui через Bun (версия — `BUN_VERSION` из
`dependencies.sh`). `PreCompile.sh` ставит Bun официальным инсталлером и
вызывает `tools/bootstrap/javascript.sh tools/build/build.ts` с
`CBT_BUILD_MODE="TGS"`. Здесь граблей не встречено — просто нужен RAM
(еще ~0.5-1 ГБ на первом билде, дальше кэш `TG_BOOTSTRAP_CACHE` помогает).

## Проверка успешного деплоя

1. В логе деплоя нет ошибок rust-g/tgui.
2. После старта мира в консоли DreamDaemon нет runtime'ов `log_write`.
3. `ls /srv/tgs/instances/<Имя>/webroot_assets/` — появились файлы
   `asset.<hash>.<ext>` (значит SSassets жив и webroot-транспорт пишет).
4. В access-логе nginx — 200-е на `/asset.*`, и **нет** потока 404 на `/`.
