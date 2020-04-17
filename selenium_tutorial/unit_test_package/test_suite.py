import unittest
from test_case_demo import TestCaseDemo1
from test_case_demo_2 import TestCaseDemo2


# Get All Tests from Test Classes we imported
test_case_1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)


# Create a test suite combining imported Test Classes
test_suit_name = unittest.TestSuite([test_case_1, test_case_2])

unittest.TextTestRunner(verbosity=2).run(test_suit_name)
