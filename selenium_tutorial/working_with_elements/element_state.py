"""
Disabled elements can't be manipulated
"""

from selenium import webdriver

class ElementState():

    def isEnabled(self):
        base_url = 'https://www.google.com'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        e1 = driver.find_element_by_css_selector('input[name="q"]')
        e1_state = e1.is_enabled()
        print('E1 is enabled? -> ' + str(e1_state))
        e1.send_keys('123')

        e2 = driver.find_element_by_css_selector('input[name="iflsig"]')
        e2_state = e2.is_enabled()
        print('E2 is enabled? -> ' + str(e2_state))

        driver.quit()


start = ElementState()
start.isEnabled()