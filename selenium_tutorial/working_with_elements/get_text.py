from selenium import webdriver
import time

class GetText():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        open_tab_element = driver.find_element_by_id('opentab')
        get_text = open_tab_element.text
        print('Text of the element is: ' + get_text)

        # Another way of finding text
        get_text2 = open_tab_element.get_attribute('innerText')
        print('Text of the element is: ' + get_text2)

        time.sleep(2)
        driver.quit()


start = GetText()
start.test()