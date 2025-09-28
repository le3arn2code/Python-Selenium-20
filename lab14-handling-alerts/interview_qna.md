# Interview Q&A - Lab 14: Handling Alerts

**Q1: How do you switch to an alert in Selenium?**
A: Use `driver.switch_to.alert`.

**Q2: How do you accept or dismiss an alert?**
A: `alert.accept()` to accept, `alert.dismiss()` to cancel/dismiss.

**Q3: How can you retrieve the text from an alert?**
A: Use `alert.text`.

**Q4: How do you handle prompt alerts in Selenium?**
A: Use `alert.send_keys("text")` to send input before accepting.

**Q5: Why is handling alerts important in test automation?**
A: Alerts are common in applications (confirmation, prompts, warnings). Handling them ensures smooth automated flows.
