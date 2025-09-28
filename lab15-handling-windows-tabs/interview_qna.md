# Interview Q&A for Lab 15

**Q1: How do you get all open window handles in Selenium?**  
A: Use `driver.window_handles`, which returns a list of all open windows/tabs.

**Q2: How do you switch to a specific tab/window?**  
A: Use `driver.switch_to.window(handle)`.

**Q3: How do you know which window is active?**  
A: Use `driver.current_window_handle`.

**Q4: What happens if you try to interact with an element in a background tab without switching?**  
A: Selenium will throw a `NoSuchElementException` because it can only interact with the active tab.

**Q5: Why did `find_element_by_link_text` fail in this lab?**  
A: Because Selenium 4 deprecated `find_element_by_*` methods. You must now use `find_element(By.LINK_TEXT, "...")`.
