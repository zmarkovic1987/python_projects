from base.selenium_driver import SeleniumDriver



class ErrorStatus(SeleniumDriver):

    def __init__(self, driver):
        super(ErrorStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result is True:
                    self.result_list.append('PASS')
                    self.logger.info('### VERIFICATION SUCCESSFUL ' + result_message)
                else:
                    self.result_list.append('FAIL')
                    self.logger.error('### VERIFICATION FAILED ' + result_message)
                    self.screenshots(result_message)
            else:
                self.result_list.append('FAIL')
                self.logger.error('### VERIFICATION FAILED / No result ' + result_message)
                self.screenshots(result_message)
        except:
            self.result_list.append('FAIL')
            self.logger.error('### SOMETHING IS GONE WRONG> Couldnt get result ' + result_message)
            self.screenshots(result_message)

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.logger.error("Test name: " + test_name + " FAILED ONE OR MORE TEST CASES")
            self.result_list.clear()
            # this means if Fail found (true) present it as False
            assert True == False
        else:
            self.logger.info("Test name: " + test_name + " PASSED ALL TEST CASES")
            self.result_list.clear()
            assert True == True

