# Troubleshooting - Lab 2

## Issue: chromedriver not found
**Fix:** Ensure chromedriver is installed and moved to /usr/local/bin
```bash
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```

## Issue: SessionNotCreatedException (user-data-dir already in use)
**Fix:** Use a unique temporary profile directory:
```python
options.add_argument("--user-data-dir=/tmp/selenium_profile_lab2")
```

## Issue: Externally managed environment (pip install fails)
**Fix:** Use virtual environment
```bash
python3 -m venv selenium-env
source selenium-env/bin/activate
pip install selenium
```
