from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Open a browser and website
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

# Step 2: Click the link that opens a new tab
link = driver.find_element(By.LINK_TEXT, "Click Here")
link.click()

# Step 3: Get all window handles
window_handles = driver.window_handles
print(f"Total open windows/tabs: {len(window_handles)}")

# Step 4: Switch through each window and print title + URL
for handle in window_handles:
    driver.switch_to.window(handle)
    print(f"Title: {driver.title}, URL: {driver.current_url}")

# Step 5: Close the browser
driver.quit()
