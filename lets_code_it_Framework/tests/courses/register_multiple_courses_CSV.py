from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home_page.navigation_page import NavigationPage
from utilities.test_status import ErrorStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures('one_time_setUp', 'setUp')
@ddt
class TestRegisterCourseCSV(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setUp):
        self.register_courses_page = RegisterCoursesPage(self.driver)
        self.test_status = ErrorStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigate_to_home()

    @pytest.mark.run(order=1)
    @data(*get_csv_data("C:\\Users\\Zarko\\Documents\\python_projects\\python_projects\\lets_code_it_Framework\\test_data.csv"))
    @unpack
    def test_register_courses_error(self, course_name, cc_num, cc_exp, cc_cvv, postal):
        self.register_courses_page.test(course=course_name,
                                        cc_num=cc_num, exp_date=cc_exp, cvv=cc_cvv, postal=postal)
        time.sleep(1)

        result_1 = self.register_courses_page.verify_card_invalid()
        self.test_status.mark(result_1, "Verify invalid credit card Failed")

        result_2 = self.register_courses_page.verify_enrol_btn_disabled()
        self.test_status.mark_final("Verify state", result_2, "Verify enroll button disabled Failed")
        time.sleep(1)

        # self.driver.find_element_by_css_selector('img[alt="Let\'s Kode It"]').click()
        # self.driver.find_element_by_link_text('All Courses').click()
