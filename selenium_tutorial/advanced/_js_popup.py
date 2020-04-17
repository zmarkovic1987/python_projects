"""
You can Switch to iframe by name, id.. and numbers
switch_to.frame(0)
switch_to.frame(1)
"""

from selenium import webdriver
import time


class JSPopup():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        driver.find_element_by_id('name').send_keys('Alert')
        driver.find_element_by_id('alertbtn').click()
        time.sleep(3)

        # Alert Accept
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)

        # Confirm
        driver.find_element_by_id('name').send_keys('Confirm')
        driver.find_element_by_id('confirmbtn').click()
        time.sleep(3)

        alert2 = driver.switch_to.alert
        alert2.accept()

        # DISMISS
        # alert2.dismiss()
        time.sleep(3)


start = JSPopup()
start.test()