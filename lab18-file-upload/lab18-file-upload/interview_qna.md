# Interview Q&A - Lab 18

**Q1: How does Selenium handle file uploads?**
A: By sending the file path to an `<input type="file">` element using `.send_keys()`.

**Q2: Why not use `click()` for file selection?**
A: File dialogs are OS-level and not controlled by Selenium, so `.send_keys()` is used.

**Q3: How can you verify a file is uploaded successfully?**
A: Check confirmation messages or ensure file input contains the correct file path.

**Q4: What if the upload button is disabled until a file is selected?**
A: Ensure `.send_keys()` is executed first, then interact with the submit button.
