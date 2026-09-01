# Asset CDN: the webroot transport + nginx + mandatory CORS

## Why

SS13 (`SSassets`) can serve browser assets — css, js, fonts, icons for tgui and browse windows — through an external web server instead of BYOND's built-in transport. It is faster and it keeps the load off DreamDaemon. DreamDaemon simply writes hashed files (`asset.<hash>.<ext>`) into a directory and nginx serves them over HTTP.

## Game config

In `Configuration/GameStaticFiles/config/config.txt`:

```
ASSET_TRANSPORT webroot
ASSET_CDN_WEBROOT /tgs_instances/<Name>/webroot_assets/
ASSET_CDN_URL http://<public-ip-or-domain>/
```

- `ASSET_CDN_WEBROOT` is the path **inside the container** (DreamDaemon writes there via fcopy). On the host the same directory is `/srv/tgs/instances/<Name>/webroot_assets/`, and it is the host path that goes into the nginx `root`.
- Key validation lives in `code/modules/asset_cache/asset_configs.dm` and `transport/webroot.dm`: on a malformed or incomplete config the game silently falls back to the BYOND transport (logging an error rather than crashing), so iterating on these keys is safe.

## nginx

A working config ships as `assets/nginx-assets.conf`. To install it:

```bash
apt-get install -y nginx
cp nginx-assets.conf /etc/nginx/sites-available/ss13-assets
# adjust root and server_name for your instance
ln -s /etc/nginx/sites-available/ss13-assets /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx
```

The `rm -f` line removes a config this skill did not write; confirm it with the user before running it on a host that serves anything else (see the Execution limits section in SKILL.md).

## CORS is mandatory — it is not an option

BYOND 516 renders tgui inside an embedded webview that lives on the origin `http://127.0.0.1:<random port>`. Every asset request to the CDN is therefore cross-origin. Without the right headers the browser **downloads the file and throws it away**, after which tgui enters an endless retry loop — traffic-wise everything "works", in reality nothing loads.

The minimum required (already baked into the bundled config):

- `Access-Control-Allow-Origin: *`, plus the GET, HEAD and OPTIONS methods;
- a `204` response to the `OPTIONS` preflight;
- `Access-Control-Expose-Headers: Content-Length, Content-Range` — the webview uses Range requests for fonts and larger files.

## Traps

1. **`systemctl reload nginx` may not apply `add_header` changes.** On the original server a full `restart` was required. If headers were changed and the responses do not show them, restart first and only then keep digging.
2. **A flood of 404s on the bare root (`GET / HTTP/1.1" 404`) in the access log is not an nginx problem.** It is clients requesting assets with empty names because the assets never registered when the world started. Almost certainly `librust_g.so` is not loading — see build-and-rustg.md.
3. **Check by hand:** take any filename from `webroot_assets/` and run `curl -sI http://<ip>/asset.<hash>.<ext>` — expect a 200 and the `Access-Control-*` headers in the response.
