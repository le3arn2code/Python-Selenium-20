# Interview Q&A - Lab 7

**Q1. What does `event.preventDefault()` do in JavaScript?**  
It prevents the default form action (e.g., navigation) when submitting a form.

**Q2. Why use `id` attributes in form fields?**  
To uniquely identify elements for JavaScript or Selenium automation.

**Q3. What are alternative ways to confirm form submission?**  
Using console logs, updating DOM elements, or navigating to a new page.

**Q4. How does JavaScript handle form data submission?**  
By capturing values with `document.getElementById().value` and sending them to a server (e.g., via AJAX).

**Q5. What are required fields in HTML forms?**  
Fields with the `required` attribute, which browsers validate before submission.

**Q6. How can you validate email input?**  
By using `<input type="email">` which ensures correct email formatting.

**Q7. Why log form data to the console?**  
For debugging and verification before sending data to the backend.

**Q8. How do alerts differ from console logs?**  
Alerts show a popup message to the user, while console logs are for developers.

**Q9. What happens if you don’t use `preventDefault()` in form submission?**  
The form will navigate to a new page (or refresh), losing entered data.

**Q10. Why is this lab important for automation?**  
It shows how to handle form input and submission, essential for web testing and automation tasks.
