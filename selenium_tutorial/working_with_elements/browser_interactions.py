from selenium import webdriver


class BrowserInteractions():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()

        # Maximize window
        driver.maximize_window()

        # Open URL
        driver.get(base_url)

        # Get Title
        title = driver.title
        print('The Title of the Web Page is: ' + title)

        # Get Current URL
        current_url = driver.current_url
        print('The Current URL is: ' + current_url)

        # Browser Refresh
        driver.refresh()
        print('Browser refreshed')

        #Open another Url
        driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')

        current_url = driver.current_url
        print('The Current URL is: ' + current_url)

        # Go back one page
        driver.back()

        current_url = driver.current_url
        print('The Current URL is: ' + current_url)

        if current_url == base_url:
            print('Went Back one page')

        # Go Forward one page
        driver.forward()

        current_url = driver.current_url
        if current_url == 'https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1':
            print('Wehn forward one page')

        # Close Browser
        driver.quit()


start = BrowserInteractions()
start.test()
