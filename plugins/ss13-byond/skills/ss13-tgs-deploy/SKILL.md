---
name: ss13-tgs-deploy
description: >-
  Deploy an SS13 game server (Vibelin / Vanderlin / any tgstation fork) from
  scratch on a fresh Linux host using tgstation-server (TGS) in Docker: TGS
  container setup, instance creation, EventScripts, the rust-g glibc trap,
  tgui/Bun build, nginx asset CDN with mandatory CORS, and config persistence.
  Use this whenever the user wants to deploy, move, migrate, rebuild, or
  troubleshoot an SS13/BYOND server or a TGS instance — trigger words include
  TGS, tgstation-server, DreamDaemon, Vibelin, "поднять сервер SS13",
  "развернуть инстанс", "перенести сервер", asset CDN / tgui asset problems,
  or librust_g.so errors — even if they only say "поднять сервак на новой
  машине".
---

# Развёртывание SS13-сервера (Vibelin) через TGS в Docker

Проверенный на практике порядок развёртывания форка tgstation (Vibelin,
https://github.com/trueroguan/Vibelin — Vanderlin-based) на чистом Linux-хосте.
Скилл написан по итогам реального развёртывания 2026-07-19 на Ubuntu 26.04;
все грабли ниже — реально пойманные, не теоретические.

## Требования к железу

- **RAM: 4+ ГБ желательно.** Первый деплой собирает rust-g (cargo) и tgui
  (Bun) — пик ~1.5 ГБ внутри контейнера, а линковка rust-g на release-профиле
  может съесть больше. На боксе с 2–3 ГБ обязательно добавь swap **до** первого
  деплоя (2 ГБ файл + zram), иначе OOM-killer убьёт cargo на линковке:
  ```bash
  fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
  echo '/swapfile none swap sw 0 0' >> /etc/fstab
  # быстрый компрессированный swap в RAM (опционально, но сильно помогает):
  modprobe zram num_devices=1 && echo 3G > /sys/block/zram0/disksize \
    && mkswap /dev/zram0 && swapon -p 100 /dev/zram0
  ```
  На слабой машине также собирай cargo однопоточно: `CARGO_BUILD_JOBS=1`.
- **Диск: 25+ ГБ.** Репо + два деплоя (Live и staged) + BYOND + кэши сборки
  легко занимают 15 ГБ. На 19 ГБ диске место кончалось; не храни лишний клон
  репо рядом.

## Порядок работ (чеклист)

Подробности каждого шага — в references/, читай их по мере выполнения.

1. **Docker + контейнер TGS** → [references/tgs-server.md](references/tgs-server.md)
2. **Первый вход в панель, смена пароля Admin** (порт 5000 смотрит в интернет!)
3. **Создание инстанса** (path `/tgs_instances/<Имя>`), режим конфигурации
   **Host Write** → там же
4. **EventScripts** — положить скрипты из [assets/](assets/) в
   `Configuration/EventScripts/`, `chmod +x` → [references/build-and-rustg.md](references/build-and-rustg.md)
5. **Клон репозитория** через вкладку Repository инстанса
6. **Версия BYOND**: смотри `dependencies.sh` в корне репо, **не** `.tgs.yml`
   (он бывает протухшим: у Vibelin `.tgs.yml` говорил 515.1639, реально нужен
   516.1661). Ставится через вкладку Engine.
7. **Игровой конфиг** — скопировать `config/` репо в
   `Configuration/GameStaticFiles/config/`, править только там
   → [references/tgs-server.md](references/tgs-server.md), раздел про персистентность
8. **Первый деплой** (долгий: BYOND + rust-g + tgui). Следи за логами
   в панели. Главная ловушка этого шага — **glibc у prebuilt rust-g**
   → [references/build-and-rustg.md](references/build-and-rustg.md)
9. **nginx asset CDN + CORS** → [references/nginx-assets.md](references/nginx-assets.md)
10. **DreamDaemon**: порт 1337, автостарт, запуск watchdog. Проверка:
    `byond://<ip>:1337`, регистрация на хабе — `HUB` в config.txt.

## Главные грабли (краткая карта)

| Симптом | Причина | Где решение |
|---|---|---|
| cargo убит (SIGKILL) на линковке | OOM, мало RAM | swap/zram + `CARGO_BUILD_JOBS=1`, выше |
| Runtime'ы `log_write`, тонны 404 на голый корень CDN-URL в логах nginx | `librust_g.so` не грузится: prebuilt собран под glibc 2.38/2.39, в контейнере Debian bookworm = 2.36 | build-and-rustg.md |
| tgui-окна пустые, ассеты качаются но выбрасываются, бесконечный цикл запросов | Нет CORS-заголовков на asset CDN (webview BYOND 516 живёт на origin `http://127.0.0.1:<random>`) | nginx-assets.md |
| Поменял nginx-конфиг, а заголовки не изменились | `systemctl reload nginx` не применил `add_header`; нужен `restart` | nginx-assets.md |
| Правки конфига пропали после деплоя | Правили `Game/Live/config` — он пересоздаётся каждый деплой | tgs-server.md |
| TGS ставит не ту версию BYOND | `.tgs.yml` протух | `dependencies.sh` — источник истины |

## Структура скилла

- `references/tgs-server.md` — Docker, контейнер TGS, инстанс, персистентность конфига
- `references/build-and-rustg.md` — пайплайн деплоя, rust-g/glibc, tgui/Bun
- `references/nginx-assets.md` — asset CDN через webroot + nginx + CORS
- `assets/PreCompile.sh`, `assets/InstallDeps.sh`, `assets/WatchdogLaunch.sh` — рабочие EventScripts
- `assets/nginx-assets.conf` — рабочий конфиг nginx
