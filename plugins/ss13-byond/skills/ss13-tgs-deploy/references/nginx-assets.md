# Asset CDN: webroot-транспорт + nginx + обязательный CORS

## Зачем

SS13 (`SSassets`) умеет отдавать браузерные ассеты (css/js/шрифты/иконки для
tgui и browse-окон) не через встроенный транспорт BYOND, а через внешний
вебсервер — быстрее и не грузит DreamDaemon. DreamDaemon просто пишет
хэшированные файлы (`asset.<hash>.<ext>`) в директорию, nginx отдаёт их по HTTP.

## Игровой конфиг

В `Configuration/GameStaticFiles/config/config.txt`:

```
ASSET_TRANSPORT webroot
ASSET_CDN_WEBROOT /tgs_instances/<Имя>/webroot_assets/
ASSET_CDN_URL http://<публичный-ip-или-домен>/
```

- `ASSET_CDN_WEBROOT` — путь **внутри контейнера** (DreamDaemon пишет туда
  через fcopy). На хосте эта же директория —
  `/srv/tgs/instances/<Имя>/webroot_assets/`, и именно хостовый путь идёт
  в nginx `root`.
- Валидация ключей — `code/modules/asset_cache/asset_configs.dm` и
  `transport/webroot.dm`: при кривом/неполном конфиге игра молча падает
  обратно на BYOND-транспорт (пишет ошибку в лог, не крашится) — итерироваться
  безопасно.

## nginx

Готовый конфиг — `assets/nginx-assets.conf`. Поставить:

```bash
apt-get install -y nginx
cp nginx-assets.conf /etc/nginx/sites-available/ss13-assets
# поправь root и server_name под свой инстанс
ln -s /etc/nginx/sites-available/ss13-assets /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx
```

## CORS обязателен — это не опция

BYOND 516 рендерит tgui во встроенном webview, который живёт на origin
`http://127.0.0.1:<случайный порт>`. Каждый запрос ассета с CDN —
кросс-доменный. Без правильных заголовков браузер **скачивает файл и
выбрасывает его**, после чего tgui уходит в бесконечный цикл повторных
запросов — по трафику всё "работает", по факту ничего не грузится.

Минимально необходимое (уже вшито в приложенный конфиг):

- `Access-Control-Allow-Origin: *` (+ методы GET, HEAD, OPTIONS);
- ответ `204` на preflight `OPTIONS`;
- `Access-Control-Expose-Headers: Content-Length, Content-Range` — webview
  ходит Range-запросами за шрифтами/крупными файлами.

## Грабли

1. **`systemctl reload nginx` может не применить изменения `add_header`** —
   на исходном сервере пришлось делать полный `restart`. Если поменял
   заголовки и в ответах их нет — сначала `restart`, потом уже копай дальше.
2. Поток 404 на голый корень (`GET / HTTP/1.1" 404`) в access-логе — это
   **не** проблема nginx: это клиенты запрашивают ассеты с пустыми именами,
   потому что ассеты не зарегистрировались на старте мира. Почти наверняка
   не грузится `librust_g.so` → см. build-and-rustg.md.
3. Проверка руками: возьми имя любого файла из
   `webroot_assets/` и дёрни `curl -sI http://<ip>/asset.<hash>.<ext>` —
   должен быть 200 и заголовки `Access-Control-*` в ответе.
