from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/large")

# Scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("✅ Scrolled to bottom successfully.")

# Scroll a paragraph element into view
element = driver.find_element(By.TAG_NAME, "p")
driver.execute_script("arguments[0].scrollIntoView();", element)
print("✅ Scrolled into view: A paragraph element")

# Verify element visibility
if element.is_displayed():
    print("Element is visible on the page.")
else:
    print("Element is NOT visible on the page.")

driver.quit()
