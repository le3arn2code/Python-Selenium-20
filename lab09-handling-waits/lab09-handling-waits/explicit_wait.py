from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("file:///home/toor/wait_test.html")

# Explicit wait up to 10 seconds
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "delayedButton")))
print("✅ Button clicked using Explicit Wait!")
button.click()

driver.quit()
