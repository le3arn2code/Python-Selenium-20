# Troubleshooting - Lab 11

1. **Error: WebDriver not found**
   - Ensure ChromeDriver is installed and in your PATH.
   - Check with: `chromedriver --version`.

2. **Error: selenium not installed**
   - Install using: `pip install selenium`.

3. **Empty link list**
   - Make sure the target webpage has `<a>` tags.
   - Test with `https://example.com`.

4. **Permission denied when running commands.sh**
   - Run: `chmod +x commands.sh`.
