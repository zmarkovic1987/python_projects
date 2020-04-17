from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class DragAndDrop():

    def test(self):
        base_url = 'https://jqueryui.com/droppable/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)
        action = ActionChains(driver)

        driver.switch_to.frame(0)

        drag_element = driver.find_element_by_id('draggable')
        drop_to = driver.find_element_by_id('droppable')
        time.sleep(2)

        # Drag and Drop Command
        # action.drag_and_drop(drag_element, drop_to).perform()
        # time.sleep(3)

        # Chaining Actions - another way to drag and drop
        action.click_and_hold(drag_element).move_to_element(drop_to).release().perform()
        time.sleep(2)


start = DragAndDrop()
start.test()