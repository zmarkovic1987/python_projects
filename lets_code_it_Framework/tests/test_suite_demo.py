import unittest
from tests.home_page.login_test import LoginTest
from tests.courses.register_multiple_courses_CSV import TestRegisterCourseCSV

# Get All test from test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestRegisterCourseCSV)

# Create test suite combining all test classes
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
