from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Point to ChromeDriver
service = Service("/usr/bin/chromedriver")

# Configure Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--user-data-dir=/tmp/selenium_profile")
# Uncomment next line to run headless
# options.add_argument("--headless=new")

driver = webdriver.Chrome(service=service, options=options)

print("✅ Selenium WebDriver successfully installed and executed!")

driver.quit()
