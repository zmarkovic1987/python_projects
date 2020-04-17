from selenium import webdriver
import time

class HiddenElements():

    def LetsKodeItTest(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        # Find the state of the text box
        text_box = driver.find_element_by_id('displayed-text')
        text_box_state = text_box.is_displayed()
        print('The text box is visible: ' + str(text_box_state))

        # Click the Hide Button
        hide_button = driver.find_element_by_id('hide-textbox')
        hide_button.click()
        time.sleep(2)

        # Find the state of Text box
        text_box = driver.find_element_by_id('displayed-text')
        text_box_state = text_box.is_displayed()
        print('The text box is visible: ' + str(text_box_state))
        if text_box_state is None:
            print(' Element doesnt exist')
        else:
            print(' Element exists but its not visible')

        # Click the SHow Button
        show_button = driver.find_element_by_id('show-textbox')
        show_button.click()
        time.sleep(2)

        # Find the state of Text box
        text_box = driver.find_element_by_id('displayed-text')
        text_box_state = text_box.is_displayed()
        print('The text box is visible: ' + str(text_box_state))

        # Close browser
        driver.quit()


start = HiddenElements()
start.LetsKodeItTest()