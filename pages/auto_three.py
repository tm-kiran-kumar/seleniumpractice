from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AutoThree(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    TABLE = By.XPATH, "//table[@name='BookTable']"

    def table_info(self):
        table = self.get_element(self.TABLE)
        rows = table.find_elements(By.TAG_NAME, 'tr')

        table_data = []
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, 'td')
            all_list = [col.text for col in cols]
            table_data.append(all_list)

        return table_data
