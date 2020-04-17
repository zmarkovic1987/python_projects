from selenium import webdriver
from base.webdriver_factory import WebDriverFactory
import pytest

@pytest.fixture(scope='class')
def one_time_setup(browser, request):
    print('Running one time setup')

    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print('Running One time Teardown')

# Define how to call browser type when playing test from console
def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
