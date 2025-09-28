# Interview Q&A - Lab 10: Taking Screenshots

**Q1: How do you capture a screenshot with Selenium?**  
A: By using `driver.save_screenshot("filename.png")`.

**Q2: Why use timestamps in filenames?**  
A: To prevent overwriting and organize screenshots chronologically.

**Q3: How to verify a screenshot was saved?**  
A: Check the directory for the file or use `os.path.exists()` in Python.

**Q4: What is the difference between static and dynamic content screenshots?**  
A: Static pages look the same, dynamic pages may change depending on timing or user actions.

**Q5: Can Selenium take element-specific screenshots?**  
A: Yes, by locating the element and using `element.screenshot("file.png")`.

**Q6: What format does Selenium save screenshots in?**  
A: PNG format by default.

**Q7: How would you handle failed screenshot saving?**  
A: Add error handling with try/except and confirm file creation.

**Q8: Why is screenshot automation useful in testing?**  
A: For debugging UI issues, validating layouts, and keeping execution records.

**Q9: What modules besides `time` can help with filenames?**  
A: `datetime` for more detailed timestamps.

**Q10: Can screenshots be taken in headless mode?**  
A: Yes, Chrome/Firefox headless mode supports screenshots.
