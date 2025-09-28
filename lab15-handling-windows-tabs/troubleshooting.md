# Troubleshooting

1. **Error: AttributeError: 'WebDriver' object has no attribute 'find_element_by_link_text'**
   - Cause: Deprecated methods in Selenium 4.
   - Fix: Use `driver.find_element(By.LINK_TEXT, "Click Here")` with `from selenium.webdriver.common.by import By`.

2. **Error: WebDriver not compatible with browser version**
   - Ensure Chrome and ChromeDriver versions match.

3. **Windows not switching**
   - Verify that the link opens in a new tab (`target="_blank"`).
