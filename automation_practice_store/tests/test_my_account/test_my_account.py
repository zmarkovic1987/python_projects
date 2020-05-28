"""
Log in
- click sign in
- type email and password
- submit
Add address
ADD TEST CASE TO DELETE ALL ADDRESSES IF THERE IS ANY - you can do this by checking presence of the Add first
    address button. If this button is visible click on it. If it is not : 1. go to my addresses
    2 delete all addresses. You already have method for cleaning addresses.
- click add mu first address
- fill the form
- submit
Reach My Addresses
- edit address
- delete address
My Orders
- click on some order reference and check if correct is expanded below the list
Wish list
- reach one PDP. Add item to wishlist
- close modal
- reach second PDP. Add item to wishlist
- close modal
- reach my account, reach my wishlist
- change qty of one product
- remove one product
- delete empty wish list
Sign out

"""
import unittest
import pytest
from pages.home.home_page import HomePage
from pages.my_account_page.my_account_page import MyAccount
from utilities.test_status import ErrorStatus


@pytest.mark.usefixtures('one_time_setup')
class TestMyAcc(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_setup):
        self.home = HomePage(self.driver)
        self.errors = ErrorStatus(self.driver)
        self.account = MyAccount(self.driver)

    # def test_my_addresses(self):
    #
    # # ADD FIRST ADDRESS
    #     self.account.add_address()
    #
    #     result = self.home.verify_no_addresses()
    #     if result is True:
    #         result = False
    #     else:
    #         result = True
    #     self.errors.mark(result, 'Checking if address is added')
    #
    # # UPDATE ADDRESS
    #     self.account.update_address()
    #
    #     result = self.account.verify_updated_state()
    #     self.errors.mark(result, 'Editing address')
    #
    # # DELETE ADDRESS
    #     self.home.address_delete()
    #
    #     result = self.home.verify_no_addresses()
    #     self.errors.mark_final('Addresses test', result, 'Deleting address')
    #
    # # LOGOUT
    #     self.home.log_out()
    #
    # def test_a_order_history(self):
    #     self.home.go_to_homepage()
    #     self.home.log_in()
    # # ORDER HISTORY
    #     self.account.go_to_history()
    #
    #     result = self.account.verify_checkout_btn()
    #     self.errors.mark_final('My account test', result, "My Order History")
    #
    #     self.home.log_out()

    def test_wishlist(self):
        self.home.log_in()
        self.home.go_to_homepage()

        self.home.adding_2_products_wishlist()
        self.account.test_wishlist()

        result_deleting_item = self.account.verify_item_delete()
        self.errors.mark(result_deleting_item, 'Deleting item')

        self.account.qty_manipulation()

        result_qty = self.account.verify_product_qty()
        self.errors.mark(result_qty, 'Qty manipulation inside wishlist')

        self.account.create_new_wishlist()

        result_new_wishlist = self.account.verify_new_wishlist()
        self.errors.mark(result_new_wishlist, 'Adding new wishlist')

        self.account.delete_wishlists()
        result_delete_wishlists = self.account.verify_wishlist_removed()
        self.errors.mark_final('Wish List tests', result_delete_wishlists, 'Deleting wishlists')



