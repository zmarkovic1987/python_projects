import unittest
from tests.sanity_test.sanity_test import SanityTest1
from tests.test_pdp.test_pdp import TestPDP

# Get all tests from test classes

test_case_1 = unittest.TestLoader().loadTestsFromTestCase(SanityTest1)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(TestPDP)

# Create Test suite
all_tests = unittest.TestSuite([test_case_1, test_case_2])
unittest.TextTestRunner(verbosity=2).run(all_tests)



