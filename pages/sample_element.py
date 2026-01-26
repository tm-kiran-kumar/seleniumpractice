from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.implicitly_wait(5)

# Table