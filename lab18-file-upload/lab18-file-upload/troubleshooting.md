# Troubleshooting - Lab 18

## Issue 1: ERR_FILE_NOT_FOUND
**Cause:** Script was pointing to `file:///upload` instead of actual HTML file.
**Fix:** Used `os.path.abspath()` in Python script to load the correct `upload_test.html`.

## Issue 2: Element Not Found
**Cause:** Wrong locator or missing test HTML.
**Fix:** Verified locators and ensured `upload_test.html` was in same directory.
