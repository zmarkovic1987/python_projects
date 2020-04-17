from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class Slider():

    def test(self):
        base_url = 'https://jqueryui.com/slider/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)
        action = ActionChains(driver)

        driver.switch_to.frame(0)
        slider_element = driver.find_element_by_xpath("//div[@id='slider']/span")

        # By Chaining Actions
        action.click_and_hold(slider_element).move_by_offset(50, 0).release().perform()
        time.sleep(2)

        # With Drag and Drop
        action.drag_and_drop_by_offset(slider_element, 200, 0).perform()
        time.sleep(2)


start = Slider()
start.test()