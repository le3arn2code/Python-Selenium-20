# Lab 20: End-to-End Mini Project

## Objectives
- Gain practical experience with an end-to-end testing scenario using an open-source automation tool.
- Navigate and interact with a demo website, focusing on form handling and user interactions.
- Utilize techniques such as waits and screenshots to ensure the reliability and accuracy of test results.
- Validate the successful implementation of each task through the use of assertions and checks.

## Steps
1. **Setup Environment**
   - Ensure Python 3 and Selenium are installed.
   - Install Chrome and matching ChromeDriver.

2. **Run the Test**
   ```bash
   python3 e2e_test.py
   ```

3. **Verify Output**
   - Page title should display "Swag Labs".
   - Login must be successful.
   - "Sauce Labs Backpack" should be added to cart.
   - Cart badge must validate correctly.
   - Screenshot is saved as `saucedemo_result.png`.

4. **Screenshots**
   See included screenshots (`step1.png`, `step2.png`) for test proof.

## Conclusion
This lab demonstrated a complete end-to-end test workflow: environment setup, login, interaction, waits, validations, and capturing results with Selenium in Python.
