from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    # Reusable methods
    # Waits
    def wait_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    # Send Keys
    def send_keys_element(self, locator, text):
        """Waits, clears then types"""
        element = self.wait_element(locator)
        #element = self.driver.find_element(*locator)
        element.clear()
        return element.send_keys(text)

    def get_text_from_element(self, locator):
        """Use this for Labels, Headers, and Span tags"""
        return self.driver.find_element(*locator).text

    def get_value_from_input(self, locator):
        """Use this for Textboxes and Input fields where you typed something"""
        return self.driver.find_element(*locator).get_attribute("value")

    def get_element(self, locator):
        return self.driver.find_element(*locator)


























