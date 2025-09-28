from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("file:///home/toor/test_page.html")
element = driver.find_element("xpath", "//button[text()='Login']")
print("Element found by XPATH:", element.get_attribute("outerHTML"))
driver.quit()
