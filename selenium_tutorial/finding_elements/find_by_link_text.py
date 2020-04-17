from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByLinkText():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        # find_by_link_text = driver.find_element_by_link_text('Login')
        find_by_link_text = driver.find_element('link text', 'Login')  # or like this
        # find_by_link_text = driver.find_element(By.LINK_TEXT, 'Login')  # or with import By

        if find_by_link_text is not None:
            print('We found element by Link Text')

        # find_by_partial_link_text = driver.find_element_by_partial_link_text('Log')
        # find_by_partial_link_text = driver.find_element('partial link text', 'Log')  # or like this
        find_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, 'Log')  # or with import By

        if find_by_partial_link_text is not None:
            print('We found element by Partial Link Text')


chrome_test = FindByLinkText()
chrome_test.test()
