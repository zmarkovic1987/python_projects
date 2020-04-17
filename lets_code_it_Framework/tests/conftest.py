"""
py.test -s -v pytest_package\test_command_line_args.py --browser firefox
"""
from selenium import webdriver
from base.webdriver_factory import WebDriverFactory
import pytest

@pytest.fixture(scope='class')
def one_time_setUp(browser, request):
    print('Running One time Set Up')
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print('Running One time Teardown')

@pytest.fixture()
def setUp():
    print(' Once before every method')
    yield
    print(' Once after every method')


def pytest_addoption(parser):
    parser.addoption('--browser')
    # parser.addoption('--osType', help='Type of operating system')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


# @pytest.fixture(scope='session')
# def osType(request):
#     return request.config.getoption('--osType')