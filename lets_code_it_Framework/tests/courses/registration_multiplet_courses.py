from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import ErrorStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack


@pytest.mark.usefixtures('one_time_setUp')
@ddt
class TestRegisterMultipleCourses(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setUp):
        self.register_courses_page = RegisterCoursesPage(self.driver)
        self.test_status = ErrorStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript", "1111 5678 9098 7654", "1020", '111', '11000'),
          ("Python", "2222 5678 9098 7654", "1020", '222', '22000'))
    @unpack
    def test_register_courses_error(self, course_name, cc_num, cc_exp, cc_cvv, postal):
        self.register_courses_page.test(course=course_name,
                                        cc_num=cc_num, exp_date=cc_exp, cvv=cc_cvv, postal=postal)
        time.sleep(1)

        result_1 = self.register_courses_page.verify_card_invalid()
        self.test_status.mark(result_1, "Verify invalid credict card Failed")

        result_2 = self.register_courses_page.verify_enrol_btn_disabled()
        self.test_status.mark_final("Verify state", result_2, "Verify enroll button disabled Failed")
        time.sleep(1)

        self.driver.find_element_by_css_selector('img[alt="Let\'s Kode It"]').click()
        self.driver.find_element_by_link_text('All Courses').click()
