from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AutoFirst(BasePage):

    # Constants or Locators
    NAME_FIELD = By.XPATH, "//input[@id='name']"
    EMAIL_FIELD = By.XPATH, "//input[@id='email']"
    PHONE_FIELD = By.XPATH, "//input[@id='phone']"
    GENDER_MALE = By.XPATH, "//input[@id='male']"
    GENDER_FEMALE = By.XPATH, "//input[@id='female']"
    DAY_SUNDAY = By.XPATH, "//input[@id='sunday']"
    DAY_MONDAY = By.XPATH, "//input[@id='monday']"
    DAY_TUESDAY = By.XPATH, "//input[@id='tuesday']"
    DAY_WEDNESDAY = By.XPATH, "//input[@id='wednesday']"
    DAY_THURSDAY = By.XPATH, "//input[@id='thursday']"
    DAY_FRIDAY = By.XPATH, "//input[@id='friday']"
    DAY_SATURDAY = By.XPATH, "//input[@id='saturday']"

    # Actions
    def __init__(self, driver):
        super().__init__(driver)
        # Without super(), you would have to write self.driver = driver in every single page class you create.
        # By putting it in the BasePage and calling it with super(), you write it once and reuse it everywhere.

    def enter_username(self, name):
        self.send_keys_element(self.NAME_FIELD, name)
        return self.get_value_from_input(self.NAME_FIELD)

    def enter_email(self, email):
        self.send_keys_element(self.EMAIL_FIELD, email)

    def enter_phone(self, phone):
        self.send_keys_element(self.PHONE_FIELD, phone)

    def radio_btn(self, gender='male'):
        if gender == 'male':
            self.click_element(self.GENDER_MALE)
        else:
            self.click_element(self.GENDER_FEMALE)

    def days_select(self, *args):
        days_list = [*args]
        # Select based on list match
        res = []
        for day in days_list:
            if day == 'sunday':
                self.click_element(self.DAY_SUNDAY)
                res.append(day)
            elif day == 'monday':
                self.click_element(self.DAY_MONDAY)
                res.append(day)
            elif day == 'tuesday':
                self.click_element(self.DAY_TUESDAY)
                res.append(day)
            elif day == 'wednesday':
                self.click_element(self.DAY_WEDNESDAY)
                res.append(day)
            elif day == 'thursday':
                self.click_element(self.DAY_THURSDAY)
                res.append(day)
            elif day == 'friday':
                self.click_element(self.DAY_FRIDAY)
                res.append(day)
            elif day == 'saturday':
                self.click_element(self.DAY_SATURDAY)
                res.append(day)
            else:
                print('Invalid Day Name')
        return res


