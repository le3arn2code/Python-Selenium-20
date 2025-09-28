# Troubleshooting

## Issue: AttributeError with `find_element_by_id`
- **Cause**: Selenium 4 deprecated old methods.
- **Fix**: Use new syntax:
  ```python
  from selenium.webdriver.common.by import By
  driver.find_element(By.ID, "username")
  driver.find_element(By.NAME, "user_password")
  ```

## Issue: ChromeDriver not found
- Ensure ChromeDriver is installed and in PATH.
- Verify with `chromedriver --version`.

## Issue: Version mismatch between Chrome and ChromeDriver
- Always match **ChromeDriver version** with **installed Chrome version**.
