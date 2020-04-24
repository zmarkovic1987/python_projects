from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import ErrorStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures('one_time_setUp')
class TestRegisterCourse(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setUp):
        self.register_courses_page = RegisterCoursesPage(self.driver)
        self.test_status = ErrorStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_register_courses_error(self):
        self.register_courses_page.test(course="JavaScript",
                                        cc_num='1234 5678 9098 7654', exp_date='1020', cvv='737', postal='11000')
        time.sleep(2)

        result_1 = self.register_courses_page.verify_card_invalid()
        self.test_status.mark(result_1, "Verify invalid credict card Failed")

        result_2 = self.register_courses_page.verify_enrol_btn_disabled()
        self.test_status.mark_final("Verify state", result_2, "Verify enroll button disabled Failed")
        time.sleep(2)





