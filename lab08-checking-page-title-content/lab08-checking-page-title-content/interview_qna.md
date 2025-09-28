# Interview Q&A

**Q1:** How does Selenium retrieve the page title?  
**A1:** Using `driver.title`, which fetches the `<title>` element of the loaded page.

**Q2:** How to validate dynamic text?  
**A2:** Use substring checks: `assert "partial" in element.text`.

**Q3:** Difference between XPath and CSS Selector?  
**A3:** XPath can traverse in both directions of DOM, while CSS Selectors are simpler and faster.

**Q4:** Why should we quit the driver?  
**A4:** To free system resources and prevent hanging processes.
