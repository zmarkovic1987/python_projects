"""
py.test -s -v pytest_package\test_command_line_args.py --browser firefox
"""

import pytest


@pytest.fixture()
def setUp():
    print(' Once before every method')
    yield
    print(' Once after every method')


@pytest.fixture(scope='class')
def one_time_setUp(browser, request, osType):
    print('Running One time Set Up')
    if browser == 'firefox':
        value = 10
        print('Running tests on Firefox')
    else:
        value = 20
        print('Running Tests on Chrome')

    if request.cls is not None:
        request.cls.value = value

    yield value
    print('Running One time Teardown')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='Type of operating system')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')