from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging


class SeleniumDriver():

    logger = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_element(self, locator, locator_type=By.ID):
        element = None
        try:
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

    def click_element(self, locator, locator_type=By.ID):
        try:
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

    def hover_over(self, locator, locator_type=By.ID):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_element(locator, locator_type)).perform()
        self.logger.info('Hovered over element with Locator ' + locator_type + ', ' + locator )

        time.sleep(2)

    def hover_and_click(self, hover_locator, hover_locator_type, link_locator, link_locator_type):
        action = ActionChains(self.driver)
        self.hover_over(hover_locator, hover_locator_type)
        element = self.get_element(link_locator, link_locator_type)
        action.click(element).perform()
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

    def get_text_from_element(self, locator, locator_type=By.ID):
        return self.get_element(locator, locator_type).text

    def select_from_menu(self, text, menu_locator, menu_locator_type=By.ID):
        menu = self.get_element(menu_locator, menu_locator_type)
        sel = Select(menu)
        sel.select_by_visible_text(text)

    def type_text(self, text, locator, locator_type=By.ID):
        try:
            self.get_element(locator, locator_type).clear()
            self.get_element(locator, locator_type).send_keys(text)
            self.logger.info('Typing ' + text + ' in the element with Locator type and Locator: -> '
                             + locator_type + ' , ' + locator)
        except:
            self.logger.info('Cant type ' + text + ' in the element with Locator type and Locator: -> '
                             + locator_type + ' , ' + locator)
