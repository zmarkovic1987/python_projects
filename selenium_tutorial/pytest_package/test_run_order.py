"""
First Install Ordering -> pip3 install pytest-ordering
set @pytest.mark.run(order=1)  # order number
"""

import pytest

@pytest.mark.run(order=2)
def test_run_A():
    print('Running Method A')

@pytest.mark.run(order=4)
def test_run_B():
    print('Running Method B')

@pytest.mark.run(order=1)
def test_run_C():
    print('Running Method C')

@pytest.mark.run(order=3)
def test_run_D():
    print('Running Method D')

@pytest.mark.run(order=5)
def test_run_E():
    print('Running Method E')

@pytest.mark.run(order=6)
def test_run_F():
    print('Running Method F')

