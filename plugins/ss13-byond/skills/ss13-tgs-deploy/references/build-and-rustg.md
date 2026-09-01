# The deploy pipeline: EventScripts, rust-g (glibc!), tgui

## EventScripts

Before and after compilation TGS runs the scripts in `Configuration/EventScripts/`. Start from the repo's own `tools/tgs_scripts/*.sh`, but expect to adapt them — this skill's `assets/` holds versions that actually worked on a Vibelin deployment:

- `InstallDeps.sh` — apt dependencies (i386 libraries for the 32-bit BYOND, libssl:i386, zlib:i386, git, curl) plus rustup. Called by the other two.
- `PreCompile.sh` — the main one: reads `dependencies.sh` from the repo (BYOND/rust-g/Bun versions), installs Bun, obtains `librust_g.so`, and builds tgui.
- `WatchdogLaunch.sh` — simply re-checks dependencies on every server start.

Remember `chmod +x` on all three.

## rust-g and the glibc trap — read before the first deploy

SS13 loads `librust_g.so` (the 32-bit build!) at runtime through the BYOND FFI. There are two ways to get it, and both have sharp edges.

### Option A: prebuilt from GitHub releases

`https://github.com/tgstation/rust-g/releases/download/<version>/librust_g.so` — the version being `RUST_G_VERSION` from `dependencies.sh` (6.1.0 on Vibelin).

**The trap:** release binaries are built on a recent Ubuntu and require glibc 2.38/2.39. The `tgstation/server` container is Debian bookworm with glibc **2.36**. The library then silently fails to load, and the symptoms look nothing like "wrong binary":

- `log_write` runtimes, and runtimes from other rust-g procs, as the world starts;
- `SSassets` never registers its assets → clients generate empty asset URLs → floods of requests against the **bare root** of the asset CDN (`GET /` → 404 in the nginx access log), with tgui partly broken.

**Compatibility check** (inside the container; `libc6-i386` is already present once InstallDeps.sh has run):

```bash
docker exec tgs ldd /tgs_instances/<Name>/Game/Live/librust_g.so
# "GLIBC_2.3X not found" anywhere in the output means this binary will not work
```

### Option B: build from source inside the container (the reliable one)

Building against the container's own glibc removes the incompatibility by construction. On a machine with 4+ GB RAM it is straightforward and takes about 5–10 minutes:

```bash
docker exec tgs bash -c '
  set -ex
  # toolchain (rustup is already installed by InstallDeps.sh; add the 32-bit target)
  ~/.cargo/bin/rustup target add i686-unknown-linux-gnu
  apt-get install -y gcc-multilib libc6-dev-i386
  # sources at exactly the version pinned in dependencies.sh
  cd /tgs_instances/<Name>/Configuration/EventScripts
  git clone --depth 1 --branch 6.1.0 https://github.com/tgstation/rust-g
  cd rust-g
  env PKG_CONFIG_ALLOW_CROSS=1 ~/.cargo/bin/cargo build \
    --release --target=i686-unknown-linux-gnu --ignore-rust-version
'
```

The result lands at `target/i686-unknown-linux-gnu/release/librust_g.so`.

- `PKG_CONFIG_ALLOW_CROSS=1` — without it pkg-config refuses to look for i386 libraries (openssl) during a cross build.
- `--ignore-rust-version` — the container's rust may be slightly older or newer than the crate's `rust-version`; for rust-g this is safe.
- **On a machine with under 4 GB RAM** the OOM killer takes down the release-profile link step: add swap/zram (see SKILL.md) and `CARGO_BUILD_JOBS=1`.

Put the built `librust_g.so` in `Configuration/EventScripts/` and have `PreCompile.sh` copy it into the build instead of downloading. The bundled `assets/PreCompile.sh` is built exactly that way: it fetches the prebuilt, checks it with `ldd`, and falls back to the locally built copy when the check fails.

## tgui (Bun)

Vibelin builds tgui through Bun (version from `BUN_VERSION` in `dependencies.sh`). `PreCompile.sh` installs Bun with the official installer and calls `tools/bootstrap/javascript.sh tools/build/build.ts` with `CBT_BUILD_MODE="TGS"`. No traps were hit here — it just needs RAM (another ~0.5–1 GB on the first build; after that the `TG_BOOTSTRAP_CACHE` helps).

## Confirming a deploy actually succeeded

Check all four; any one of them alone is not enough to call a deploy green.

1. The deploy log carries no rust-g or tgui errors.
2. After the world starts, the DreamDaemon console shows no `log_write` runtimes.
3. `ls /srv/tgs/instances/<Name>/webroot_assets/` lists `asset.<hash>.<ext>` files — meaning SSassets is alive and the webroot transport is writing.
4. The nginx access log shows 200s on `/asset.*` and **no** stream of 404s on `/`.
