from selenium import webdriver
from base.webdriver_factory import WebDriverFactory
from pages.home.home_page import HomePage
import pytest


@pytest.yield_fixture(scope='class')
def one_time_setup(request, browser):
    print('Running one time setup')

    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    home = HomePage(driver)
    home.log_in()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print('Running One time Teardown')

# @pytest.yield_fixture()
# def method_set_up():
#     home = one_time_setup.home
#     home.go_to_homepage()
#     yield


# Define how to call browser type when playing test from console
def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.yield_fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
