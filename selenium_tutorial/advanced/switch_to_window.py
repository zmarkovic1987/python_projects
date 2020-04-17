from selenium import webdriver
import time


class SwitchToWindow():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        # Find Parent Window
        parent_window = driver.current_window_handle
        print('Parent Window: ' + str(parent_window))

        # Click button to open new window
        driver.find_element_by_id('openwindow').click()
        time.sleep(3)

        # Find all windows
        all_windows = driver.window_handles

        # Switch to Window
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print('Switched to Window: ' + str(window))
                search_box = driver.find_element_by_id('search-courses')
                search_box.send_keys('Test123')
                time.sleep(3)
                driver.close()  # Closes just current window
                break

        # Switch back
        driver.switch_to.window(parent_window)
        driver.find_element_by_id('name').send_keys('Succesfully returned to Parrent Window')
        time.sleep(3)


start = SwitchToWindow()
start.test()