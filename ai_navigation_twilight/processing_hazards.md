# Processing Hazards

Red flags: `sleep(...)`, `do_after(...)`, `input(...)`, `alert(...)`, `browse(...)`, heavy icon/JSON work, or unbounded signal callbacks inside process/fire paths.

```powershell
rg -n "process\(|fire\(|START_PROCESSING|STOP_PROCESSING|sleep\(|do_after\(" code modular_twilight_axis modular modular_deserttown -g "*.dm"
```
