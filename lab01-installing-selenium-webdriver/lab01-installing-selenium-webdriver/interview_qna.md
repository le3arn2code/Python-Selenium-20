# Interview Q&A – Lab 1

1. **What is Selenium WebDriver?**  
   A tool for automating web browsers programmatically.

2. **Why do we need ChromeDriver?**  
   It bridges Selenium and the Chrome browser.

3. **Difference between Selenium and WebDriver?**  
   Selenium is a suite; WebDriver is the specific browser automation tool.

4. **What changed in Selenium v4 about executable_path?**  
   It was deprecated; use `Service()` instead.

5. **How do you handle Chrome profiles in Selenium?**  
   Use `Options().add_argument("--user-data-dir=/tmp/...")`.

6. **How do you run Selenium in headless mode?**  
   Add `options.add_argument("--headless=new")`.

7. **What happens if ChromeDriver version mismatches?**  
   SessionNotCreatedException will be raised.

8. **What is Selenium Manager?**  
   A helper in Selenium 4 to auto-download drivers.

9. **How to verify Selenium is installed?**  
   Run `pip show selenium`.

10. **How to close the browser after a test?**  
    Call `driver.quit()`.
