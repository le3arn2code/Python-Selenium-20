# Interview Q&A - Lab 17: Scrolling the Page

**Q1: How do you scroll to the bottom of a page in Selenium?**
A1: By executing JavaScript with `driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")`.

**Q2: How can you bring a specific element into view?**
A2: Use `driver.execute_script("arguments[0].scrollIntoView();", element)`.

**Q3: How do you confirm an element is visible?**
A3: Use the `.is_displayed()` method on the WebElement.

**Q4: What kind of exceptions can occur while scrolling?**
A4: Common ones are `NoSuchElementException` (wrong locator) or `StaleElementReferenceException` (element reloads after scroll).
