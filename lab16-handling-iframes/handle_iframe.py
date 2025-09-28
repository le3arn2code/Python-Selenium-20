from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch browser and open the test page
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

# Step 2: Switch to the iFrame
driver.switch_to.frame("mce_0_ifr")
print("Switched into the iFrame successfully.")

# Step 3: Target the <body> inside the iFrame
textbox = driver.find_element(By.ID, "tinymce")

# Clear text safely: CTRL + A then DELETE
textbox.send_keys(Keys.CONTROL + "a")
textbox.send_keys(Keys.DELETE)

# Type new text directly
textbox.send_keys("Hello from Lab 16 – typing inside an iFrame works now!")
print("Typed inside the iFrame successfully.")

# Step 4: Switch back to main page
driver.switch_to.default_content()
header = driver.find_element(By.TAG_NAME, "h3")
print("Main page header text:", header.text)

# Step 5: Pause and close
time.sleep(2)
driver.quit()
