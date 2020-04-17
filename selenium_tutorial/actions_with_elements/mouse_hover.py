from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class MouseHover():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)
        action = ActionChains(driver)

        element = driver.find_element_by_id('mousehover')
        item_to_click = driver.find_element_by_xpath('//a[text()="Top"]')

        # Scroll Element into View
        driver.execute_script('arguments[0].scrollIntoView(true);', element)
        driver.execute_script('window.scrollBy(0, -150);')
        time.sleep(3)

        try:
            # Hover over element
            action.move_to_element(element).perform()
            print("Mouse hovered over element")
            time.sleep(3)

            # click on item
            action.move_to_element(item_to_click).click().perform()
            print('Clicked the item inside Hovered menu')
            time.sleep(3)
        except:
            print("Failed to Hover")


start = MouseHover()
start.test()