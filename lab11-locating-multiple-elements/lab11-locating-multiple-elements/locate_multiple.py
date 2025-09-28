from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to example page
driver.get("https://example.com")

# Locate all <a> elements (links)
links = driver.find_elements("tag name", "a")

# Print link text and href attributes
for link in links:
    print(link.text, link.get_attribute("href"))

# Print total number of links
print(f"Total number of links found: {len(links)}")

# Close WebDriver
driver.quit()
