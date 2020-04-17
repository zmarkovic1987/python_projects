from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HandyWrapper():

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()

        if locator_type == 'id':
            return By.ID
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'class':
            return  By.CLASS_NAME
        elif locator_type == 'linktext':
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type + " not correct/supported")

    def get_element(self, locator, locator_type='id'):
        try:
            element_list = self.driver.find_elements(locator_type, locator)
            if len(element_list) > 0:
                print('Element found')
                return True
            else:
                print('Element not found')
                return False
        except:
            print('Element not found')
            return False

    # def get_element(self, locator, locator_type='id'):
    #     element = None
    #     try:
    #         locator_type = locator_type.lower()
    #         by_type = self.get_by_type(locator_type)
    #         element = self.driver.find_element(by_type, locator)
    #         print('Element found')
    #     except:
    #         print('Element not found')
    #     return element


