
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import os
from traceback import print_stack
import utilities.custom_logger as cl
import logging
from selenium.webdriver import ActionChains


class SeleniumDriver():

    logger = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshots(self, result_message):
        """
        Takes a screenshot of current open web page
        :param result_message:
        :return:
        """

        # CREATE DIRECTORY AND FILE NAME
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        sc_directory = "../screenshots/"
        relative_file_name = sc_directory + file_name  # This gives us ../screenshots/34383234.png

        # FInd the File and current File Directory
        current_directory = os.path.dirname(__file__)

        destination_file = os.path.join(current_directory, relative_file_name)

        destination_dir = os.path.join(current_directory, sc_directory)

        # Check if Destination Directory exists
        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)        # if Destination folder doesnt exists. Create it
            self.driver.save_screenshot(destination_file)
            self.logger.info("Screenshot " + file_name + " saved in the Directory: " + destination_dir)
        except:
            self.logger.error("Creating or saving Screenshot failed")
            print_stack()

    def get_title(self):
        return self.driver.title


    # def get_by_type(self, locator_type):
    #     locator_type = locator_type.lower()
    #
    #     if locator_type == 'id':
    #         return By.ID
    #     elif locator_type == 'xpath':
    #         return By.XPATH
    #     elif locator_type == 'class':
    #         return By.CLASS_NAME
    #     elif locator_type == 'linktext':
    #         return By.LINK_TEXT
    #     elif locator_type == 'css':
    #         return By.CSS_SELECTOR
    #     elif locator_type == 'name':
    #         return By.NAME
    #     else:
    #         print("Locator type " + locator_type + " not correct/supported")

    def get_element(self, locator, locator_type=By.ID):
        element = None
        try:
            # locator_type = locator_type.lower()
            # byType = self.get_by_type(locator_type)
            element = self.driver.find_element(locator_type, locator)
            self.logger.info("Element Found with: " + locator + " and Locator type: " + locator_type)
        except:
            self.logger.info("Element NOT Found with: " + locator + " and Locator type: " + locator_type)
        return element

    def get_elements(self, locator, locator_type=By.CLASS_NAME):
        element_list = None
        try:
            element_list = self.driver.find_elements(locator_type, locator)
            if len(element_list) > 0:
                self.logger.info(
                    "Found List of elements with Locator: " + locator + " and Locator type: " + locator_type)
            else:
                self.logger.error("Cant find elements with Locator: " + locator + " and Locator type: " + locator_type)
        except:
            self.logger.error(
                'Exception: Cant find elements with Locator: ' + locator + " and Locator type: " + locator_type)
        return element_list

    def element_click(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.logger.info('Clicked on element with locator: ' + locator + 'locator Type : ' + locator_type)
        except:
            self.logger.info('Cant click on element with locator: ' + locator + 'locator Type : ' + locator_type)
            # print_stack()

    def sendKeys(self, data, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.logger.info('Sent data on element with locator: ' + locator + 'locator Type : ' + locator_type)
        except:
            self.logger.info('Cant send data on element with locator: ' + locator + 'locator Type : ' + locator_type)
            print_stack()

    def is_element_present(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.logger.info("Element with Locator: " + locator +
                                 " and Locator type: " + locator_type + "is present")
                return True
            else:
                self.logger.info("Element with Locator: " + locator +
                                 " and Locator type: " + locator_type + "is NOT present")
                return False
        except:
            self.logger.info("Element not found")
            return False

    # def is_element_displayed(self, locator="", locator_type=By.ID, element=None):
    #     displayed = False
    #     try:
    #         if locator:
    #             element = self.get_element(locator, locator_type)
    #         if element is not None:
    #             displayed = element.is_displayed()
    #             self.logger.info("Element with Locator: " + locator +
    #                              " and Locator type: " + locator_type + "is displayed")
    #         else:
    #             self.logger.error(
    #                 "Element with Locator: " + locator + " and Locator type: " + locator_type + "is NOT displayed")
    #         return displayed
    #     except:
    #         self.logger.error("Element not found")
    #         return False

    def isElementDisplayed(self, locator="", locator_type=By.ID, element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.logger.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.logger.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def wait_for_element(self, locator, locator_type=By.ID, timeout=10):
        element = None
        try:
            # locator_type = self.get_by_type(locator_type)
            self.logger.info('Waiting maximum: ' + str(timeout) + 'seconds to be clickable')
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

            self.logger.info('Element appeared on the webpage')
        except:
            self.logger.info('Element didn\'t appear on the webpage')
        return element

    def web_scroll_down(self, pixels):
        script = "window.scrollBy(0, {})".format(pixels)
        self.driver.execute_script(script)

    def scroll_to_element(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
            self.web_scroll_down(-150)
            self.logger.info("Scrolled to element with Locator: " + locator + "and Locator Type: " + locator_type)
            time.sleep(2)
        except:
            self.logger.error(
                "Failed to scroll to element with Locator: " + locator + "and Locator Type: " + locator_type)

    def switch_iframe_name(self, name):
        try:
            self.driver.switch_to.frame(name)
            self.logger.info("Switched to iFrame with name: " + name)
        except:
            self.logger.error("CANT switch to iFrame with name: " + name)

    def get_element_attribute(self, att, locator='', locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            attribute = element.get_attribute(att)
            return attribute
        except:
            self.logger.error('Couldnt get attribute')

