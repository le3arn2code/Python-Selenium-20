from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///home/toor/wait_test.html")

# Set implicit wait
driver.implicitly_wait(5)

# Try locating delayed button
button = driver.find_element(By.ID, "delayedButton")
print("✅ Found button using Implicit Wait:", button.text)

driver.quit()
