# Source Index

Where this skill's claims come from and how far each one can be trusted. Unlike the architecture skills, almost nothing here is engine documentation: this is an **operations** skill, and its backbone is a single real deployment. That makes provenance more important, not less — a number that was true of one host on one date is not a fact about TGS.

This skill runs on whatever machine installs it. Never assume a local path layout, and never present a version pin below as current without re-reading the repo's own `dependencies.sh`.

## Grades used in this skill

| Tag | Meaning |
|---|---|
| `[field]` | Observed directly during the deployment below: the symptom was seen, the fix was applied, the result was checked |
| `[source]` | Read out of a repository, a container image, or vendor documentation, and cited by path — but not re-verified since |
| `[reasoned]` | An explanation built on top of a `[field]` observation; the observation is solid, the mechanism is the best available account of it |
| `[unverified]` | Stated in this skill without any of the above; treat as a lead, not a fact |

## The primary deployment

One deployment supplies most of this skill: a Vibelin (Vanderlin-family) fork, on a fresh Ubuntu 26.04 host, using the `tgstation/server:latest` container, on **2026-07-19**. Everything tagged `[field]` below was seen on that host.

What that means for trust: the *failure modes* generalize well (they are properties of the container image, the BYOND webview, and TGS's directory contract), while the *version numbers* do not generalize at all — they were true of one repo on one day.

## Claim ledger

| Claim | Grade | Notes |
|---|---|---|
| Prebuilt rust-g releases need glibc 2.38/2.39; the `tgstation/server` container is Debian bookworm with 2.36 | `[field]` | The mismatch was reproduced, and the `ldd` check in build-and-rustg.md is the test that exposed it. The specific glibc versions are properties of the release binaries and the image **at that time** — re-run `ldd` rather than trusting the numbers |
| A non-loading `librust_g.so` presents as `log_write` runtimes plus a flood of 404s on the bare CDN root | `[field]` | The single most useful fingerprint in this skill: the visible symptom is in nginx, the cause is in the FFI |
| Building rust-g from source inside the container removes the incompatibility | `[field]` | Including the `PKG_CONFIG_ALLOW_CROSS=1` and `--ignore-rust-version` flags, both of which were required |
| The release-profile link step is OOM-killed under ~4 GB RAM; swap/zram plus `CARGO_BUILD_JOBS=1` fixes it | `[field]` | Measured on the low-RAM box, not modelled |
| Disk: repo + two deployments + BYOND + caches reach ~15 GB; a 19 GB disk ran out | `[field]` | One data point. The 25 GB recommendation is that data point plus headroom, not a measured minimum |
| BYOND 516 renders tgui in a webview on origin `http://127.0.0.1:<random port>`, making every CDN asset request cross-origin | `[reasoned]` | The blank-window symptom and the CORS fix are `[field]`; the origin mechanism is the account that explains them |
| Without CORS headers the browser downloads assets and discards them, and tgui retries forever | `[field]` | Observed as "traffic looks healthy, nothing renders" |
| `systemctl reload nginx` did not apply changed `add_header` directives; `restart` did | `[field]` | Seen on that host. Reported as what happened, not as documented nginx behaviour |
| `.tgs.yml` claimed BYOND 515.1639 while 516.1661 was actually required; `dependencies.sh` is the source of truth | `[field]` | Version numbers are Vibelin-on-that-date. The *rule* — prefer `dependencies.sh` — is the transferable part |
| rust-g 6.1.0, and Bun pinned by `BUN_VERSION` | `[source]` | Read from that repo's `dependencies.sh`. Always re-read it; never carry these forward |
| Asset config keys are validated in `code/modules/asset_cache/asset_configs.dm` and `transport/webroot.dm`, falling back to the BYOND transport on a bad config | `[source]` | Cited by path from the fork's own tree; **not re-verified since, and not checked against tgstation master.** Grep before relying on the fallback behaviour |
| `Game/Live/` is replaced every deploy; `Configuration/GameStaticFiles/` is linked into each new deploy | `[field]` | The config-vanishes trap was hit directly |
| TGS default credentials `Admin` / `ISolemlySwearToDeleteTheDataDirectory` | `[source]` | tgstation-server's documented default. Public knowledge, which is exactly why the skill insists on changing it |
| Docker cannot add published ports to a running container | `[source]` | Standard Docker behaviour; the practical consequence (publish the port range up front) is `[field]` |
| The tgui/Bun build needs another ~0.5–1 GB on a first build, then benefits from `TG_BOOTSTRAP_CACHE` | `[field]` | Approximate, from watching the first build; no instrumented measurement |

## Bundled assets

`assets/PreCompile.sh`, `assets/InstallDeps.sh` and `assets/WatchdogLaunch.sh` are **adapted** from the fork's own `tools/tgs_scripts/*.sh`, modified during the deployment above — chiefly so `PreCompile.sh` fetches the prebuilt rust-g, tests it with `ldd`, and falls back to a locally built copy. `assets/nginx-assets.conf` was written for that deployment and carries the CORS block the skill treats as mandatory. All four are `[field]`: they ran on a real host. None have been re-run since **2026-07-19**, and the nginx config still carries a concrete instance name in its `root` — adjust it before use.

## What is not verified here

- **No claim in this file was re-checked while writing it.** It records the provenance the skill's body already asserted, at the grade that body supports. Anything a decision hangs on should be re-tested on the host at hand.
- Nothing here is checked against tgstation master or the official BYOND Reference. Where this skill touches engine or code semantics rather than hosting, `byond-ss13-coding` (engine invariants) and `ss13-tgui` (asset delivery on the interface side) are the authorities — this skill is not.
- Behaviour on any container image other than `tgstation/server:latest` as it stood on 2026-07-19, on any host OS other than Ubuntu 26.04, and on any fork other than the Vibelin/Vanderlin family is `[unverified]` by default.

## Keeping this file honest

When a claim here is re-tested on a new deployment, add the date and the outcome rather than editing the original line away — a claim that held twice, on different hosts, is worth more than a claim that was silently rewritten. When a version pin is found stale, delete the number and keep the rule.
