from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the HTML test page
driver.get('file:///home/toor/test_page.html')

# Locate element by Name
password_element = driver.find_element("name", "user_password")

# Retrieve and print value
print("Element with Name 'user_password':", password_element.get_attribute("outerHTML"))

# Close the browser
driver.quit()
