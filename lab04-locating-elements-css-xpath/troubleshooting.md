# Troubleshooting Lab 4

## Common Issues

1. **Selenium Deprecated Syntax**
   - Old: `driver.find_element_by_css_selector()`
   - New: `driver.find_element("css selector", "value")`
   - Old: `driver.find_element_by_xpath()`
   - New: `driver.find_element("xpath", "value")`

2. **ChromeDriver not found**
   - Ensure `chromedriver` is installed and in PATH.
   - Run `chromedriver --version` to confirm.

3. **Version mismatch**
   - ChromeDriver must match installed Google Chrome version.
   - Re-download correct driver if mismatch occurs.

4. **Permission denied**
   - Run `sudo chmod +x /usr/local/bin/chromedriver`.
