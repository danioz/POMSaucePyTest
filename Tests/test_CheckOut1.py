import pytest
import allure

import Config.config
from Tests.test_base import BaseTest


class Test_CheckOut_1(BaseTest):
    expected_url = Config.config.Test_Data.BASE_URL
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_cart_url = Config.config.Test_Data.CART_URL
    expected_checkout1_url = Config.config.Test_Data.CHECKOUT1_URL
    expected_checkout2_url = Config.config.Test_Data.CHECKOUT2_URL

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("expected_inputs", [['First Name', 'Last Name', 'Zip/Postal Code']])
    def test_checkout_page(self, expected_inputs):
        self.inventoryPage.enter_cart()
        assert self.cartPage.check_url() == self.expected_cart_url

        self.cartPage.checkout()
        assert self.checkout1Page.check_url() == self.expected_checkout1_url
        assert self.checkout1Page.get_title() == 'CHECKOUT: YOUR INFORMATION'
        current_inputs = self.checkout1Page.get_inputs('placeholder')
        assert current_inputs == expected_inputs

    @allure.severity(allure.severity_level.NORMAL)
    def test_fill_checkout_errors(self):
        self.inventoryPage.enter_cart()
        assert self.cartPage.check_url() == self.expected_cart_url
        self.cartPage.checkout()
        assert self.checkout1Page.check_url() == self.expected_checkout1_url
        self.checkout1Page.continue_checkout()
        assert self.checkout1Page.get_error_message() == 'Error: First Name is required'
        self.checkout1Page.input_first_name('Daniel')
        self.checkout1Page.continue_checkout()
        assert self.checkout1Page.get_error_message() == 'Error: Last Name is required'
        self.checkout1Page.input_last_name('Zet')
        self.checkout1Page.continue_checkout()
        assert self.checkout1Page.get_error_message() == 'Error: Postal Code is required'
        assert self.checkout1Page.get_error_svg() == True

    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_checkout(self):
        self.inventoryPage.enter_cart()
        assert self.cartPage.check_url() == self.expected_cart_url
        self.cartPage.checkout()
        assert self.checkout1Page.check_url() == self.expected_checkout1_url
        self.checkout1Page.continue_checkout()
        assert self.checkout1Page.get_error_message() == 'Error: First Name is required'
        self.checkout1Page.cancel_checkout()
        assert self.cartPage.check_url() == self.expected_cart_url

    @allure.severity(allure.severity_level.NORMAL)
    def test_fill_checkout_continue(self):
        self.inventoryPage.enter_cart()
        assert self.cartPage.check_url() == self.expected_cart_url
        self.cartPage.checkout()
        assert self.checkout1Page.check_url() == self.expected_checkout1_url
        self.checkout1Page.input_first_name('Daniel')
        self.checkout1Page.input_last_name('Zet')
        self.checkout1Page.input_postal_code('99-100')
        self.checkout1Page.continue_checkout()
        assert self.checkout2Page.check_url() == self.expected_checkout2_url