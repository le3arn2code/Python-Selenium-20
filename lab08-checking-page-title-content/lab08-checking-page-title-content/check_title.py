from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open Python.org
driver.get("https://www.python.org")

# Retrieve Page Title
page_title = driver.title
print(f"Page Title: {page_title}")

# Verify Title
expected_title = "Welcome to Python.org"
assert page_title == expected_title, f"Title mismatch! Expected: {expected_title}, Got: {page_title}"

# Locate "Downloads" link
element = driver.find_element(By.XPATH, "//a[text()='Downloads']")
actual_text = element.text
expected_text = "Downloads"
assert actual_text == expected_text, f"Text mismatch! Expected: {expected_text}, Got: {actual_text}"

print("✅ Title and content validated successfully!")

# Close Browser
driver.quit()
