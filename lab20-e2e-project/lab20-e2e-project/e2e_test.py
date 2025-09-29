from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome WebDriver
service = Service("/usr/local/bin/chromedriver")
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)

# ---- Navigate to site ----
driver.get("https://www.saucedemo.com/")
print("Page Title:", driver.title)

# ---- Login ----
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
assert "inventory" in driver.current_url, "Login failed!"
print("Login successful.")

# ---- Add to cart (Sauce Labs Backpack) ----
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
print("Clicked Add to Cart for Sauce Labs Backpack")

# ---- Wait for cart badge text ----
try:
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
    )
    print("Cart validation successful.")
except Exception as e:
    print("Cart badge not found:", str(e))

# ---- Screenshot ----
driver.save_screenshot("saucedemo_result.png")
print("Screenshot saved as saucedemo_result.png")

driver.quit()
