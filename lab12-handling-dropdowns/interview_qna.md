# Lab 12 Interview Q&A

**Q1: How do you handle dropdowns in Selenium?**  
A: Use the `Select` class to interact with <select> elements.

**Q2: What are the methods to select options in a dropdown?**  
A: By visible text, by value, and by index.

**Q3: Why use `first_selected_option`?**  
A: To retrieve the currently selected option’s text.

**Q4: Can you handle multi-select dropdowns?**  
A: Yes, Selenium provides methods like `select_by_index`, `deselect_all`, etc.

**Q5: What happens if you try to select a non-existent option?**  
A: Selenium throws a `NoSuchElementException`.
