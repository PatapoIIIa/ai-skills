# TGS в Docker: контейнер, инстанс, персистентность

## Установка Docker

Стандартно: `curl -fsSL https://get.docker.com | sh` (ставит Engine + compose-плагин).

## Контейнер tgstation-server

Рабочая конфигурация (эквивалент того, что крутится на исходном VPS):

```bash
mkdir -p /srv/tgs/{config,instances,logs}

docker run -d --name tgs --restart unless-stopped \
  -p 5000:5000 \
  -p 1337:1337 \
  -v /srv/tgs/config:/config_data \
  -v /srv/tgs/instances:/tgs_instances \
  -v /srv/tgs/logs:/tgs_logs \
  -e General__ValidInstancePaths__0=/tgs_instances \
  -e FileLogging__Directory=/tgs_logs \
  -e Internal__UsingDocker=true \
  tgstation/server:latest
```

Почему так:

- `5000` — HTTP API и веб-панель (`/app/`), `1337` — игровой порт DreamDaemon.
  Каждый дополнительный инстанс = ещё один игровой порт; docker не умеет
  добавлять порты на живом контейнере, так что если планируешь несколько
  инстансов — прокинь диапазон сразу (`-p 1337-1340:1337-1340`).
- Бинды на хост означают: всё состояние (конфиг TGS, инстансы, логи) живёт в
  `/srv/tgs` и переживает пересоздание контейнера. Это же даёт nginx прямой
  доступ к webroot-ассетам (см. nginx-assets.md).
- Путь инстанса внутри контейнера (`/tgs_instances/...`) и на хосте
  (`/srv/tgs/instances/...`) — это одна и та же директория с разными именами.
  Помни об этом: в игровом config.txt пути пишутся **контейнерные**, в
  nginx — **хостовые**.

## Первый вход и безопасность

Панель: `http://<ip>:5000/app/`. Дефолтный логин TGS:
`Admin` / `ISolemlySwearToDeleteTheDataDirectory`.

**Сразу смени пароль** (Administration → Users): порт 5000 обычно открыт
в интернет, дефолтный пароль общеизвестен.

## Создание инстанса

Через панель (можно и через REST API на том же порту, но панель проще):

1. Instances → Create. Имя, путь `/tgs_instances/<Имя>` (путь должен быть под
   `ValidInstancePaths`). После создания инстанс переводится в Online.
2. **Configuration Mode → Host Write** — критично. Это позволяет редактировать
   `Configuration/` инстанса напрямую с хоста (по биндам), а не только через
   панель.
3. Repository → clone нужного форка (для Vibelin:
   `https://github.com/trueroguan/Vibelin`).
4. Engine → выбрать BYOND-версию из `dependencies.sh` репо → Install.
   TGS сам скачает и распакует BYOND.
5. Deployment: `.dme` TGS находит сам, если он один в корне репо.

## Персистентность: что где живёт

Структура инстанса (`/srv/tgs/instances/<Имя>/` на хосте):

| Директория | Что это | Переживает деплой? |
|---|---|---|
| `Game/Live/` | Текущая работающая сборка | **Нет** — заменяется каждый деплой |
| `Repository/` | Git-клон | Да |
| `Configuration/GameStaticFiles/` | Оверлей поверх игровой сборки: `config/`, `data/` | **Да** — линкуется в каждый новый деплой |
| `Configuration/EventScripts/` | Хуки деплоя (PreCompile.sh и т.д.) | Да |

Практическое следствие: **игровой конфиг редактируй только в
`Configuration/GameStaticFiles/config/`**. Первый раз наполни его копией
`config/` из репозитория, затем правь под сервер (config.txt: `HUB`,
`SERVERNAME`, asset CDN-ключи, `GITHUBURL`, и т.д.). Всё, что поправишь в
`Game/Live/config`, молча исчезнет при следующем деплое — эта ловушка
ловилась на практике.

## Диагностика

- Логи TGS: `/srv/tgs/logs/` на хосте.
- Логи деплоя и консоль DreamDaemon — в панели (вкладки Deployment /
  DreamDaemon инстанса).
- Быстрая проверка порта: `nc -zv <ip> 1337`.
