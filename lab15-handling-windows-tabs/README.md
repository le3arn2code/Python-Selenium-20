# Lab 15: Handling Multiple Windows/Tabs

## Objectives
- Understand how to handle multiple browser windows or tabs using automation.
- Learn to switch between windows/tabs using appropriate commands.
- Practice extracting information from different tabs.

## Tasks
1. Open a new tab or window by clicking a link or directly.
2. Use `driver.window_handles` to list all open windows.
3. Switch between windows using `driver.switch_to.window(handle)`.
4. Print titles and URLs for each open window/tab.

## What Was Fixed
Selenium 4 deprecated `find_element_by_*` methods.  
- ❌ Old: `driver.find_element_by_link_text("Click Here")`  
- ✅ Fixed: `driver.find_element(By.LINK_TEXT, "Click Here")` (with `from selenium.webdriver.common.by import By`)

This update fixed the AttributeError seen in Selenium 4.18.1.

---
