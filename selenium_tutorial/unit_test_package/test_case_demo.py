"""

"""

import unittest
import unit_test_package.assert_demo


class TestCaseDemo1(unittest.TestCase):

    # SetUp Class will run once at the start of the test suite, before all tests run
    @classmethod
    def setUpClass(cls) -> None:
        print('*#' * 30)
        print('Class 1 -> I will run once before all tests')
        print('*#' * 30)

    # SetUp will run before every test
    def setUp(self) -> None:
        print('Class 1 -> I will run once before every test')

    def test_method_A(self):
        print('Class 1 -> Running method A')

    def test_method_B(self):
        print('Class 1 -> Running method B')

    # tearDown will run after every test
    def tearDown(self) -> None:
        print('Class 1 -> I will run after every test')

    # tearDown class will run only once at the end of test suite, after all test run
    @classmethod
    def tearDownClass(cls) -> None:
        print('*#' * 30)
        print('Class 1 -> I will run only once after all test finished')
        print('*#' * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)