import allure

import Config.config
from Pages.Cart.CartPage import CartPage
from Pages.CheckOut1.CheckOut1Page import CheckOutPage_1
from Pages.Inventory.InventoryPage import InventoryPage
from Tests.test_base import BaseTest

@allure.suite('Test Cart')
@allure.sub_suite('Test Cart')
class Test_Cart(BaseTest):
    expected_url = Config.config.Test_Data.BASE_URL
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_cart_url = Config.config.Test_Data.CART_URL
    expected_checkout1_url = Config.config.Test_Data.CHECKOUT1_URL

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Checking elements in Cart')
    @allure.description('Going to the cart and verifying elements')
    def test_go_to_cart(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)

        self.inventoryPage.enter_cart()

        assert self.cartPage.check_url() == self.expected_cart_url
        assert self.cartPage.get_title() == 'YOUR CART'
        assert self.cartPage.get_desc_label_cart() == 'DESCRIPTION'
        assert self.cartPage.get_qty_label_cart() == 'QTY'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Continue shopping')
    @allure.description('Adding item to the cart, then remove it from the cart. Continue shopping and add item to the cart')
    def test_continue_shopping(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)

        self.inventoryPage.add_to_cart()

        assert self.inventoryPage.check_cart() == '1'

        self.inventoryPage.enter_cart()

        assert self.cartPage.get_qty_cart() == '1'
        assert self.cartPage.get_item_price() == '$29.99'

        self.cartPage.remove_from_cart()
        status = self.cartPage.empty_cart()

        assert True == status
        status_2 = self.inventoryPage.empty_cart()
        assert True == status_2

        self.cartPage.continue_shopping()
        self.inventoryPage.add_to_cart()

        assert self.inventoryPage.check_cart() == '1'
        assert self.inventoryPage.check_url() == self.expected_inventory_url

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Going to the checkout page')
    @allure.description('Adding item to the cart and checkout')
    def test_checkout(self):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkout1Page = CheckOutPage_1(self.driver)

        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'
        self.inventoryPage.enter_cart()
        assert self.cartPage.get_qty_cart() == '1'
        assert self.cartPage.get_item_price() == '$29.99'
        self.cartPage.checkout()
        assert self.checkout1Page.check_url() == self.expected_checkout1_url