# Troubleshooting - Lab 10: Taking Screenshots

1. **No Screenshot Saved**
   - Ensure the directory has write permissions.
   - Check that `driver.save_screenshot()` points to a valid filename.

2. **Browser Not Opening**
   - Verify ChromeDriver matches your Chrome version.

3. **File Overwritten**
   - Use timestamped filenames to avoid overwriting screenshots.

4. **Image Corrupt or Empty**
   - Ensure the page has fully loaded before capturing the screenshot.
