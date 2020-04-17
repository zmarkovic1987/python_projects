from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, locator_type, timeout=10):
        element = None
        try:
            print('Waiting maximum: ' + str(timeout) + 'seconds to be clickable')
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

            print('Element appeared on the webpage')
        except:
            print('Element didnt appeared on the webpage')
        return element
