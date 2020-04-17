"""
You can Switch to Shadow DOM by JS
"""

from selenium import webdriver
import time


class Shadow():

    def test(self):
        base_url = 'https://eu.puma.com/de/en/pd/puma-x-sonic-leadcat-youth-sandals/372342.html?dwvar_372342_color=02'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        # This is the Way to manipulate Shadow DOM
        driver.execute_script("return document.querySelector('#puma-swatches-size').shadowRoot.querySelector('#swatch-0280')").click()

        time.sleep(3)


start = Shadow()
start.test()