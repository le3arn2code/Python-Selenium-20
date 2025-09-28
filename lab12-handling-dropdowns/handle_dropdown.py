from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Load local HTML file
driver.get("file:///home/toor/dropdown.html")

# Locate dropdown
dropdown = driver.find_element("id", "dropdown-example")
select_element = Select(dropdown)

# Select options
select_element.select_by_visible_text("Option 2")
time.sleep(2)

select_element.select_by_value("3")
time.sleep(2)

# Print currently selected option
selected_option = select_element.first_selected_option
print("Selected option:", selected_option.text)

# Close browser
driver.quit()
