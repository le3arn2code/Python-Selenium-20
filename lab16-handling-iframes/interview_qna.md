# Interview Q&A - Lab 16: Handling iFrames

**Q1: What is an iFrame?**
A: An iFrame is an HTML element that embeds another webpage within the current page.

**Q2: How do you switch to an iFrame in Selenium?**
A: Using `driver.switch_to.frame()` with the iFrame's ID, name, or index.

**Q3: How do you return to the main page after working inside an iFrame?**
A: By using `driver.switch_to.default_content()`.

**Q4: Why did `.clear()` and `.click()` fail in this lab?**
A: Because TinyMCE uses a `<body>` as the editor surface, not a standard input element.

**Q5: What is the correct way to type into TinyMCE?**
A: Select all text with `Keys.CONTROL + "a"`, delete it, and then type using `.send_keys()`.
