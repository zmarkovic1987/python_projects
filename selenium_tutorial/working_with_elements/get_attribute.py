"""
Mathod for finding attribute value is:
element.get_attribute('placeholder/value/class...')
"""

from selenium import webdriver
import time

class GetValue():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        open_tab_element = driver.find_element_by_id('name')

        get_attribute = open_tab_element.get_attribute('placeholder')

        print('Text of the element is: ' + get_attribute)
        time.sleep(1)
        driver.quit()


start = GetValue()
start.test()