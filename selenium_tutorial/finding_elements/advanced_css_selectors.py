"""
Css Wild Cards
You can Access element by any attribute inside - value, name, placeholder...
CSS Selector - input[placeholder="Enter Your Name"]
First the tag name (input), then attribute (placehlder), then value of attribute (Enter Your Name)
There are 3 more wildcards but it will not be used very often
^ -> Starting text - like first class name inside class attribute
$ -> Ending text - Like last class name inside class attribute - This can be used to check if some JS append class to element
* -> Text contained - Doesnt matter if it is on start, end or middle - This can be used for Dynamic IDs
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

class AdvancedCss():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        # find_by_css = driver.find_element_by_css_selector('a.btn-style.class1.class2')
        # find_by_css = driver.find_element('css selector', '#displayed-text')  # or like this
        # find_by_css = driver.find_element(By.CSS_SELECTOR, '#displayed-text')   # or with import By
        # find_by_css = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter Your Name"]')
        # find_by_css = driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Your"]')
        find_by_css = driver.find_element(By.CSS_SELECTOR, 'a[class*="class1"]')
        find_by_css = driver.find_element(By.CSS_SELECTOR, 'input[class*="displayed"]')

        if find_by_css is not None:
            print('We found element by Css Selector')


chrome_test = AdvancedCss()
chrome_test.test()