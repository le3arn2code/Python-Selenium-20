# Troubleshooting - Lab 14: Handling Alerts

**Issue 1:** `selenium.common.exceptions.NoAlertPresentException`
- Cause: Script tried to switch to an alert before it appeared.
- Fix: Add a short delay or WebDriverWait before switching.

**Issue 2:** `chromedriver not found`
- Cause: ChromeDriver is not in PATH.
- Fix: Download ChromeDriver and place it in the PATH or specify executable_path.

**Issue 3:** Alert not handled properly
- Ensure the correct alert button is clicked before switching to alert.
