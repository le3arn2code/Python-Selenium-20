# Interview Q&A - Lab 11: Locating Multiple Elements

1. **Q: How do you locate multiple elements in Selenium?**  
   A: Using `find_elements` with a locator strategy like tag name or class.

2. **Q: What is the return type of `find_elements`?**  
   A: A list of WebElement objects.

3. **Q: How do you extract text from all located elements?**  
   A: Iterate over the list and use `.text` property.

4. **Q: How do you get attributes like href from links?**  
   A: Use `.get_attribute("href")`.

5. **Q: Difference between `find_element` and `find_elements`?**  
   A: `find_element` returns the first matching element, `find_elements` returns all matches as a list.

6. **Q: What happens if `find_elements` finds nothing?**  
   A: Returns an empty list (no exception).

7. **Q: Can you use XPath with `find_elements`?**  
   A: Yes, `driver.find_elements("xpath", "//a")`.

8. **Q: How to count total elements found?**  
   A: Use `len(elements)`.

9. **Q: How is locating multiple elements useful in automation?**  
   A: For scraping, validating lists, menus, or repeated elements.

10. **Q: How do you handle dynamic links?**  
   A: Use explicit waits before locating elements.
