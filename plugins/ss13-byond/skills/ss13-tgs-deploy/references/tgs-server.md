# TGS in Docker: container, instance, persistence

## Installing Docker

Nothing special: `curl -fsSL https://get.docker.com | sh` (installs Engine plus the compose plugin).

## The tgstation-server container

A working configuration (equivalent to what runs on the original VPS):

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

Why it looks like this:

- `5000` is the HTTP API and web panel (`/app/`); `1337` is the DreamDaemon game port. Every additional instance means another game port, and docker cannot add ports to a running container — so if several instances are planned, publish the range up front (`-p 1337-1340:1337-1340`).
- The host binds mean all state (TGS config, instances, logs) lives in `/srv/tgs` and survives recreating the container. They are also what gives nginx direct access to the webroot assets (see nginx-assets.md).
- The instance path inside the container (`/tgs_instances/...`) and on the host (`/srv/tgs/instances/...`) are the same directory under two names. Keep that straight: the game's config.txt takes the **container** path, nginx takes the **host** path.

## First login and security

Panel: `http://<ip>:5000/app/`. The TGS default login is `Admin` / `ISolemlySwearToDeleteTheDataDirectory`.

**Change the password immediately** (Administration → Users): port 5000 is usually exposed to the internet and the default password is public knowledge.

## Creating the instance

Through the panel (the REST API on the same port also works, but the panel is simpler):

1. Instances → Create. Give it a name and the path `/tgs_instances/<Name>` (which must sit under `ValidInstancePaths`). Once created, bring the instance Online.
2. **Configuration Mode → Host Write** — this one matters. It is what allows the instance's `Configuration/` to be edited directly from the host through the binds, rather than only through the panel.
3. Repository → clone the fork you are deploying. Identify it by repository name (for example the Vibelin fork of Vanderlin) and paste the clone URL the fork's owner publishes; this skill does not hardcode anyone's account URL.
4. Engine → pick the BYOND version from the repo's `dependencies.sh` → Install. TGS downloads and unpacks BYOND itself.
5. Deployment: TGS finds the `.dme` on its own as long as there is exactly one at the repo root.

## Persistence: what lives where

Instance layout (`/srv/tgs/instances/<Name>/` on the host):

| Directory | What it is | Survives a deploy? |
|---|---|---|
| `Game/Live/` | The currently running build | **No** — replaced on every deploy |
| `Repository/` | The git clone | Yes |
| `Configuration/GameStaticFiles/` | Overlay applied on top of the game build: `config/`, `data/` | **Yes** — linked into every new deploy |
| `Configuration/EventScripts/` | Deploy hooks (PreCompile.sh and friends) | Yes |

The practical consequence: **edit the game config only in `Configuration/GameStaticFiles/config/`.** Seed it once with a copy of the repo's `config/`, then adjust it for this server (config.txt: `HUB`, `SERVERNAME`, asset CDN keys, `GITHUBURL`, and so on). Anything edited in `Game/Live/config` disappears silently at the next deploy — a trap caught in practice, not in theory.

## Diagnostics

- TGS logs: `/srv/tgs/logs/` on the host.
- Deploy logs and the DreamDaemon console: in the panel, on the instance's Deployment and DreamDaemon tabs.
- Quick port check: `nc -zv <ip> 1337`.
