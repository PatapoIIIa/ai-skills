# Embedded Map Geometry and Field-Debugging Discipline

Read this when a `ByondUi` map control renders content tiny, off-center, clipped, or invisible; when sizing/zooming an embedded map_view preview; or when field reports about map behavior contradict each other. Everything here was measured on ONE build — **BYOND 516.1661, Vanderlin tgui-core fork, ~25 build-test rounds**; constants marked "this build" are that build's values, not engine guarantees. The *instruments*, the *pinning recipe*, and the *failure modes* are what generalize — re-measure the numbers anywhere else.

## The geometry contract (measured, then falsified, then pinned)

**A dynamically-created secondary map control (ByondUi `type: 'map'`) chooses its world canvas by rules you do not control — so pin the canvas yourself.** Field data from the same build shows TWO canvas modes with no reliable trigger:

- **Skin-default mode**: canvas = 640×480 world px on this build (20×15 tiles; matches the skin's default element size) regardless of registered screen objects — objects at tile (1,1) still render into the big canvas, and a `fill_rect` background could not shrink it across many rounds.
- **Object-bbox mode**: the SAME code on the same build later produced a canvas equal to the registered objects' tile bounding box (1 tile), silently, after an unrelated layout change (the container went from square to portrait — correlation, not a proven mechanism). Content positioned in 640×480 coordinates landed outside the 1-tile world: the control rendered pure black.

For one round, "the canvas is a fixed 640×480" looked like a measured constant. It was a *configuration-dependent function* — see false conclusion #7 below.

**The robust contract: make both modes identical by pinning the bbox.** Register an invisible `/atom/movable/screen/background` with `fill_rect(1, 1, frame_w, frame_h)` spanning your ENTIRE intended frame (e.g. 20×15 tiles). Then object-bbox mode computes exactly your frame, default mode already is it (when they differ, the larger wins — bbox only ever grew past the default in field tests), and your coordinates are valid in both. Never leave the frame implicit.

**Sizing: the `zoom` skin param disables auto-fit entirely.** At `zoom: N` each icon px renders at N screen px, and the viewport shows the CENTER of the canvas. The working recipe for a preview that fills its box:

1. Pin the canvas with the background frame (above).
2. Frontend measures its container (`getBoundingClientRect()` × `devicePixelRatio` — BYOND works in physical px) and computes `zoom = floor(min(boxW * wFill / contentW, boxH * hFill / contentH))` from the content's real pixel size.
3. Pass `zoom` and `'zoom-mode': 'distort'` (crisp integer scaling) in the ByondUi creation params.
4. Place the content at the frame center via `set_position(1, 1, frame_cx - w/2, frame_cy - h/2)` (e.g. 320,240 for a 20×15 frame). Large pixel offsets in `screen_loc` are valid.
5. Never use the `CENTER`/`SOUTH` keywords with a map-id-prefixed screen_loc — the object silently vanishes. Only `"mapid:tile:px,tile:py"` works.
6. With `zoom=0` (auto-fit, the default) the whole canvas letterboxes into the control: a 1-tile doll in a 20-tile frame renders at ~1/20 of the control width. This is why naive map_view previews are tiny. Code comments claiming fill_rect "allocates the rectangle used for auto-scaling" describe popup *windows* (`setup_popup`) — under auto-fit the background frame cannot make the doll bigger, only the zoom path can.

## The proven end-to-end recipe (field-validated reference build)

The complete shape that survived ~26 rounds of field testing, for a live character-doll preview:

- **DM, per open menu**: one `map_view` per projection (main + fixed-dir minis), each with a unique `assigned_map`; one invisible background per map with `fill_rect(1, 1, frame_w, frame_h)` pinning the canvas (20×15). Doll = `view.appearance = dummy.appearance` + `view.setDir(dir)`; `appearance_flags = KEEP_TOGETHER | PIXEL_SCALE` (no TILE_BOUND); positioned by `set_position(1, 1, frame_cx - art_w/2, frame_cy - art_h/2)`.
- **Measure per render**: flatten the dummy at the CURRENT direction, trim to art bounds (GetPixel bounding box — canvas size and canvas origin both lie for asymmetric overlay sets), store art w/h and origin offset; re-measure on every rotation (art bounds are per-direction: a side view is half the width of a front view).
- **Decouple POSITIONING dims from ZOOM dims or rotation makes the doll pulse.** Positioning uses the current direction's art bounds (re-measured per rotate). Zoom uses stable dims: max of the current and perpendicular directions' art, quantized up (e.g. to 4px), updated only on full renders — so rotating a wide-bodied sprite keeps one scale (the side-view-limited one) instead of zooming in and out per facing, and hover-induced ±1px art changes don't churn the zoom either.
- **Frontend**: ByondUi keyed by map id ONLY; mount params carry initial `zoom` (computed from container rect × devicePixelRatio and the backend-reported art size: `floor(min(w*0.95/artW, h*0.85/artH))` — width factor ≤1 so side views never crop), `'zoom-mode': 'distort'`, initial `background-color`. A measurement effect reports container sizes + computed zooms to the backend through a normal `act()`.
- **DM on each geometry report**: `winset` zoom AND background-color onto all map controls — this is the ONLY update channel for control params after mount (no remounts), and re-running it every report self-heals the component's stale param re-asserts.
- **Interaction costs**: rotate = re-measure + one `apply_to_view` (no dummy rebuild); hover = dummy rebuild with a temporarily swapped customizer entry, main view only; full three-view render only on real state changes. Field profile: ~0.7 tick-units per render including the pixel scan, no per-tick work (autoupdate off).

## Live content: what actually syncs

- `view.appearance = mob.appearance` + `view.setDir(dir)` is the reliable live path (the /tg/ char_preview mechanism). Rotation is a pure `setDir`; no re-render.
- Set `appearance_flags = KEEP_TOGETHER | PIXEL_SCALE` on the view and DROP the mob's `TILE_BOUND` — TILE_BOUND clips overlays extending past the 32px cell once magnified.
- Reassigning a runtime-built `.icon` on the screen object does NOT reliably repaint the embedded control (VV shows the new icon; the control shows stale frames, blanks, or nothing until a full re-display). Do not build flatten-icon pipelines on that path.
- `transform` scaling on these screen objects produced contradictory pivot behavior across builds — avoid it for sizing; the control-side `zoom` supersedes it.

## Measurement instruments (use these before theorizing)

- **`winget(user, map_id, "view-size")` at a fixed zoom measures the canvas**: `canvas_px = view-size / zoom`. This one probe ended weeks of canvas guessing. At zoom=0 view-size only reveals the canvas *aspect* (it equals the letterboxed content area).
- **A frontend geometry report**: send `getBoundingClientRect()` sizes, `devicePixelRatio`, and the computed zoom through `act()` into the server log, next to the DM-side winget dump. Screenshots lie about anchor/scale; two numbers in one log line don't.
- **Content size ≠ canvas size**: a flattened measurement icon reports its overlay *canvas*, which is often asymmetric around the base cell (a 64px-wide canvas with art hugging one edge). For centering and zoom math, scan the real art bounds (`icon.GetPixel` bounding box, ~2k calls is fine per user action) or your "centered" content will sit visibly off-center.
- **Design experiments that measure even when they fail.** The build that made the doll vanish still measured the canvas, because fixed zoom turned view-size into a ruler. Prefer interventions whose failure output is informative, and expose position/size knobs as VV-editable vars so the next round can probe live without recompiling.

## Two-artifact deploys: fingerprint or suffer

A tgui fork ships TWO artifacts — the `.dmb` and the tgui bundle — and they go stale independently. Multiple "engine facts" in this saga were fabricated by testing new DM against an old bundle (or vice versa):

- "winset zoom doesn't stick" — false; the old bundle's ByondUi kept re-winsetting `zoom: 0` from its mount-time params closure on every layout pass.
- "the fix didn't work" rounds that were actually running last week's build entirely.

Discipline:

- **Log a fingerprint from BOTH sides.** The frontend should echo something version-identifying into the backend log (a formula constant, a literal bundle marker in the geometry report). Before believing any "still broken" report, check the fingerprint — a stale value means stop debugging and rebuild.
- **Field observations inherit the credibility of their build.** When recording a conclusion (in notes, memory, handoffs), record which build produced it. A conclusion from a round later proven stale is poisoned — re-verify it before letting it steer design.

## ByondUi param lifecycle (why remounts flash and updates go stale)

`ByondUi` winsets `{parent, ...params, pos, size}` once on mount and re-winsets the SAME mount-time params on window resize (stale closure). Therefore:

- **Never put ANY changeable param (zoom, sizes, background-color) in the React `key`.** A key change unmounts (`winset parent: ''`) and recreates the control — a visible flash. Field-proven twice: zoom-in-key made species switches flash; backdrop-in-key made background switches flash. The key is the map id, nothing else.
- **Dynamic param updates go through DM `winset`** after creation; they stick, but expect the component's resize handler to re-assert its original params — have the DM side re-push ALL dynamic params (zoom, background-color) on its own recurring signal (e.g. after each frontend geometry report), so any stale re-assert self-heals.
- Mount-time params are still worth setting correctly: they apply instantly with zero server round-trip.

## How the false conclusions formed (prevention rules)

1. **Stale-build observation → recorded as engine fact → inherited by later sessions.** Prevention: build fingerprints in logs; provenance on recorded conclusions.
2. **Model stacked on unverified model** (assumed square view → assumed pivot → assumed anchor; each screenshot "confirmed" the current theory). Prevention: one measurement outranks any number of consistent-looking screenshots; get the number first.
3. **A code comment about a different context** (popup windows) transplanted to embedded controls. Prevention: comments state intent; measure the actual target.
4. **Several independent bugs treated as one** (repaint reliability + geometry + remount flicker + sprite gating were four different defects with one shared symptom: "doll looks wrong"). Prevention: when a symptom survives a correct fix, split it — list the independent mechanisms that could each produce it and test them separately.
5. **Handoff links labeled "source of truth" that nobody had opened** (they were unrelated bug reports). Prevention: verify references at write time and annotate what each actually contains; at read time, spend the first five minutes confirming they say what the handoff claims.
6. **"Misaligned/invisible sprite" reports treated as pixel-tuning problems.** In the field they were logic bugs: a gendered state-resolution branch skipping offsets, a validated-preference write silently sanitizing every value back to default (a choices list wired to a stub), an accessory list unfiltered by gender/species. Prevention: trace the resolution chain (which state was picked, which gate returned FALSE, what value actually landed on the mob) before nudging any pixel — and never blind-tune pixel offsets you cannot see rendered.
7. **A constant measured under one configuration recorded as an engine fact.** "The canvas is a fixed 640×480" held across every square-container round, went into notes as a constant — and the first portrait-container round flipped the engine into object-bbox mode, invalidating every coordinate and rendering pure black. The claim was true *for the configurations tested*; nothing had varied the configuration. Prevention: before recording a measured value as a constant, vary the configuration axes you can reach (container shape, creation order, params) or explicitly scope the claim to the tested configuration and build; better, don't RELY on the value at all — pin the invariant you need (the background frame) so the engine's choice stops mattering.
