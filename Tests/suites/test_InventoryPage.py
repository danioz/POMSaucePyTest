import allure
import pytest

import Config.config
from Tests.test_base import BaseTest

@allure.suite('Test Inventory')
@allure.sub_suite('Test Inventory')
class Test_Inventory(BaseTest):
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_url = Config.config.Test_Data.BASE_URL

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking adding item to the cart')
    @allure.description('Adding item to the cart and verifying cart')
    def test_add_to_cart(self):
        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking removing element to the cart')
    @allure.description('Adding items to the cart, then removing item and verifying cart')
    def test_remove_from_cart(self):
        self.inventoryPage.add_to_cart()
        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '2'
        self.inventoryPage.remove_from_cart()
        assert self.inventoryPage.check_cart() == '1'

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking emptying the cart')
    @allure.description('Adding item to the cart then removing item and verifying empty cart')
    def test_add_and_empty_cart(self):
        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'
        self.inventoryPage.remove_from_cart()
        assert True == self.inventoryPage.empty_cart()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Adding/Removing one item to cart')
    @allure.description('Adding individual item to the cart, checking cart, removing item and then verifying empty cart')
    @pytest.mark.parametrize("item",
                             [("backpack"), ("bike-light"),("bolt-t-shirt"),
                              ("fleece-jacket"),("onesie"),("t-shirt-(red)")])
    def test_add_to_cart_one_item_then_remove(self, item):
        self.inventoryPage.add_item_to_cart(item)
        assert self.inventoryPage.check_cart() == '1'
        self.inventoryPage.remove_item_from_cart(item)
        assert True == self.inventoryPage.empty_cart()
