from selenium import webdriver
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.example.com")

# ---- Basic Screenshot ----
screenshot_file = "screenshot.png"
driver.save_screenshot(screenshot_file)
print(f"Basic screenshot saved as: {screenshot_file}")

# ---- Screenshot with Timestamp ----
timestamp = time.strftime("%Y%m%d-%H%M%S")
timestamped_file = f"screenshot_{timestamp}.png"
driver.save_screenshot(timestamped_file)
print(f"Timestamped screenshot saved as: {timestamped_file}")

# Close the browser
driver.quit()
