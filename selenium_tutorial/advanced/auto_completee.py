from selenium import webdriver
import time


class AutoComplete():

    def test(self):
        base_url = 'http://www.southwest.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        city_field = driver.find_element_by_id('LandingAirBookingSearchForm_originationAirportCode')
        city_field.send_keys('New York')

        time.sleep(3)
        newark = driver.find_element_by_xpath("//ul[@id='LandingAirBookingSearchForm_originationAirportCode--menu']//button[contains(@aria-label, 'LGA')]")
        newark.click()

        time.sleep(3)
        driver.quit()


start = AutoComplete()
start.test()


