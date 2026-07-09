# Icon Rendering

- Open `code/__HELPERS/icons.dm` for flattening/helpers.
- Open smoothing helpers/defines when smoothing flags/groups are involved.
- Static TGUI catalogs should be `/datum/asset` or spritesheets, not repeated base64 in data.
- Dynamic one-off photos/previews may remain direct `browse_rsc`/base64; see `$ss13-tgui`.
