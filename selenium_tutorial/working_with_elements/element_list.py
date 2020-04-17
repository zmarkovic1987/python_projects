from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementLists():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        radio_button_list = driver.find_elements(By.XPATH, '//input[contains(@type, "radio") and contains(@name, "cars")]')
        size = len(radio_button_list)
        print('The numer of radio buttons is: ' + str(size))

        num = 0

        for r in radio_button_list:
            r.click()
            time.sleep(2)
            if r.is_selected() == True:
                num += 1
                print('Successfully selected radio button number: ' + str(num))
            else:
                num += 1
                print('Failed to select radio button number: ' + str(num))

        driver.quit()


start = ElementLists()
start.test()