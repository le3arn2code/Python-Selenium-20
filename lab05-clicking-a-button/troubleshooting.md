# Troubleshooting for Lab 5: Clicking a Button

## Common Issues

### 1. NoSuchElementException
- **Error:** `selenium.common.exceptions.NoSuchElementException`
- **Cause:** Selenium cannot find the element.
- **Fix:** Ensure you are using the correct locator (e.g., `By.ID`, `By.NAME`).
  - Verify that the HTML file path is correct (use full absolute path with `file:///`).

### 2. ChromeDriver Version Mismatch
- **Error:** ChromeDriver cannot start session.
- **Fix:** Ensure Chrome and ChromeDriver versions match.

### 3. Permission Errors
- **Error:** `chromedriver: Permission denied`
- **Fix:** Run:
  ```bash
  sudo chmod +x /usr/local/bin/chromedriver
  ```
