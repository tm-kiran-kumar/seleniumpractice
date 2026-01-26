import pytest
from selenium.webdriver.chrome.options import Options
from pages.sample_element import login
from utilities.excel_utils import get_excel_data

@pytest.mark.smoke
# @pytest.mark.parametrize('username, password', [('student12', 'Password1234'), ('student1', 'Password1234')])
@pytest.mark.parametrize('username, password', get_excel_data())
def test_login(driver, username, password):
    print(f"Testing login for: {username} with password: {password}")
    result = login(driver, username, password)
    print(result)
    assert result == "Your username is invalid!"
