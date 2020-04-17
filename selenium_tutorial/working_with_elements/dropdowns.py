from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():

    def test(self):

        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        cars_dropdown = driver.find_element_by_id('carselect')
        sel = Select(cars_dropdown)

        # Select benz by value
        sel.select_by_value('benz')
        time.sleep(2)
        # Check if correctly selected
        sel_value = driver.find_element_by_css_selector("option[value='benz']")
        is_selected = sel_value.is_selected()

        if is_selected is True:
            print('Benz selected successfully')
        else:
            print('Failed to select Benz')

        # Select Honda by index
        sel.select_by_index('2')
        time.sleep(2)

        sel_value = driver.find_element_by_css_selector("option[value='honda']")
        is_selected = sel_value.is_selected()

        if is_selected is True:
            print('Honda selected successfully')
        else:
            print('Failed to select Honda')

        # Select BMW by Visible Text
        sel.select_by_visible_text('BMW')
        time.sleep(2)
        # Check if correctly selected
        sel_value = driver.find_element_by_css_selector("option[value='bmw']")
        is_selected = sel_value.is_selected()

        if is_selected is True:
            print('BMW selected successfully')
        else:
            print('Failed to select BMW')

        # Select Honda by Index again
        sel.select_by_index(2)
        time.sleep(2)
        # Check if correctly selected
        sel_value = driver.find_element_by_css_selector("option[value='honda']")
        is_selected = sel_value.is_selected()

        if is_selected is True:
            print('Honda selected successfully')
        else:
            print('Failed to select Honda')

start = DropdownSelect()
start.test()