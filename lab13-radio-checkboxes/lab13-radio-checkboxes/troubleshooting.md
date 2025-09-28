# Troubleshooting Lab 13

## Issue: Puppeteer fails to launch Chromium with error:
```
No usable sandbox!
```
### Fix:
Use Puppeteer launch flags:
```js
const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
});
```

---

## Issue: `node: command not found`
### Fix:
Install Node.js and npm:
```bash
sudo apt install -y nodejs npm
```
