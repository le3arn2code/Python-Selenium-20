# Lab 4: Interview Q&A

1. **Q:** What is the difference between CSS Selector and XPATH?
   **A:** CSS is simpler and faster, while XPATH is more flexible and powerful for complex DOM structures.

2. **Q:** When would you prefer CSS Selector over XPATH?
   **A:** For speed and readability when selecting by class, ID, or hierarchy.

3. **Q:** When would you prefer XPATH?
   **A:** When working with complex or dynamic HTML structures where CSS fails.

4. **Q:** What is an absolute XPATH?
   **A:** It starts from the root of the HTML (`/html/body/...`) and specifies the full path.

5. **Q:** What is a relative XPATH?
   **A:** It starts with `//` and can find elements anywhere in the DOM.

6. **Q:** How do you handle dynamic elements in Selenium?
   **A:** Use contains, starts-with, or normalize-space functions in XPATH.

7. **Q:** Which is faster: CSS or XPATH?
   **A:** Generally, CSS is faster and more efficient.

8. **Q:** Can CSS Selectors traverse backwards in DOM like XPATH?
   **A:** No, CSS can only go downwards, while XPATH can traverse both ways.

9. **Q:** How do you debug CSS Selectors or XPATH in Chrome?
   **A:** Use Developer Tools Console: `document.querySelector()` or `$x()`.

10. **Q:** Why is locating elements important in Selenium?
    **A:** Accurate element location is the foundation of reliable test automation.
