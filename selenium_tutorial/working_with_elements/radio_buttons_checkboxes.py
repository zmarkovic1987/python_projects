from selenium import webdriver
import time

class RadioCheck():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        bmw_radio = driver.find_element_by_id('bmwradio')
        bmw_radio.click()
        time.sleep(2)

        benz_radio = driver.find_element_by_id('benzradio')
        benz_radio.click()
        time.sleep(2)

        bmw_check = driver.find_element_by_id('bmwcheck')
        bmw_check.click()
        time.sleep(2)

        benz_check = driver.find_element_by_id('benzcheck')
        benz_check.click()
        time.sleep(2)

        print('BMW radio buttons is selected: ' + str(bmw_radio.is_selected()))
        print('Benz radio buttons is selected: ' + str(benz_radio.is_selected()))
        print('BMW checkbox buttons is selected: ' + str(bmw_check.is_selected()))
        print('Benz checkbox buttons is selected: ' + str(benz_check.is_selected()))


start = RadioCheck()
start.test()


