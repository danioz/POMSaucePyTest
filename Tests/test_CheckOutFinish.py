import pytest
import allure

import Config.config
from Tests.test_base import BaseTest


class Test_CheckOut_Finish(BaseTest):
    expected_url = Config.config.Test_Data.BASE_URL
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_cart_url = Config.config.Test_Data.CART_URL
    expected_checkout1_url = Config.config.Test_Data.CHECKOUT1_URL
    expected_checkout2_url = Config.config.Test_Data.CHECKOUT2_URL
    expected_checkout_finish_url = Config.config.Test_Data.CHECKOUT_FINISH_URL

    @allure.severity(allure.severity_level.CRITICAL)
    def test_finish_checkout(self):
        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'
        self.inventoryPage.enter_cart()
        qty = self.cartPage.get_qty_cart()
        price = self.cartPage.get_item_price()
        self.cartPage.checkout()
        assert self.checkout1Page.check_url() == self.expected_checkout1_url
        self.checkout1Page.input_first_name('Daniel')
        self.checkout1Page.input_last_name('Z')
        self.checkout1Page.input_postal_code('00-100')
        self.checkout1Page.continue_checkout()
        assert self.checkout2Page.check_url() == self.expected_checkout2_url
        assert self.checkout2Page.get_qty_cart() == qty
        assert self.checkout2Page.get_item_price() == price
        assert self.checkout2Page.get_subtotal() == f'Item total: {price}'
        assert self.checkout2Page.get_tax() == 'Tax: $2.40'
        assert self.checkout2Page.get_total_price() == 'Total: $32.39'
        self.checkout2Page.finish_checkout()
        assert self.checkoutFinish.check_url() == self.expected_checkout_finish_url
        assert self.checkoutFinish.get_title() == 'CHECKOUT: COMPLETE!'
        assert self.checkoutFinish.get_checkout_header() == 'THANK YOU FOR YOUR ORDER'
        assert self.checkoutFinish.get_checkout_message() == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        status = self.inventoryPage.empty_cart()
        assert True == status
        self.checkoutFinish.go_back_home()
        assert self.inventoryPage.check_url() == self.expected_inventory_url