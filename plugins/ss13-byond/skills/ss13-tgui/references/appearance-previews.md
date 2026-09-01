# Appearance previews — field detail

Loaded from SKILL.md → Appearance preview pickers. That section carries the
*decision*: map_view for live scenes, spritesheet assets for static catalogs,
`DmIcon` for single un-composed icons, base64 for dynamic one-offs. This file
carries what goes wrong once you have chosen, which is longer than the decision
and needed far less often.

Read it when a preview renders wrong — transparent, mis-scaled, wrong facing,
a silhouette, or an option list that empties itself — and when planning a
migration away from base64.

## Why this is a separate file

The pitfalls below are ~800 words of forensics on bugs that are real but rare.
Kept inline they were 20% of a skill loaded on *every* tgui task, including the
majority that never touch a preview. The symptoms stay named in SKILL.md so you
can recognise one; the diagnosis lives here.

## Three base64-preview pitfalls proven in the field

**Field case — skill consulted too late:** asked to mock up a tgui panel where two characters' on-screen appearance mirrors their live actions, the assistant produced two rounds of design (separate SVG-placeholder avatars, then a server-side `icon.Blend()` composite-into-one-icon proposal) from general BYOND knowledge before ever opening this skill — despite the user's own message naming `ByondUi` directly (misspelled as "BYOND UI"). Only a third, explicit "is there something for this in the skill?" question triggered the lookup, which immediately surfaced map_view as the priority pattern and made the `icon.Blend()` detour moot. Nothing had shipped yet — it was all chat mockups — so the cost was wasted turns and an anchor toward the wrong architecture, not a bad diff. Lesson folded into the activation guard above: read a live/synced character-appearance request as this skill's domain from the first message that raises it, and lead with the map_view hierarchy before mentioning any compositing alternative.

Three base64-preview pitfalls proven in the field:

- **Custom icon flatteners drift from native rendering.** A hand-rolled `getFlatIcon` clone will not read `appearance.transform` (matrix scales silently do nothing in the preview while working in-game) and its canvas-growth math diverges once several pixel-offset overlays stack. Prefer the native flattener whenever sprites fit its bounds; if you must scale for a flattener, resize the icon itself (`icon.Scale`), never the transform.
- **The NATIVE tg-family `getFlatIcon` carries a canvas-expansion transposition bug** (present in tgstation master itself, `icons.dm` canvas-growth block): the grow condition uses `&&` (fires only when ALL four edges change) and on trigger transposes the tracked bounds (`flatX2 = addY1; flatY1 = addX2`) — one oversized inhand overlay expands all four edges and every later Blend lands off-canvas, so the flatten returns **fully transparent, with zero runtime errors**. Both halves re-verified verbatim against tgstation master (`code/__HELPERS/icons.dm`, the `addX1/addY1` growth block) **and, independently, in a Vanderlin-family fork on 2026-08-31 — identical `&&` and identical transposition, in a helper otherwise older than tg's (no `pixel_w`/`pixel_z` terms). Assume any tg-derived fork inherits this until greped; it is not a tg-only defect.** The two bugs mask each other: the `&&` is itself why upstream rarely trips the transposition, since a typical overlay expands only one or two edges and the resize branch never runs — so **fixing the `&&` to `||` alone, without also straightening the axis assignments, converts a latent bug into a live one.** Fix both together or neither. (Do *not* assume upstream avoids this by stripping held items: tg's `get_flat_human_icon` → `equipOutfit(outfit, TRUE)` still fills hands — `visuals_only` is passed *through* to `put_in_l_hand`/`put_in_r_hand`, and only pockets/backpack are gated behind `if(!visuals_only)`, since hands do show on the sprite.) Fingerprint: preview renders a naked mob fine, dies the moment it holds an item; the canvas doubles while the encoded payload SHRINKS. Fix the helper (`||` + straight-axis assignments) or, without touching it, flatten an appearance snapshot (`image(null)` + `.appearance = mob.appearance` — probe-proven byte-identical to flattening the live mob) with all-four-edge-expanding overlays dropped. The snapshot is also the only reliable way to force facing: `getFlatIcon`'s `defdir` is silently ignored unless the appearance's own dir is SOUTH/unset, so set `.dir = SOUTH` on the snapshot rather than flipping the live mob.
- **Preview-only state must bypass validated preferences.** `write_preference()` silently returns FALSE for out-of-domain values (`is_valid()`), so "force the dummy nude for the preview" via a pref write can silently not happen. Set preview-only state directly on the dummy after `apply_prefs_to()` and rebuild its body — never through the validated pref pipeline.

Keep picker state simple. If a background picker has become `None` / `White` / `Dark`, send those values directly and remove turf thumbnail renderers and option caches. If a helper now returns an `icon` directly, remove any stale cache that used to wrap that helper.

When filtering an option catalog by whitelists (gender, species, coverage), guard the empty result: on modular forks the core whitelist macros routinely omit modular content ids, and an emptied list can cascade — validation marks the entry permanently disabled, the enable toggle silently re-disables every pass, and the feature looks "broken" for exactly the modular species. Give bypass flags to content that must be universal, and fall back to a less-filtered list instead of returning empty.

For hover previews that replace an existing sprite accessory, render the base doll with the current customizer temporarily disabled, cache it by `(customizer, current preview signature)`, and overlay the candidate on that base. Do not stack the candidate over the already-equipped current accessory; it gives plausible screenshots while hiding the actual replacement bug.
