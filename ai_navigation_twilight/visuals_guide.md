# Visuals Guide

| Area | Path |
|---|---|
| Icon helpers | code/__HELPERS/icons.dm |
| Overlay subsystem | code/controllers/subsystem/overlays.dm |
| Vis overlay subsystem | code/controllers/subsystem/vis_overlays.dm |
| Lighting subsystem | code/controllers/subsystem/lighting.dm |
| Particle weather | code/controllers/subsystem/particle_weather.dm, code/controllers/subsystem/particle_weather_outdoors.dm |
| Icons/assets | icons/**, html/**, code/modules/asset_cache/** |

Performance rule: cache stable appearances and avoid per-tick icon rebuilds. For TGUI previews, use `$ss13-tgui`.
