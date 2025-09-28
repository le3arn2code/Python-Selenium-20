# Interview Q&A - Lab 9 Handling Waits

**Q1. What is an implicit wait in Selenium?**
A1. Implicit wait tells WebDriver to poll DOM for a set time before throwing exception.

**Q2. How is explicit wait different from implicit wait?**
A2. Explicit wait is applied to specific elements with conditions, implicit applies globally.

**Q3. Can you combine implicit and explicit waits?**
A3. Not recommended, can cause unpredictable wait times.

**Q4. What are common explicit wait conditions?**
A4. Visibility, element to be clickable, presence of element.

**Q5. Why use explicit waits over sleep()?**
A5. Explicit waits are smarter; they pause only until condition is met, not fixed time.

**Q6. What happens if element is found before implicit wait time ends?**
A6. WebDriver continues immediately without waiting full duration.

**Q7. Give a scenario for implicit wait.**
A7. When most elements load within a predictable short time, e.g., static websites.

**Q8. Give a scenario for explicit wait.**
A8. Waiting for dynamic element like loading spinner to disappear.

**Q9. What is TimeoutException in explicit waits?**
A9. Raised when condition isn’t met within specified wait time.

**Q10. Which wait improves script efficiency?**
A10. Explicit wait, as it waits only as long as needed.
