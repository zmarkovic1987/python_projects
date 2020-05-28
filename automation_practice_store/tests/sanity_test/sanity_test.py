"""
Open homepage
from manu navigation select category - from home page test
Add product from PLP - create plp page class
Reach PDP - click on color
increase qty and add product - from PDP class
Remove one item - create Checkout page class
change qty of one product
reach Checkout
Sign in
Add new address
pay with cc

"""
from pages.home.home_page import HomePage
from pages.pdp.pdp_page import PDP
from pages.plp.plp_page import ProductListingPage
from pages.checkout.checkout_page import CheckoutPage
from utilities.test_status import ErrorStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures('one_time_setup')
class SanityTest1(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.home_page = HomePage(self.driver)
        self.errors = ErrorStatus(self.driver)
        self.plp = ProductListingPage(self.driver)
        self.pdp = PDP(self.driver)
        self.checkout = CheckoutPage(self.driver)

    # @pytest.mark.run(order=1)
    def test_a_reach_woman_dresses(self):
        self.home_page.click_woman_dresses()
        time.sleep(1)

        result = self.home_page.verify_woman_dresses_title("Dresses - My Store")
        self.errors.mark_final("Reach woman dress", result, 'Reach woman dresses Failed - Title doesnt match')

    # @pytest.mark.run(order=2)
    def test_b_plp_actions(self):
        self.plp.plp_test_1(0)
        time.sleep(1)

        add_result = self.pdp.test_qty_of_items_added(1)
        self.errors.mark_final("Test items in cart", add_result, "Failed to add 1 item from PLP")

        self.plp.plp_test_2()

    # @pytest.mark.run(order=3)
    def test_c_pdp_actions(self):
        self.pdp.test_pdp1()
        self.pdp.continue_to_checkout()

        result = self.pdp.products_in_cart(3)
        self.errors.mark_final("Cart qty check", result, "Qty in cart is not correct")

    # @pytest.mark.run(order=4)
    def test_d_cart_actions(self):
        self.checkout.cart_actions(1, 0)

        result = self.pdp.products_in_cart(2)
        self.errors.mark_final("Cart qty check", result, "Qty in cart is not correct")

    # @pytest.mark.run(order=5)
    def test_e_login_actions(self):
        self.checkout.click_proceed_to_checkout()
        self.checkout.login('zmarkovic1987@gmail.com', '123')

        result = self.checkout.verify_invalid_login()
        self.errors.mark(result, 'Invalid Login Test')
        time.sleep(1)

        self.checkout.login('zmarkovic1987@gmail.com', 'Zarko321')

        result = self.checkout.verify_valid_login()
        self.errors.mark_final('Login Actions', result, 'Valid Login Test')

    # @pytest.mark.run(order=6)
    def test_f_address_actions(self):
        self.checkout.add_new_address_btn()
        self.checkout.address_handling(
            'Zarko', 'Test', '565 W Orchard st', 'Milwaukee', '53204', "Wisconsin", '2345678902')
        time.sleep(1)

        result = self.checkout.verify_address_submit_success()
        self.errors.mark(result, 'Adding Address')

        # select address from dropdown
        self.checkout.select_shipping_address_dropdown()

        self.checkout.add_billing_address()
        self.checkout.address_handling(
            'Zarko', 'Test', '123 Santa Monica Blvd', 'Santa Monica', '90401', 'California', '2349030994')

        result_billing = self.checkout.verify_address_submit_success()
        self.errors.mark_final('Handling SHipping and billing address', result_billing, 'Billing Address Add')

    # @pytest.mark.run(order=7)
    def test_g_carrier_actions(self):
        self.checkout.handling_4th_step()

        bank_present = self.checkout.verify_payment_method_wire()
        self.errors.mark(bank_present, "Bank Payment Method present")

        check_present = self.checkout.verify_payment_check()
        self.errors.mark_final('Payment methods present', check_present, 'Check Payment Method present')

    # @pytest.mark.run(order=8)
    def test_h_place_order(self):
        self.checkout.place_order_wire()

    # @pytest.mark.run(order=9)
    def test_i_remove_addresses(self):
        self.home_page.address_delete()

        result = self.home_page.verify_no_addresses()
        self.errors.mark(result, "Removing addresses")

        self.home_page.log_out()
        result_2 = self.home_page.verify_log_out()
        self.errors.mark_final('Teardown', result_2, 'Log out')
        time.sleep(1)
