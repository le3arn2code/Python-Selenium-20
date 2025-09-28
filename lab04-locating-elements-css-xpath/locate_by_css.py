from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("file:///home/toor/test_page.html")
element = driver.find_element("css selector", ".btn.login-btn")
print("Element found by CSS Selector:", element.get_attribute("outerHTML"))
driver.quit()
