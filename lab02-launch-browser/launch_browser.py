from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Point to ChromeDriver
service = Service("/usr/local/bin/chromedriver")

# Configure Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--user-data-dir=/tmp/selenium_profile_lab2")
# Uncomment for headless mode:
# options.add_argument("--headless=new")

# Launch browser
driver = webdriver.Chrome(service=service, options=options)

# Open webpage
driver.get("https://www.example.com")

# Verify navigation
current_url = driver.current_url
print(f"✅ Current URL: {current_url}")

# Close browser
driver.quit()
