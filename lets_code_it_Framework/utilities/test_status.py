from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl
import time


# Verifying if result of assertation from Test file is True or False
# Then storing results of fail/pass without stopping the test
# Then evaluating if all test passed we get PASS. And if one test Failed we get FAIL
class ErrorStatus(SeleniumDriver):

    # logger = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        super(ErrorStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result is True:
                    self.result_list.append("PASS")
                    self.logger.info("###VERIFICATION SUCCESSFUL " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.logger.error("VERIFICATION FAILED " + result_message)
                    self.screenshots(result_message)
            else:
                self.result_list.append("FAIL")
                self.logger.error("###VERIFICATION FAILED " + result_message)
                self.screenshots(result_message)
        except:
            self.result_list.append("FAIL")
            self.logger.error("### EXCEPTION OCCURRED")
            self.screenshots(result_message)

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.logger.error(test_name + " ### FAILED ONE OR MORE TEST CASES")
            self.result_list.clear()
            # This is if one Failed test in suite, mark as Failed
            # If you find one Fail, mark as False
            assert True == False
        else:
            self.logger.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True == True

