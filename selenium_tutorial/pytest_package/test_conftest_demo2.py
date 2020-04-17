import pytest


def test_demo2_method_A(one_time_setUp, setUp):
    print('Demo 2 - Running Method A')

# IF You dont Apply fixture (setUp) it will not be ran
def test_demo2_method_B(one_time_setUp, setUp):
    print('Demo 2 - Running method B')

