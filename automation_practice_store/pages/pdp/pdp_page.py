from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import utilities.custom_logger as cl
import logging


class PDP(BasePage):

    # logger = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _qty_add = 'icon-plus'
    _quantity_wanted = 'quantity_wanted'
    _size_menu = 'group_1'  #ID
    _first_size = 'M'
    _actual_size = 'div#uniform-group_1 > span'  #css
    _size_m = "//option[@title='M']"
    _size_s = "//option[@title='S']"
    _add_to_cart_btn = "//button[@name='Submit']"
    _continue_shopping = '//span[@title="Continue shopping"]'
    _color_black = '//a[@title="Black"]'
    # _color_black_li = _color_black + '//parent::li'
    _color_black_li = '//a[@title="Black"]//parent::li'
    _cart_qty = 'layer_cart_product_quantity'
    _mini_cart = '//div[@class="shopping_cart"]/a'
    _remove_first_item_minicart = "//dt[@class='first_item']//a[@class='ajax_cart_block_remove_link']"
    # _items_in_cart = "ajax_cart_block_remove_link"  # class
    _items_in_cart = "cart-images"  # class
    _qty_of_items_added = "layer_cart_product_quantity"


    # Actions
    def click_on_add_qty(self):
        self.click_element(self._qty_add, By.CLASS_NAME)
        qty_check = self.get_element(self._quantity_wanted).get_attribute('value')
        self.logger.info('Qty is: ' + qty_check)
        time.sleep(2)
        # if qty_check == '2':
        #     self.logger.info('Qty is: ' + str(qty_check))
        # else:
        #     self.logger.info('Wanted Qty is 2 but we got ' + str(qty_check))

    def select_size_and_check(self):
        actual_size = self.get_text_from_element(self._actual_size, By.CSS_SELECTOR)
        if actual_size != 'M':
            self.select_from_menu(self._first_size, self._size_menu, By.ID)
            # m = self.get_element(self._size_m, By.XPATH)
            # is_selected = m.is_selected()
            # if is_selected is True:
            #     self.logger.info('Selected size M')
            # else:
            #     self.logger.info('Cant select M')
        else:
            self.select_from_menu(self._first_size, self._size_menu, By.ID)
            # s = self.get_element(self._size_s, By.XPATH)
            # is_selected = s.is_selected()
            # if is_selected is True:
            #     self.logger.info('Selected size S')
            # else:
            #     self.logger.info('Cant select S')

    def add_to_cart_click(self):
        self.click_element(self._add_to_cart_btn, By.XPATH)
        time.sleep(2)

    def close_cart_popup(self):
        self.click_element(self._continue_shopping, By.XPATH)
        time.sleep(2)

    def color_black_click(self):
        self.wait_for_element(self._color_black, By.XPATH)
        self.click_element(self._color_black, By.XPATH)
        time.sleep(2)
        # # element = self.get_element(self._color_black_li, By.XPATH)
        # element_class = self.get_element(self._color_black_li, By.XPATH).get_attribute('class')
        # if element_class == 'selected':
        #     self.logger.info('Black dress Selected')
        # else:
        #     self.logger.info('Fail to select Black color')

    def type_qty_field(self):
        self.type_text('1', self._quantity_wanted)
        time.sleep(2)

    def cart_qty_check(self):
        element = self.get_element(self._cart_qty).text
        self.logger.info(element)
        # if element == '1':
        #     self.logger.info('Qty Correct')
        # else:
        #     self.logger.info('Qty not correct')

    def remove_item_minicart(self):
        self.hover_and_click(self._mini_cart, By.XPATH, self._remove_first_item_minicart, By.XPATH)
        time.sleep(2)
        # self.hover_over(self._mini_cart, By.CLASS_NAME)
        # elements = self.get_elements(self._items_in_cart, By.CLASS_NAME)
        # self.logger.info(str(len(elements)))
        # if len(elements) < 2:
        #     self.logger.info('First element removed from Cart')
        # else:
        #     self.logger.info('Failed to remove item from cart')

    def go_to_cart(self):
        self.click_element('//div[@class="shopping_cart"]/a/b', By.XPATH)


    def test_pdp1(self):
        self.click_on_add_qty()
        self.select_size_and_check()
        self.add_to_cart_click()

    def test_pdp2(self):
        self.close_cart_popup()
        self.color_black_click()
        self.type_qty_field()
        self.add_to_cart_click()
        self.cart_qty_check()

    def test_pdp_remove_item(self):
        self.close_cart_popup()
        self.remove_item_minicart()
        self.go_to_cart()

    def test_qty_of_items_added(self, num_qty):
        actual = self.get_text_from_element(self._qty_of_items_added, By.ID)
        # self.logger.info("####################    " + actual)
        # self.logger.info("####################    " + str(num_qty))
        result = actual == str(num_qty)
        return result

    def products_in_cart(self, num_item):
        time.sleep(5)
        items_in_cart = self.get_text_from_element('summary_products_quantity')
        self.logger.info(items_in_cart)

        num_item_strip = None
        if num_item == 1:
            num_item_strip = '1 Product'
        elif num_item == 2:
            num_item_strip = '2 Products'
        elif num_item == 3:
            num_item_strip = '3 Products'
        # return num_item_strip

        self.logger.info(num_item_strip)
        result = items_in_cart == num_item_strip
        return result

    def verify_title_matches(self, title_to_match):
        self.logger.info(title_to_match)
        self.logger.info(self.get_title())

        if title_to_match == self.get_title():
            return True
        else:
            return False


        # actual_title = self.get_title()
        # self.logger.info(actual_title)
        # result = actual_title == title_to_match
        # return result
