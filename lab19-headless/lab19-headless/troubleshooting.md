# Troubleshooting - Lab 19

### Chrome Headless
- Works fine when Chrome and ChromeDriver versions match.

### Firefox Headless
Error: `X11 connection rejected because of wrong authentication` or `Process unexpectedly closed with status 1`
- Cause: Newer Firefox builds sometimes still try to connect to X11 even in headless mode.
- Fixes tried:
  - Using `options.headless = True`
  - Running with `MOZ_HEADLESS=1`
  - Clearing `DISPLAY` environment variable
- If error persists: **Use Chrome headless for this lab.**
