from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByXpathCss():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        # find_by_xpath = driver.find_element_by_xpath('//*[@id="name"]')
        find_by_xpath = driver.find_element('xpath', '//*[@id="name"]')  # or like this
        # find_by_xpath = driver.find_element(By.XPATH, '//*[@id="name"]')   # or with import By

        if find_by_xpath is not None:
            print('We found element by Xpath')

        find_by_css = driver.find_element_by_css_selector('a.btn-style.class1.class2')
        # find_by_css = driver.find_element('css selector', '#displayed-text')  # or like this
        # find_by_css = driver.find_element(By.CSS_SELECTOR, '#displayed-text')   # or with import By

        if find_by_css is not None:
            print('We found element by Css Selector')


chrome_test = FindByXpathCss()
chrome_test.test()