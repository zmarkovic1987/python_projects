from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
import os


class SeleniumDriver():

    logger = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

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

        # Locate current directory
        current_directory = os.path.dirname(__file__)
        self.logger.info("################################### " + current_directory)

        destination_file = os.path.join(current_directory, relative_file_name)
        destination_dir = os.path.join(current_directory, sc_directory)

        try:
            if not os.path.exists(destination_dir):
                os.mkdir(destination_dir)
            self.driver.save_screenshot(destination_file)  # Selenium methhod
            self.logger.info("Screenshot " + file_name + " saved in the Directory: " + destination_dir)
        except:
            self.logger.error("Creating or saving Screenshot failed")

    def get_element(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:  # exists
                element = self.driver.find_element(locator_type, locator)
                self.logger.info('Element with locator: ' + locator + ' found')
        except:
            self.logger.info('Element with locator: ' + locator + ' NOT found')
        return element

    def get_elements(self, locator, locator_type=By.ID):
        element = None
        try:
            element = self.driver.find_elements(locator_type, locator)
            self.logger.info('Elements with' + locator_type + ', ' + locator + 'found')
        except:
            self.logger.info('Elements with locator: ' + locator_type + ', ' + locator + ' not found')
        return element

    def click_element(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.logger.info('Clicked on element with Locator: ' + locator)
        except:
            self.logger.info('Cant click on element with locator: ' + locator)

    def click_element_from_list_number(self, locator, locator_type=By.ID, place=0):
        try:
            elements = self.get_elements(locator, locator_type)
            element = elements[place]
            element.click()
            self.logger.info('Clicked on ' + str(place) + ' element from elements list with locator ' + locator)
        except:
            self.logger.info('Cant click on ' + str(place) + ' element from elements list with locator ' + locator)

    def get_element_from_list(self, locator, locator_type=By.ID, place=0):
        try:
            elements = self.get_elements(locator, locator_type)
            element = elements[place]
            self.logger.info('Found ' + str(place) + '. element from elements list with locator ' + locator)
            return element
        except:
            self.logger.error('Couldn\'t Find ' + str(place) + '. element from elements list with locator ' + locator)

    def hover_over(self, locator="", locator_type=By.ID, element=None):
        try:
            action = ActionChains(self.driver)
            if locator:
                element = self.get_element(locator, locator_type)
            action.move_to_element(element).perform()
            self.logger.info('Hovered over element with Locator ' + locator_type + ', ' + locator)
        except:
            self.logger.error('Failed to Hover')

        time.sleep(2)

    def hover_and_click(self, hover_locator, hover_locator_type, link_locator="", link_locator_type=By.ID, link_element=None):
        action = ActionChains(self.driver)
        self.hover_over(hover_locator, hover_locator_type)
        if link_locator:
            link_element = self.get_element(link_locator, link_locator_type)
        action.click(link_element).perform()
        self.logger.info('Hovered over element with Locator ' + hover_locator_type + ', ' + hover_locator +
                         '. And clicked on the element with Locator: ' + link_locator_type + ', ' + link_locator)

    def frame_switch(self, n=0):
        self.driver.switch_to.frame(n)

    def wait_for_element(self, locator, locator_type=By.ID, timeout=10):
        element = None
        try:
            # locator_type = self.get_by_type(locator_type)
            self.logger.info('Waiting maximum: ' + str(timeout) + 'seconds to be clickable')
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

            self.logger.info('Element with Locator -> ' + locator_type + ', ' + locator + '. Appeared on the webpage')
        except:
            self.logger.info('Element with Locator -> ' + locator_type + ', ' + locator +
                             '. NOT appeared on the webpage')
        return element

    def get_text_from_element(self, locator='', locator_type=By.ID, element=None):
        if locator:
            element = self.get_element(locator, locator_type)
        return element.text

    def select_from_menu(self, text, menu_locator, menu_locator_type=By.ID):
        menu = self.get_element(menu_locator, menu_locator_type)
        sel = Select(menu)
        sel.select_by_visible_text(text)

    def type_text(self, text, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(text)
            self.logger.info('Typing ' + text + ' in the element with Locator type and Locator: -> '
                             + locator_type + ' , ' + locator)
        except:
            self.logger.info('Cant type ' + text + ' in the element with Locator type and Locator: -> '
                             + locator_type + ' , ' + locator)

    def element_is_present(self, locator="", locator_type=By.ID, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.logger.info('Element with locator type and locator: ' + locator_type + locator + ' is Present')
                return True
            else:
                self.logger.info('Element with locator type and locator: ' + locator_type + locator + ' is NOT Present')
                return False
        except:
            self.logger.error('Is displayed Exception')

    def dropdown_select(self, menu_id, option_selector, by_type):
        """
        by_type can be - text, value or index
        :param menu_id:
        :param option_selector:
        :param by_type:
        :return:
        """
        try:
            dropdown = self.get_element(menu_id, By.ID)
            if dropdown is not None:
                sel = Select(dropdown)
                if by_type == 'text':
                    sel.select_by_visible_text(option_selector)
                    self.logger.info('Selected option By Text')
                elif by_type == 'value':
                    sel.select_by_value(option_selector)
                    self.logger.info('Selected option By Value')
                elif by_type == 'index':
                    sel.select_by_index(option_selector)
                    self.logger.info('Selected option By Index')
                else:
                    self.logger.error("Wrong by type")
            else:
                self.logger.error("Cant find Dropdown menu with ID: " + menu_id)
        except:
            self.logger.error("Dropdown Select ERROR")

    def confirm_alert(self):
        self.driver.switch_to.alert.accept()


    # NOT SURE IF THIS WORKS
    # def element_is_displayed(self, locator="", locator_type=By.ID, element=None):
    #     try:
    #         if locator:
    #             element = self.get_element(locator, locator_type)
    #         # result = element.is_displayed()
    #         if element is not None:
    #             result = element.is_displayed()
    #             if result is True:
    #                 self.logger.info('Element with locator type and locator: ' + locator_type + locator + ' is Displayed')
    #             else:
    #                 self.logger.error('Element with locator type and locator: ' + locator_type + locator + ' is NOT displayed')
    #             return result
    #         else:
    #             self.logger.error('Element with locator type and locator: ' + locator_type + locator + ' NOT Found')
    #     except:
    #         self.logger.error('Is displayed Exception')
