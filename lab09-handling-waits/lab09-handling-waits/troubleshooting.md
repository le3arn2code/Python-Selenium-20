# Troubleshooting - Lab 9

1. **NoSuchElementException**
   - Check if the element ID is correct.
   - Ensure waits are set before locating elements.

2. **TimeoutException**
   - Explicit wait timed out. Increase wait duration or verify element is truly clickable.

3. **Version mismatch (Chrome vs ChromeDriver)**
   - Ensure ChromeDriver matches your Chrome version.

4. **Multiple finds with implicit wait**
   - Remember implicit waits apply globally to all element searches.
