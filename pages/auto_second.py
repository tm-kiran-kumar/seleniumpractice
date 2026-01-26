import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class AutoSecond(BasePage):

    # Constants or Locators
    COUNTRY = By.XPATH, "//select[@id='country']"
    COLORS = By.XPATH, "//select[@id='colors']"
    DATE_PICKER = By.XPATH, "//input[@id='datepicker']"
    DATE_PICKER2 = By.XPATH, "//input[@id='txtDate']"
    MONTH = By.XPATH, "//select[@class='ui-datepicker-month']"
    DATE = By.XPATH, "//a[@class='ui-state-default' and text()='25']"
    YEAR = By.XPATH, "//select[@class='ui-datepicker-year']"

    def __init__(self, driver):
        super().__init__(driver)

    # Action Methods
    # Countries of list using Select class
    def countries(self, country):
        ct_list = []
        select_country = Select(self.get_element(self.COUNTRY))
        select_country.select_by_visible_text(country)
        actual_selection = select_country.first_selected_option # First selected state from web after selection
        return actual_selection.text.strip()

    # Color selection
    def colors(self, color_selection):
        select_color = Select(self.get_element(self.COLORS))
        select_color.select_by_visible_text(color_selection)
        capture_color = select_color.first_selected_option.text
        return capture_color

    # Date selection
    def date_picker(self):
        self.send_keys_element(self.DATE_PICKER, '11/25/1988')
        #print('Date Selected')
        time.sleep(2)

        self.click_element(self.DATE_PICKER2)
        time.sleep(2)
        month = Select(self.get_element(self.MONTH))
        time.sleep(2)
        month.select_by_visible_text('Nov')
        print('Selected Month')

        time.sleep(2)
        date = self.get_element(self.DATE)
        print('Selected Date')
        time.sleep(2)

        year = Select(self.get_element(self.YEAR))
        time.sleep(2)
        year.select_by_visible_text('2026')
        print('Selected Year')



