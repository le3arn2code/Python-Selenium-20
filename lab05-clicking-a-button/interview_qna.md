# Interview Q&A - Lab 5: Clicking a Button

**Q1: How does Selenium locate a button?**  
A1: By using locators like ID, Name, Class, CSS Selector, or XPATH.

**Q2: What happens if Selenium cannot find the button?**  
A2: It raises a `NoSuchElementException`.

**Q3: How can you wait for an element to be available?**  
A3: Use WebDriverWait with Expected Conditions (EC).

**Q4: Can Selenium interact with hidden buttons?**  
A4: No, it can only click visible and enabled elements.

**Q5: Why is `By.ID` preferred?**  
A5: Because IDs are unique and the fastest locator.

**Q6: How can you debug when Selenium fails to click a button?**  
A6: Check page source, wait for page load, confirm element locator.

**Q7: What alternatives exist for button clicks?**  
A7: You can use JavaScript `execute_script("arguments[0].click()", element)`.

**Q8: How to verify a click worked?**  
A8: Check changes in DOM, URL, or page source after the click.

**Q9: What if multiple buttons share the same class?**  
A9: Use indexing (`find_elements`) or a more specific locator.

**Q10: How to handle dynamic buttons loaded later?**  
A10: Use explicit waits until the element is present and clickable.
