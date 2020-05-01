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
        self.browser = browser

    def get_webdriver_instance(self):
        """
        Get Webdriver Instance based on browser
        :return:
        """

        # base_url = 'http://automationpractice.com/index.php?id_product=5&controller=product'
        base_url = 'http://automationpractice.com/'

        if self.browser == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser == 'edge':
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(7)
        driver.maximize_window()
        driver.get(base_url)

        return driver
