# Performance Gotchas

1. Hot loops without `CHECK_TICK`.
2. `sleep`/`do_after`/`browse` in process/fire paths.
3. Repeated icon flattening/base64 generation for static catalogs.
4. Unbounded `RegisterSignal` without cleanup.
5. START_PROCESSING without matching STOP_PROCESSING.
6. Static caches that never invalidate.
7. TGUI autoupdate on heavy `ui_data` payloads.
