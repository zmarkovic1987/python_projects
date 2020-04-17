from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWait():

    def test(self):
        base_url = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(0.5)
        driver.get(base_url)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                 ElementNotSelectableException])

        driver.find_element_by_id('tab-flight-tab-hp').click()

        city_from = wait.until(EC.element_to_be_clickable((By.ID, 'flight-origin-hp-flight')))
        city_from.send_keys('SFO')

        driver.find_element_by_id('flight-destination-hp-flight').send_keys('NYC')
        driver.find_element_by_id('flight-departing-hp-flight').click()
        driver.find_element_by_xpath('//div[@id="flight-departing-wrapper-hp-flight"]//button[contains(@data-month, "3") and contains(@data-day,"12")]').click()
        driver.find_element_by_id('flight-returning-hp-flight').click()
        driver.find_element_by_xpath('//div[@id="flight-returning-wrapper-hp-flight"]//button[contains(@data-month, "3") and contains(@data-day,"15")]').click()
        driver.find_element_by_xpath('//div[@id="f-fh-msg-tooltip-hp-flight"]/preceding-sibling::label/button').click()

        stop_filter = wait.until(EC.element_to_be_clickable((By.ID, 'stopFilter_stops-1')))
        stop_filter.click()

        time.sleep(3)
        driver.quit()


start = ExplicitWait()
start.test()

