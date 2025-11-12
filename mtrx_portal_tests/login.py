from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# Navigate to the MTRX Admin Portal
driver.get("https://admin.mobiletechrx.com")
# Find the element 
element = driver.find_element(By.CLASS_NAME, "call-to-action")
# Check that text is present
assert element.text == "Log In"

driver.quit()
