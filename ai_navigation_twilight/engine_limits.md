# Engine Limits

- BYOND tick budget is finite; long loops need `CHECK_TICK` or an existing batching pattern.
- Do not block subsystem `fire()`/`process()` paths with sleeps, prompts, browse calls, or synchronous icon generation.
- References can go stale after sleeps/do_after; revalidate critical refs and state.
- Appearance/overlay churn can dominate client/network cost.
- TGUI first open can be asset/WebView/bundle cost; separate first-open delay from per-click update cost.
