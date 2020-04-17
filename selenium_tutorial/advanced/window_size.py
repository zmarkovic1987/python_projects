from selenium import webdriver
import time


class WindowSize():

    def test(self):
        base_url = 'https://learn.letskodeit.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        # JavaScript
        height = driver.execute_script('return window.innerHeight;')
        width = driver.execute_script('return window.innerWidth;')

        print('Height: ' + str(height))
        print('With: ' + str(width))

        # The Way to set screen size with Python
        driver.set_window_size(800, 600)

        time.sleep(4)

        # python way
        p_height = driver.get_window_size()

        print('Size of the Window using python method is :' + str(p_height))

        driver.quit()


start = WindowSize()
start.test()