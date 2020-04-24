from base.base_page import BasePage
from selenium.webdriver.common.by import By


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _home_icon = 'img[alt="Let\'s Kode It"]'
    _my_courses = 'My Courses'
    _all_courses = 'All Courses'
    _practice = 'Practice'
    _user_settings = '//img[@alt="test@email.com"]'

    def navigate_to_home(self):
        self.element_click(self._home_icon, By.CSS_SELECTOR)

    def navigate_to_my_courses(self):
        self.element_click(self._my_courses, By.LINK_TEXT)

    def navigate_to_all_courses(self):
        self.element_click(self._all_courses, By.LINK_TEXT)

    def navigate_to_practice(self):
        self.element_click(self._practice, By.LINK_TEXT)

    def navigate_to_settings(self):
        self.element_click(self._user_settings, By.XPATH)

