from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = Options()
options.add_argument("--headless=new")  # run headless (no GUI)

# Point to ChromeDriver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Open the local HTML file (absolute path)
driver.get("file:///home/toor/button_page.html")

# Wait until the button is present
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sampleButton"))
)

# Click the button
button.click()
print("✅ Button clicked successfully!")

# Close browser
driver.quit()
