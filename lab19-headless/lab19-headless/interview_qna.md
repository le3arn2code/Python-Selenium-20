# Interview Q&A - Lab 19

**Q1: What is headless mode in Selenium?**  
A: Running a browser without a graphical user interface.

**Q2: Which browsers support headless mode in Selenium?**  
A: Chrome and Firefox both support it. Chrome is more reliable in server setups.

**Q3: How do you run Chrome in headless mode?**  
```python
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

**Q4: Why might Firefox headless fail on some servers?**  
A: Due to X11 authentication conflicts in some Linux environments.

**Q5: Why is headless mode useful in CI/CD pipelines?**  
A: It reduces resource usage and works in environments without a display.
