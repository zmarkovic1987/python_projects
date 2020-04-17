from selenium import webdriver
import time


class Scroll():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        driver.execute_script('window.scrollBy(0, 1000);')
        time.sleep(3)

        driver.execute_script('window.scrollBy(0, -1000);')
        time.sleep(3)

        # Scroll Element into View
        element = driver.find_element_by_id('mousehover')
        driver.execute_script('arguments[0].scrollIntoView(true);', element)
        time.sleep(3)
        driver.execute_script('window.scrollBy(0, -150);')
        time.sleep(3)

        driver.execute_script('window.scrollBy(0, -1000);')
        time.sleep(3)

        # Native Way to Scroll into View
        location = element.location_once_scrolled_into_view
        print('Location: ' + str(location))
        time.sleep(3)


start = Scroll()
start.test()