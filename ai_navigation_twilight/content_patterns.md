# Content Patterns

| Pattern | Use when | Twilight route |
|---|---|---|
| Subtype | New item/mob/turf/structure variant | nearest existing branch, prefer overlay |
| Component | Behavior attaches to many owners | code/datums/components/** or overlay equivalent |
| Element | Lightweight shared behavior | code/datums/elements/** if local pattern exists |
| Status effect | Timed mob state | status effect dirs |
| Signal listener | React to existing events | signal_map.md, register/unregister cleanly |
| Subsystem | Global scheduler/state owner | high risk; use only for real global ownership |
| TGUI interface | Player/admin browser UI | $ss13-tgui |
