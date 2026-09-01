---
name: "ss13-tgs-deploy"
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

# SS13 Server Deployment via TGS in Docker

Field-tested order of operations for standing a tgstation-derived fork (Vibelin, Vanderlin, any /tg/-family codebase) up on a clean Linux host with tgstation-server. Written from a real deployment on Ubuntu 26.04 (2026-07-19); every trap below was actually hit, not theorized.

## Activation guard

This is the **operations** skill: it owns the host a build runs on, never the code inside the build. Use it for TGS/tgstation-server, DreamDaemon, Docker, hosting, deploying/migrating/rebuilding an instance, asset-CDN or nginx delivery, and build-toolchain failures (`librust_g.so`, cargo, Bun).

Two edges it does not cross:

- A **DM compile error, runtime, or code-level defect** surfaced by a deploy belongs to `byond-ss13-coding`. This skill's job ends at "the build failed, here is the compiler output" — it does not start editing `.dm` files to make a deploy go green.
- An **interface that renders wrong once assets are demonstrably being served** belongs to `ss13-tgui`. This skill owns asset *delivery* (transport mode, webroot, CORS, nginx); it does not own what tgui does with an asset it successfully received.

This skill binds to no semantic base — `ai_navigation/` folders describe code, not hosts. Routing between skills is `byond-codemaster-controller`'s single source of truth (its Gate 1, node 0, lands here); do not re-derive it.

## Execution limits

Every command below runs against a live host: it writes `/etc/fstab`, creates swap, installs packages, restarts nginx, and rebuilds game deployments. **Propose the commands; do not run them on your own initiative.** Run one only when the user has explicitly asked for it in this session, and only against the host they named.

Two are destructive enough to confirm individually even under broad permission: appending to `/etc/fstab` (a malformed line can block the next boot) and `rm -f /etc/nginx/sites-enabled/default` (removes a config this skill did not write and cannot restore).

Report honestly. A deploy is green only if its log was actually read in this session — "the container started", "the compile finished", and "the world booted with no rust-g runtimes" are three separate claims, and merging them is how a broken `librust_g.so` reaches players.

## Hardware requirements

- **RAM: 4+ GB preferred.** The first deploy builds rust-g (cargo) and tgui (Bun) — peak ~1.5 GB inside the container, and linking rust-g on the release profile can exceed that. On a 2–3 GB box, add swap **before** the first deploy (a 2 GB file plus zram) or the OOM killer will take cargo down during linking:
  ```bash
  fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
  echo '/swapfile none swap sw 0 0' >> /etc/fstab
  # fast compressed swap in RAM (optional, but helps a lot):
  modprobe zram num_devices=1 && echo 3G > /sys/block/zram0/disksize \
    && mkswap /dev/zram0 && swapon -p 100 /dev/zram0
  ```
  On a weak machine also build cargo single-threaded: `CARGO_BUILD_JOBS=1`.
- **Disk: 25+ GB.** The repo plus two deployments (Live and staged) plus BYOND plus build caches easily reach 15 GB. A 19 GB disk ran out of space; don't keep a spare clone of the repo alongside.

## Order of work (checklist)

Per-step detail lives in `references/`; open each as you reach it.

1. **Docker + the TGS container** → [references/tgs-server.md](references/tgs-server.md)
2. **First panel login, change the Admin password** (port 5000 faces the internet!)
3. **Create the instance** (path `/tgs_instances/<Name>`), configuration mode **Host Write** → same file
4. **EventScripts** — drop the scripts from [assets/](assets/) into `Configuration/EventScripts/`, `chmod +x` → [references/build-and-rustg.md](references/build-and-rustg.md)
5. **Clone the repository** through the instance's Repository tab
6. **BYOND version**: read `dependencies.sh` at the repo root, **not** `.tgs.yml` — that one goes stale (on Vibelin it claimed 515.1639 while 516.1661 was actually required). Installed through the Engine tab.
7. **Game config** — copy the repo's `config/` into `Configuration/GameStaticFiles/config/` and edit only there → [references/tgs-server.md](references/tgs-server.md), the persistence section
8. **First deploy** (long: BYOND + rust-g + tgui). Watch the panel logs. The trap of this step is **glibc versus prebuilt rust-g** → [references/build-and-rustg.md](references/build-and-rustg.md)
9. **nginx asset CDN + CORS** → [references/nginx-assets.md](references/nginx-assets.md)
10. **DreamDaemon**: port 1337, autostart, launch the watchdog. Verify with `byond://<ip>:1337`; hub registration is `HUB` in config.txt.

## Trap map

| Symptom | Cause | Where it is solved |
|---|---|---|
| cargo killed (SIGKILL) while linking | OOM, not enough RAM | swap/zram + `CARGO_BUILD_JOBS=1`, above |
| `log_write` runtimes, floods of 404s on the bare CDN root in the nginx log | `librust_g.so` does not load: the prebuilt binary targets glibc 2.38/2.39, the Debian bookworm container has 2.36 | build-and-rustg.md |
| tgui windows blank, assets download but are discarded, endless request loop | No CORS headers on the asset CDN (the BYOND 516 webview lives on origin `http://127.0.0.1:<random>`) | nginx-assets.md |
| Changed the nginx config, headers did not change | `systemctl reload nginx` did not apply `add_header`; a `restart` is required | nginx-assets.md |
| Config edits vanished after a deploy | They were made in `Game/Live/config`, which is recreated on every deploy | tgs-server.md |
| TGS installs the wrong BYOND version | `.tgs.yml` is stale | `dependencies.sh` is the source of truth |

## Example requests

- EN: "Stand our SS13 fork up on a fresh Ubuntu box with TGS in Docker — walk me through it from zero."
- RU: «Подними наш форк SS13 на чистой Ubuntu через TGS в Docker — проведи с нуля».
- EN: "tgui windows are blank on the new server and nginx is logging a flood of 404s on `/`. Where do I start?"
- RU: «На новом сервере tgui-окна пустые, а nginx сыплет 404 на `/`. С чего начинать?»
- EN: "Migrate the running instance to a new host without losing the game config."
- RU: «Перенеси работающий инстанс на новую машину, не потеряв игровой конфиг».

## Reference files (progressive disclosure)

- `references/tgs-server.md` — Docker, the TGS container, instance creation, and which directories survive a deploy. **Read for steps 1–3 and 5–7, and whenever config edits disappear or a migration has to preserve state.**
- `references/build-and-rustg.md` — the deploy pipeline: EventScripts, rust-g versus the container's glibc (with the build-from-source fallback), and the tgui/Bun build. **Read before the first deploy, and whenever the world boots with `log_write` runtimes or a build step fails.**
- `references/nginx-assets.md` — asset CDN over the webroot transport: game config keys, the nginx site, and the mandatory CORS headers. **Read for step 9, and whenever assets are requested but never applied.**
- `references/source-index.md` — where each claim comes from, what was field-verified and when, and what is still unverified. **Read before presenting any number or version in this skill as fact.**
- `assets/PreCompile.sh`, `assets/InstallDeps.sh`, `assets/WatchdogLaunch.sh` — working EventScripts.
- `assets/nginx-assets.conf` — a working nginx config.
