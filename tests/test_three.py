import pytest
from selenium import webdriver

from pages.auto_three import AutoThree

@pytest.mark.smoke
def test_table(driver):
    auto3 = AutoThree(driver)
    result = auto3.table_info()
    print(result)

