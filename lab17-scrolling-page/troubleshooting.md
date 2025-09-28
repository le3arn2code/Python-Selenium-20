# Troubleshooting - Lab 17

## Issue: NoSuchElementException
```
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//div[@class='footer']"}
```
### Cause:
The target element `//div[@class='footer']` was not found on the page.

### Fix:
- Replace the locator with an existing element, e.g. `//p` for a paragraph element.
- Always inspect the target site structure with browser DevTools before writing locators.

## Verified Fix:
Used `By.TAG_NAME, "p"` instead of searching for a missing footer div.
