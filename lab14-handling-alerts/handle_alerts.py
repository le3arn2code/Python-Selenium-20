from selenium import webdriver
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open test page
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

# Handle JS Alert
alert_button = driver.find_element("xpath", "//button[text()='Click for JS Alert']")
alert_button.click()
alert = driver.switch_to.alert
print("Alert says:", alert.text)
alert.accept()
print("Alert accepted successfully.")

# Handle JS Confirm
confirm_button = driver.find_element("xpath", "//button[text()='Click for JS Confirm']")
confirm_button.click()
confirm_alert = driver.switch_to.alert
print("Confirm alert text:", confirm_alert.text)
confirm_alert.dismiss()
print("Confirm alert dismissed successfully.")

# Handle JS Prompt
prompt_button = driver.find_element("xpath", "//button[text()='Click for JS Prompt']")
prompt_button.click()
prompt_alert = driver.switch_to.alert
print("Prompt alert text:", prompt_alert.text)
prompt_alert.send_keys("Test input")
prompt_alert.accept()
print("Prompt accepted with input.")

time.sleep(2)
driver.quit()
