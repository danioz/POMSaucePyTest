import allure
import pytest

import Config.config
from Tests.test_base import BaseTest


@allure.suite('Test Inventory')
@allure.sub_suite('Test Inventory')
class Test_Inventory(BaseTest):
    expected_inventory_title = 'PRODUCTS'
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_url = Config.config.Test_Data.BASE_URL

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking adding item to the cart')
    @allure.description('Adding item to the cart and verifying cart')
    def test_add_to_cart(self):
        self.inventoryPage \
            .ASSERT_actual_title(self.expected_inventory_title) \
            .ASSERT_actual_url(self.expected_inventory_url) \
            .ASSERT_empty_cart() \
            .add_to_cart() \
            .ASSERT_actual_cart('1')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking removing element to the cart')
    @allure.description('Adding items to the cart, then removing item and verifying cart')
    def test_remove_from_cart(self):
        self.inventoryPage \
            .ASSERT_actual_title(self.expected_inventory_title) \
            .ASSERT_actual_url(self.expected_inventory_url) \
            .ASSERT_empty_cart() \
            .add_to_cart() \
            .add_to_cart() \
            .ASSERT_actual_cart('2') \
            .remove_from_cart() \
            .ASSERT_actual_cart('1')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checking emptying the cart')
    @allure.description('Adding item to the cart then removing item and verifying empty cart')
    def test_add_and_empty_cart(self):
        self.inventoryPage \
            .ASSERT_actual_title(self.expected_inventory_title) \
            .ASSERT_actual_url(self.expected_inventory_url) \
            .ASSERT_empty_cart() \
            .add_to_cart() \
            .ASSERT_actual_cart('1') \
            .remove_from_cart() \
            .ASSERT_empty_cart()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Adding/Removing one item to/from cart parametrized in Pytest')
    @allure.description(
        'Adding individual item to the cart, checking cart, removing item and then verifying empty cart')
    @pytest.mark.parametrize("item",
                             [("backpack"), ("bike-light"), ("bolt-t-shirt"),
                              ("fleece-jacket"), ("onesie"), ("t-shirt-(red)")])
    def test_add_to_cart_one_item_then_remove(self, item):
        self.inventoryPage \
            .ASSERT_actual_title(self.expected_inventory_title) \
            .ASSERT_actual_url(self.expected_inventory_url) \
            .ASSERT_empty_cart() \
            .add_item_to_cart(item) \
            .ASSERT_actual_cart('1') \
            .remove_item_from_cart(item) \
            .ASSERT_empty_cart()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Looping through Adding/Removing available item to/from cart')
    @allure.description(
        'Looping through Adding available item to the cart, checking cart, removing item and then verifying empty cart')
    def test_looping_add_to_cart_one_item_then_remove(self):
        for item in self.inventoryPage.list_of_available_item():
            self.inventoryPage \
                .ASSERT_empty_cart() \
                .add_item_to_cart(item) \
                .ASSERT_actual_cart('1') \
                .remove_item_from_cart(item) \
                .ASSERT_empty_cart()
