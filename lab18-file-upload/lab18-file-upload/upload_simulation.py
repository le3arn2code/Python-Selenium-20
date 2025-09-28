from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Launch browser
driver = webdriver.Chrome()

# Load local test HTML
file_path = f"file://{os.path.abspath('upload_test.html')}"
driver.get(file_path)
print("✅ Opened test upload page.")

# Locate file input
file_input = driver.find_element(By.ID, "fileInput")

# Select test file
file_to_upload = os.path.abspath("sample.txt")
file_input.send_keys(file_to_upload)
print(f"📂 File selected: {file_to_upload}")

# Submit form
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
print("🚀 Form submitted (simulated upload).")

time.sleep(2)
driver.quit()
print("✅ Test completed.")
