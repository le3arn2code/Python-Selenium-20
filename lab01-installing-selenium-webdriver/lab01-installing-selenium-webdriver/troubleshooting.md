# Troubleshooting – Lab 1

## Common Issues
1. **Selenium Manager errors** → Use explicit ChromeDriver path with `Service()`.
2. **executable_path deprecated** → Use `Service("/path/to/chromedriver")` instead.
3. **Profile already in use** → Use `--user-data-dir` in Chrome Options.
4. **Chrome not opening on servers** → Add `--headless=new` to run headless.
