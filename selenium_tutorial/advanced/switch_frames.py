"""
You can Switch to iframe by name, id.. and numbers
switch_to.frame(0)
switch_to.frame(1)
"""

from selenium import webdriver
import time


class SwitchFrame():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        frame_name = driver.find_element_by_id('courses-iframe')

        # Switch to iframe by id
        # driver.switch_to.frame(frame_name)
        
        # Switch to iframe by numbers
        driver.switch_to.frame(0)

        driver.find_element_by_id('search-courses').send_keys('Python')
        time.sleep(3)

        # Return to Parent frame
        driver.switch_to.default_content()

        element = driver.find_element_by_id('name')
        driver.execute_script('arguments[0].scrollIntoView(true);', element)
        time.sleep(0.5)
        driver.execute_script('window.scrollBy(0, -150);')
        time.sleep(2)

        element.send_keys('Python')
        time.sleep(3)


start = SwitchFrame()
start.test()