"""
file name should start with test
test method name should start with test

py.test test_mod.py  # Run all Tests in module
py.test somepath     # Run all Tests below some path
py.test test_mod.py::test_method  # Only run one test method from test module

-s  --> To print statements
-v  --> Verbose - To print informations
"""

import pytest


@pytest.yield_fixture()
def setUp():
    print(' Demo 2 - Once before every method')
    yield
    print(' Demo 2 - Once after every method')


def test_demo2_method_A(setUp):
    print('Demo 2 - Running Method A')

# IF You dont Apply fixture (setUp) it will not be ran
def test_demo2_method_B(setUp):
    print('Demo 2 - Running method B')


