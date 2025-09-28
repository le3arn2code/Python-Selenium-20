# Troubleshooting - Lab 16: Handling iFrames

**Issue 1: InvalidElementStateException**
- Cause: Using `.clear()` on TinyMCE body element (not a real input field).
- Fix: Use `send_keys(Keys.CONTROL + "a", Keys.DELETE)`.

**Issue 2: ElementClickInterceptedException**
- Cause: Attempting to `.click()` on TinyMCE body intercepted by overlay.
- Fix: Avoid `.click()`. Directly use `.send_keys()` to type text.

**General Tips:**
- Always switch to the iFrame first: `driver.switch_to.frame("mce_0_ifr")`.
- Return to main content after: `driver.switch_to.default_content()`.
