import pytest
from pytest_package.class_to_test import SomeClassToTest


@pytest.mark.usefixtures('one_time_setUp', 'setUp')
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.abc = SomeClassToTest(10)

    def test_method_A(self):
        result = self.abc.sum_numbers(2, 7)
        assert result == 35
        print('Running method A')

    def test_method_B(self):
        print('Running method B')

