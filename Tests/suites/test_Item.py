import pytest
import allure

import Config.config
from Pages.Inventory.InventoryPage import InventoryPage
from Pages.Item.ItemPage import ItemPage
from Pages.Login.LoginPage import LoginPage
from Tests.test_base import BaseTest


@allure.suite("Test Item")
@allure.sub_suite("Test Item")
class Test_Item(BaseTest):

    @pytest.fixture(autouse=True)
    def class_setup(self, init_driver):
        self.inventoryPage = InventoryPage(self.driver)
        self.itemPage = ItemPage(self.driver)

    expected_item_url = Config.config.Test_Data.ITEM_URL
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_url = Config.config.Test_Data.BASE_URL

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Checking adding item to the cart")
    @allure.description("Adding item to the cart and verifying cart")
    @pytest.mark.parametrize(
        "item",
        [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ],
    )
    def test_add_to_cart(self, item):

        self.inventoryPage\
            .add_item_link(item)
        assert self.expected_item_url in self.itemPage.get_actual_url()

        self.itemPage\
            .add_to_cart()
        assert self.inventoryPage.check_cart() == "1"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Checking removing item from the cart")
    @allure.description("Adding item to the cart, then removing and verifying cart")
    @pytest.mark.parametrize(
        "item",
        [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ],
    )
    def test_remove_from_cart(self, item):

        self.inventoryPage\
            .add_item_link(item)
        assert self.expected_item_url in self.itemPage.get_actual_url()

        self.itemPage\
            .add_to_cart()
        assert self.inventoryPage.check_cart() == "1"

        self.itemPage\
            .remove_from_cart()
        assert True == self.inventoryPage.empty_cart()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Checking backing to products")
    @allure.description("Adding item to the cart and back to the inventory page")
    @pytest.mark.parametrize(
        "item",
        [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ],
    )
    def test_back_to_products(self, item):

        self.inventoryPage\
            .add_item_link(item)
        assert self.expected_item_url in self.itemPage.get_actual_url()

        self.itemPage\
            .back_to_products()
        assert self.inventoryPage.get_actual_url() == self.expected_inventory_url

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checking item elements")
    @allure.description(
        "Adding item to the cart and verifying price, title and description of the item"
    )
    @pytest.mark.parametrize(
        "item",
        [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ],
    )
    def test_compare_item(self, item):

        name = self.inventoryPage.get_item_name(item)
        desc = self.inventoryPage.get_item_description(item)
        price = self.inventoryPage.get_item_price(item)

        self.inventoryPage\
            .add_item_link(item)

        assert self.expected_item_url in self.itemPage.get_actual_url()
        assert self.itemPage.get_item_name() == name
        assert self.itemPage.get_item_description() == desc
        assert self.itemPage.get_item_price() == price
