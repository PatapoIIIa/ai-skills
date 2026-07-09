# Modular Guide

Generated on 2026-07-09.

| Path | Role | Evidence |
|---|---|---|
| modular_twilight_axis/** | Primary Twilight-Axis overlay; prefer for Twilight-specific new work and fixes. | First include line 3595; last include line 4137 in `roguetown.dme`. |
| modular_deserttown/** | Secondary desert map/content overlay. | Included after Twilight block, lines 4138-4185. |
| modular/** | Legacy modular layer inherited from earlier fork work. | Included before Twilight block, lines 3488-3594. |
| code/** | Core/upstream-style code. | Use when the owner is genuinely core or no modular extension exists; classify risk first. |


Rules:

- Prefer `modular_twilight_axis/**` for new Twilight-local content.
- If fixing behavior in `code/**`, first check overlay directories for extensions.
- For TGUI files, backend may live in an overlay while frontend lives in `tgui/packages/tgui/interfaces/**`.
