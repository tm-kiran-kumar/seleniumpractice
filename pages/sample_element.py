import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


# options = Options()
# options.add_argument('--headless=new')
# driver = webdriver.Chrome(options=options)
# # driver.get('https://practicetestautomation.com/practice-test-login/')
# # driver.maximize_window()

# Login
def login(driver, username, password):
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()
    time.sleep(3)
    status = driver.find_element(By.ID, "error")
    result1 = status.text
    return result1