from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from wait_types.explicit_wait_framework import ExplicitWaitType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitUsingFramwork():

    def test(self):
        base_url = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(0.5)
        wait = ExplicitWaitType(driver)
        driver.get(base_url)

        driver.find_element_by_id('tab-flight-tab-hp').click()

        # city_from = wait.wait_for_element('flight-origin-hp-flight', By.ID)
        wait.wait_for_element('flight-origin-hp-flight', By.ID).send_keys('SFO')
        # city_from = wait.until(EC.element_to_be_clickable((By.ID, 'flight-origin-hp-flight')))
        # city_from.send_keys('SFO')

        driver.find_element_by_id('flight-destination-hp-flight').send_keys('NYC')
        driver.find_element_by_id('flight-departing-hp-flight').click()

        month_name = ''

        while month_name != 'Jun 2020':
            month_name = driver.find_element_by_xpath(
                '//*[@id="flight-departing-wrapper-hp-flight"]/div/div[2]/div[3]/table/caption').text
            print(month_name)
            if month_name == 'Jun 2020':
                departing_month = driver.find_element_by_xpath(
                    '//div[@id="flight-departing-wrapper-hp-flight"]//button[contains(@data-month, "5") and contains(@data-day,"12")]')
                departing_month.click()
                break
            else:
                driver.find_element_by_css_selector('button.next').click()

        driver.find_element_by_id('flight-returning-hp-flight').click()

        arrival_month_name = ''
        while arrival_month_name != 'Jun 2020':
            arrival_month_name = driver.find_element_by_xpath(
                '//*[@id="flight-returning-wrapper-hp-flight"]/div/div[2]/div[3]/table/caption').text
            driver.find_element_by_css_selector('button.next').click()
            print(arrival_month_name)
            if arrival_month_name == 'Jun 2020':
                time.sleep(1)
                departing_month = driver.find_element_by_xpath('//div[@id="flight-returning-wrapper-hp-flight'
                                                               '"]//button[contains(@data-month, "5") and contains('
                                                               '@data-day,"18")]')
                departing_month.click()
                break
            # else:
            #     driver.find_element_by_css_selector('button.next').click()

        driver.find_element_by_xpath('//div[@id="f-fh-msg-tooltip-hp-flight"]/preceding-sibling::label/button').click()

        filter_stop = wait.wait_for_element("//input[@id='stopFilter_stops-1']", By.XPATH)
        filter_stop.click()

        time.sleep(3)
        driver.quit()


start = ExplicitWaitUsingFramwork()
start.test()
