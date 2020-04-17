from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndType():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        # Find xpath of element and Click on element
        login_link = driver.find_element(By.XPATH, "//div[contains(@class, 'course-block')]//parent::div//parent::div//preceding-sibling::header//*[@id='navbar']/div/div/div/ul/li[2]/a")
        login_link.click()

        time.sleep(3)
        email_input = driver.find_element(By.ID, 'user_email')
        email_input.send_keys('Test')

        password = driver.find_element_by_id('user_password')
        password.send_keys('123454321')

        email_input.clear()

        time.sleep(3)
        email_input.send_keys('Drugi test')
        time.sleep(3)

        driver.quit()


start = ClickAndType()
start.test()
