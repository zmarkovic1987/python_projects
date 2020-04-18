from selenium import webdriver
from pages.pdp.pdp_page import PDP
from utilities.test_status import ErrorStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures('one_time_setup')
class TestPDP(unittest.TestCase):

    # page_url = 'index.php?id_product=5&controller=product'

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.pdp_test = PDP(self.driver)
        self.error_status = ErrorStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_pdp(self):
        self.pdp_test.test_pdp1()
        time.sleep(2)

        result = self.pdp_test.test_qty_of_items_added(2)

        assert result is True


    @pytest.mark.run(order=2)
    def test_2(self):
        self.pdp_test.test_pdp2()
        time.sleep(2)

        result = self.pdp_test.test_qty_of_items_added(1)

        assert result is True

    @pytest.mark.run(order=3)
    def test_3(self):
        self.pdp_test.test_pdp_remove_item()
        time.sleep(2)

        title_result = self.pdp_test.verify_title_matches("Order + My Store")
        self.error_status.mark(title_result, " Verify the Title")

        result = self.pdp_test.products_in_cart(1)
        self.error_status.mark_final("Remove item Test", result, " Verify number of products in cart")

