from pages.auto_second import AutoSecond
import pytest


@pytest.mark.smoke
def test_autopage1(driver):
    auto1 = AutoSecond(driver)

    # Countries
    country = 'India'
    selected = auto1.countries(country)
    print(selected)
    assert selected == country, f"Expected {country} but found {selected}"

    # Colors
    color_selection = 'Green'
    result = auto1.colors(color_selection)
    assert color_selection in result

    # Date Selection
    auto1.date_picker()
