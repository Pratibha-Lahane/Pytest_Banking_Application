import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "Chrome":
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()

    elif browser == "Firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()

    elif browser == "Edge":
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()

    else:
        print("Test Run - headless Browser")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://bankapp.credence.in/")
    yield driver
    driver.quit()


# bellow code for single browser
# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://bankapp.credence.in/")
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()
#
@pytest.fixture(params=[
    ("Admin.cred.in", "Admin@123", "LoginPass"),
    ("admin.cred.in", "admin@123", "LoginPass"),
    ('Admin.cred.in', 'admin@123', 'LoginFail'),
    ('admin.cred.in', "Admin@123", "LoginFail")
])
def getDataForLogin(request):
    return request.param
