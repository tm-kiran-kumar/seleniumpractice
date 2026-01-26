import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver(browser='chrome'):
    # Setup: Initialize the driver
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        page = webdriver.Chrome(options=options)
        #page.get('https://testautomationpractice.blogspot.com/')
        page.get('https://practicetestautomation.com/practice-test-login/')
        page.maximize_window()
    elif browser == 'safari':
        page = webdriver.Safari()
        page.maximize_window()
    else:
        return 'Invalid browser'
    yield page

    # Teardown: Closing the driver
    page.quit()

# To take automatic screenshots
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extra", [])
#
#     if report.when == "call" and report.failed:
#         # Get the driver from the test item
#         driver = item.funcargs.get('driver')
#         if driver:
#             screenshot = driver.get_screenshot_as_base64()
#             extras.append(pytest_html.extras.image(screenshot))
#     report.extra = extras
