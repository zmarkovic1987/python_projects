from selenium import webdriver


class runFFtests():

    def testMethod(self):
        # Instantiate the FF Browser Command
        # driver = webdriver.Firefox(
        #     executable_path='C:\\Users\\Zarko\\Documents\\python_projects\\drivers\\geckodriver.exe')
        # Open the URL
        driver = webdriver.Firefox()

        driver.get('http://www.letskodeit.com')


ff = runFFtests()
ff.testMethod()
