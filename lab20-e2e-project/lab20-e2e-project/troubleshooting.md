# Troubleshooting Lab 20

## Common Issues & Fixes

1. **NoSuchElementException**
   - Cause: Locator mismatch or page not fully loaded.
   - Fix: Use explicit waits (`WebDriverWait`) until the element appears.

2. **SessionNotCreatedException**
   - Cause: ChromeDriver version mismatch with Chrome browser.
   - Fix: Download and install the correct ChromeDriver version.

3. **StaleElementReferenceException**
   - Cause: DOM reloaded after locating element.
   - Fix: Re-locate element after reload, or add wait conditions.

4. **Popups like 'Change your password'**
   - Cause: Chrome/Google prompts can appear during login.
   - Fix: Run browser with options to disable password manager prompts:
     ```python
     options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
     ```
