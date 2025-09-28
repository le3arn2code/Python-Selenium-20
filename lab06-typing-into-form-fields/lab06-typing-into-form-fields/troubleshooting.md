# Troubleshooting Lab 6

## Common Issues

### 1. NoSuchElementException
- **Cause**: The element ID or locator is wrong.
- **Fix**: Double-check the `id="username"` or `id="password"` in HTML and Python script.

### 2. ChromeDriver version mismatch
- **Cause**: Chrome and ChromeDriver versions differ.
- **Fix**: Install the exact matching ChromeDriver.

### 3. Permission errors
- **Cause**: chromedriver not executable.
- **Fix**: Run `sudo chmod +x /usr/local/bin/chromedriver`.
