# Interview Q&A for Lab 3

1. **Q:** What are different ways to locate elements in Selenium?
   **A:** ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, CSS Selector, XPath.

2. **Q:** Why is locating by ID preferred?
   **A:** Because IDs are unique and fastest to locate.

3. **Q:** What happens if multiple elements share the same Name?
   **A:** Selenium will return the first match; we can use `find_elements` for all matches.

4. **Q:** How do you locate dynamic elements?
   **A:** Use XPath/CSS with patterns, attributes, or contains functions.

5. **Q:** What is the difference between `find_element` and `find_elements`?
   **A:** `find_element` returns a single WebElement, `find_elements` returns a list.

6. **Q:** How do you verify an element is present before interacting?
   **A:** Use WebDriverWait with Expected Conditions.

7. **Q:** What exception is raised when an element is not found?
   **A:** `NoSuchElementException`.

8. **Q:** Why use explicit waits over implicit waits?
   **A:** Explicit waits are more reliable and target specific conditions.

9. **Q:** How would you debug if Selenium cannot find an element?
   **A:** Check DOM with DevTools, verify locator strategy, add waits, print page source.

10. **Q:** Can Selenium interact with elements inside an iframe?
    **A:** Yes, but you must switch to the iframe first using `driver.switch_to.frame()`.
