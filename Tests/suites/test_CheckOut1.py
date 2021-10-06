import pytest
import allure

import Config.config
from Pages.Cart.CartPage import CartPage
from Pages.CheckOut1.CheckOut1Page import CheckOutPage_1
from Pages.CheckOut2.CheckOut2Page import CheckOutPage_2
from Pages.Inventory.InventoryPage import InventoryPage
from Tests.test_base import BaseTest

@allure.suite('Test Checkout 1')
@allure.sub_suite('Test Checkout 1')
class Test_CheckOut_1(BaseTest):
    expected_url = Config.config.Test_Data.BASE_URL
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_cart_url = Config.config.Test_Data.CART_URL
    expected_checkout1_url = Config.config.Test_Data.CHECKOUT1_URL
    expected_checkout2_url = Config.config.Test_Data.CHECKOUT2_URL

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Checking elements in checkout page ')
    @allure.description('Going to the checkout and verifying elements')
    @pytest.mark.parametrize("expected_inputs", [['First Name', 'Last Name', 'Zip/Postal Code']])
    def test_checkout_page(self, expected_inputs):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkout1Page = CheckOutPage_1(self.driver)

        self.inventoryPage\
            .enter_cart()

        assert self.cartPage.get_actual_url() == self.expected_cart_url

        self.cartPage\
            .checkout()

        assert self.checkout1Page.get_actual_url() == self.expected_checkout1_url
        assert self.checkout1Page.get_title() == 'CHECKOUT: YOUR INFORMATION'
        assert self.checkout1Page.get_inputs('placeholder') == expected_inputs

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Checking error messages')
    @allure.description('Going to the checkout and verifying possible error messages due to lack of inputs')
    def test_fill_checkout_errors(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkout1Page = CheckOutPage_1(self.driver)

        self.inventoryPage\
            .enter_cart()

        assert self.cartPage.get_actual_url() == self.expected_cart_url

        self.cartPage\
            .checkout()

        assert self.checkout1Page.get_actual_url() == self.expected_checkout1_url

        self.checkout1Page\
            .continue_checkout()

        assert self.checkout1Page.get_error_message() == 'Error: First Name is required'

        self.checkout1Page\
            .input_first_name('Daniel')\
            .continue_checkout()

        assert self.checkout1Page.get_error_message() == 'Error: Last Name is required'

        self.checkout1Page\
            .input_last_name('Zet')\
            .continue_checkout()

        assert self.checkout1Page.get_error_message() == 'Error: Postal Code is required'
        assert self.checkout1Page.get_error_svg() == True

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Checking cancelling checkout')
    @allure.description('Going to the checkout and cancelling checkout procedure')
    def test_cancel_checkout(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkout1Page = CheckOutPage_1(self.driver)

        self.inventoryPage\
            .enter_cart()
        assert self.cartPage.get_actual_url() == self.expected_cart_url
        self.cartPage\
            .checkout()
        assert self.checkout1Page.get_actual_url() == self.expected_checkout1_url
        self.checkout1Page\
            .continue_checkout()
        assert self.checkout1Page.get_error_message() == 'Error: First Name is required'
        self.checkout1Page\
            .cancel_checkout()
        assert self.cartPage.get_actual_url() == self.expected_cart_url

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Checking checkout procedure')
    @allure.description('Going to the checkout and continue checkout procedure')
    def test_fill_checkout_continue(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkout1Page = CheckOutPage_1(self.driver)
        self.checkout2Page = CheckOutPage_2(self.driver)

        self.inventoryPage\
            .enter_cart()
        assert self.cartPage.get_actual_url() == self.expected_cart_url
        self.cartPage\
            .checkout()
        assert self.checkout1Page.get_actual_url() == self.expected_checkout1_url
        self.checkout1Page\
            .input_first_name('Daniel')\
            .input_last_name('Zet')\
            .input_postal_code('99-100')\
            .continue_checkout()

        assert self.checkout2Page.get_actual_url() == self.expected_checkout2_url