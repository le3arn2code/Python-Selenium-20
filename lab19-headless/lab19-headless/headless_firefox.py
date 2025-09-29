from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

driver.get("https://www.example.com")
print("Page Title:", driver.title)
driver.save_screenshot("firefox_headless.png")

driver.quit()
