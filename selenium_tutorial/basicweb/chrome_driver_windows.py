from selenium import webdriver


class ChromeDriverWindows():

    def test(self):
        # driver = webdriver.Chrome(executable_path='C:\\Users\\Zarko\\Documents\\python_projects\\drivers'
        #                                           '\\chromedriver.exe')
        driver = webdriver.Chrome()
        driver.get('http://www.letskodeit.com')


cc = ChromeDriverWindows()
cc.test()
