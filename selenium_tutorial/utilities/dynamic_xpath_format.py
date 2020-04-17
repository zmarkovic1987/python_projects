from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DynamicXpath():

    def Test(self):
        base_url = 'https://learn.letskodeit.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        login_button = driver.find_element(By.LINK_TEXT, 'Login')
        login_button.click()

        user_email = driver.find_element_by_id('user_email')
        user_email.send_keys('test@email.com')

        password = driver.find_element_by_id('user_password')
        password.send_keys('abcabc')

        submit_user_pass = driver.find_element(By.CSS_SELECTOR, "input[name='commit']")
        submit_user_pass.click()

        search_field = driver.find_element_by_id('search-courses')
        search_field.send_keys('JavaScript')

        submit_search = driver.find_element_by_id('search-course-button')
        submit_search.click()

        # Select Course
        # _course = "//div[contains(@class, 'course-listing-title')and contains(text(), 'JavaScript for beginners')]"
        _course = "//div[contains(@class, '{0}') and contains(text(), '{1}')]"
        _course_locator = _course.format('course-listing-title',
                                         'JavaScript for beginners')  # With this Line we replace {0} using element.format()

        course_element = driver.find_element_by_xpath(_course_locator)
        course_element.click()
        time.sleep(3)


start = DynamicXpath()
start.Test()
