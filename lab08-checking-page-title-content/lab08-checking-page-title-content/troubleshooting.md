# Troubleshooting

1. **NoSuchElementException**
   - Ensure the element text (`Downloads`) matches exactly.

2. **AssertionError**
   - The expected title might differ. Confirm the actual title using `driver.title`.

3. **Driver not found**
   - Add ChromeDriver path explicitly:
     ```python
     driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
     ```
