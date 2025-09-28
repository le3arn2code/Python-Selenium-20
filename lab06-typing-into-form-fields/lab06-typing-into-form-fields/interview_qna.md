# Interview Q&A for Lab 6

**Q1. What does send_keys() do in Selenium?**  
A: It simulates keyboard input into input fields.

**Q2. How do you locate a text field by ID in Selenium 4?**  
A: `driver.find_element(By.ID, "username")`.

**Q3. What is the difference between click() and send_keys()?**  
A: `click()` simulates mouse clicks, while `send_keys()` types into fields.

**Q4. How do you clear an input field before typing?**  
A: Use `element.clear()` before `send_keys()`.

**Q5. What happens if the locator is incorrect?**  
A: Selenium raises `NoSuchElementException`.

**Q6. Can send_keys() simulate pressing Enter?**  
A: Yes, using `send_keys(Keys.ENTER)`.

**Q7. What are alternative locators besides ID?**  
A: Name, class name, CSS selector, XPATH, tag name, link text.

**Q8. How can you verify text was typed correctly?**  
A: Use `element.get_attribute("value")`.

**Q9. Why is WebDriver quit() important?**  
A: It closes all browser windows and ends the session properly.

**Q10. How do you handle hidden fields?**  
A: Hidden fields cannot receive input with send_keys; use JavaScript execution instead.
