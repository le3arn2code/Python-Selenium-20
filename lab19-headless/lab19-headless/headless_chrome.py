from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

start_time = time()
driver.get("https://www.example.com")
end_time = time()

print("Page Title:", driver.title)
print(f"Headless Chrome Load Time: {end_time - start_time:.2f} seconds")

driver.save_screenshot("chrome_headless.png")
driver.quit()
