# Lab 13: Radio/Checkboxes Interview Q&A

**Q1. How do you locate a radio button in Puppeteer?**  
A1. Use a CSS selector, e.g.:
```js
await page.click('input[name="fruit"][value="banana"]');
```

**Q2. How do you handle multiple checkboxes at once?**  
A2. Loop over their selectors or call `page.click()` for each.

**Q3. Why do we need `--no-sandbox` in Puppeteer on Ubuntu EC2?**  
A3. Because unprivileged user namespaces are disabled, Chromium cannot start its sandbox, so we must disable it for labs.

**Q4. What’s the difference between Selenium and Puppeteer for this task?**  
A4. Both can handle radio/checkboxes, but Puppeteer is Node.js-native and often simpler for headless Chrome automation.
