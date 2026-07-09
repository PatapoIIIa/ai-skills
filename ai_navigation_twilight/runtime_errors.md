# Runtime Errors

| Runtime shape | Likely cause | Route |
|---|---|---|
| Cannot read null.X after delay | ref invalid after sleep/do_after | source proc + revalidate refs |
| Bad index / list access | DM list shape mismatch | source proc, frontend JSON type if TGUI |
| Hard delete / qdel warning | cleanup contract broken | Destroy/qdel path + coding_standards.md |
| Cannot execute proc on deleted object | timer/signal callback outlived owner | signal_map.md + cleanup |
| TGUI minified/fatal JS error | frontend import/component/data shape | tgui_guide.md + $ss13-tgui |
| Asset 404 / missing image | unregistered asset or stale mapping | tgui_guide.md asset section |
