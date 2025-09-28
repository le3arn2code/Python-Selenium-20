from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Load local form page
driver.get("file:///home/toor/form_page.html")

# Locate username field and type text
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("testuser")

# Locate password field and type text
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("securepassword123")

# Confirmation message
print("✅ Username and password fields populated successfully.")

# Pause to visually confirm (optional)
time.sleep(2)

# Close browser
driver.quit()
