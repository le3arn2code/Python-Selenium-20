from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the HTML test page
driver.get('file:///home/toor/test_page.html')

# Locate element by ID
username_element = driver.find_element("id", "username")

# Retrieve and print value
print("Element with ID 'username':", username_element.get_attribute("outerHTML"))

# Close the browser
driver.quit()
