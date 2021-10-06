import allure

import Config.config
from Pages.Cart.CartPage import CartPage
from Pages.CheckOut1.CheckOut1Page import CheckOutPage_1
from Pages.CheckOut2.CheckOut2Page import CheckOutPage_2
from Pages.Inventory.InventoryPage import InventoryPage
from Tests.test_base import BaseTest

@allure.suite('Test Checkout 2')
@allure.sub_suite('Test Checkout 2')
class Test_CheckOut_2(BaseTest):
    expected_url = Config.config.Test_Data.BASE_URL
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_cart_url = Config.config.Test_Data.CART_URL
    expected_checkout1_url = Config.config.Test_Data.CHECKOUT1_URL
    expected_checkout2_url = Config.config.Test_Data.CHECKOUT2_URL

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Checking elements in the second checkout page ')
    @allure.description('Going to the second checkout page and verifying elements')
    def test_checkout2_page(self):
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
        assert self.checkout2Page.get_title() == 'CHECKOUT: OVERVIEW'
        assert self.checkout2Page.get_desc_label_cart() == 'DESCRIPTION'
        assert self.checkout2Page.get_qty_label_cart() == 'QTY'
        assert self.checkout2Page.get_subtotal() == 'Item total: $0'
        assert self.checkout2Page.get_tax() == 'Tax: $0.00'
        assert self.checkout2Page.get_total_price() == 'Total: $0.00'

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking cancelling checkout')
    @allure.description('Going to the checkout and cancelling checkout procedure')
    def test_cancel_checkout(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkout1Page = CheckOutPage_1(self.driver)
        self.checkout2Page = CheckOutPage_2(self.driver)

        self.inventoryPage\
            .enter_cart()
        self.cartPage\
            .checkout()

        assert self.checkout1Page.get_actual_url() == self.expected_checkout1_url

        self.checkout1Page\
            .input_first_name('Daniel')\
            .input_last_name('Z')\
            .input_postal_code('00-100')\
            .continue_checkout()

        assert self.checkout2Page.get_actual_url() == self.expected_checkout2_url

        self.checkout2Page\
            .cancel_checkout()

        assert self.inventoryPage.get_actual_url() == self.expected_inventory_url

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking checkout procedure')
    @allure.description('Going to the checkout, verifying price and continue checkout procedure')
    def test_price_checkout(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkout1Page = CheckOutPage_1(self.driver)
        self.checkout2Page = CheckOutPage_2(self.driver)

        self.inventoryPage\
            .add_to_cart()

        assert self.inventoryPage.check_cart() == '1'

        self.inventoryPage\
            .enter_cart()
        qty = self.cartPage.get_qty_cart()
        price = self.cartPage.get_item_price()
        self.cartPage\
            .checkout()

        assert self.checkout1Page.get_actual_url() == self.expected_checkout1_url

        self.checkout1Page\
            .input_first_name('Daniel')\
            .input_last_name('Z')\
            .input_postal_code('00-100')\
            .continue_checkout()

        assert self.checkout2Page.get_actual_url() == self.expected_checkout2_url
        assert self.checkout2Page.get_qty_cart() == qty
        assert self.checkout2Page.get_item_price() == price
        assert self.checkout2Page.get_subtotal() == f'Item total: {price}'
        assert self.checkout2Page.get_tax() == 'Tax: $2.40'
        assert self.checkout2Page.get_total_price() == 'Total: $32.39'