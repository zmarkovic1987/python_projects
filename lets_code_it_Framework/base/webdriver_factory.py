"""
WebDriver Factory class implementation
It chreates a Webdriver instance based on browser configurations

Example:
        wdf = WebDriverFactory(browser)
        wdf.get_webdriver_instance()
"""

from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriveFactory class
        :param browser:
        """
        self.browser = browser

    def get_webdriver_instance(self):
        """
        Get Web Driver Instance based on the browser configuration
        :return: driver
        """
        base_url = 'https://learn.letskodeit.com/'
        if self.browser == 'edge':
            driver = webdriver.Edge()
        elif self.browser == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.maximize_window()

        driver.get(base_url)

        return driver



