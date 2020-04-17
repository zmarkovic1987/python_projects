"""
find a list of elements by tag name, class, name, text...
"""

from selenium import webdriver
# from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.get(base_url)

        # elements_by_class = driver.find_elements_by_class_name('inputs')
        elements_by_class = driver.find_elements('class name', 'inputs')  # or like this
        # elements_by_class = driver.find_elements(By.CLASS_NAME, 'inputs')  # or like this
        length1 = len(elements_by_class)

        if elements_by_class is not None:
            print('Size of a List is: ' + str(length1))

        elements_by_tag = driver.find_elements_by_tag_name('h1')
        # elements_by_tag = driver.find_elements('tag name', 'a')
        # elements_by_tag = driver.find_elements(By.TAG_NAME, 'a')
        length1 = len(elements_by_tag)

        if elements_by_tag is not None:
            print('Size of a List is: ' + str(length1))


execute = ListOfElements()
execute.test()
