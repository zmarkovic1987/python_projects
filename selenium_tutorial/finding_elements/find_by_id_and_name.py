from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        # find_by_id = driver.find_element_by_id('name')
        # find_by_id = driver.find_element('id', 'name')  # or like this
        find_by_id = driver.find_element(By.ID, 'name')  # Or with Import By

        if find_by_id is not None:
            print('We found element by ID')

        # find_by_name = driver.find_element_by_name('enter-name')
        # find_by_name = driver.find_element('name', 'enter-name') # or like this
        find_by_name = driver.find_element(By.NAME, 'enter-name')  # Or with Import By

        if find_by_name is not None:
            print('We found element by name')


chrome_test = FindByIdName()
chrome_test.test()