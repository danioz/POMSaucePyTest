import pytest
import allure

import Config.config
from Tests.test_base import BaseTest


class Test_Item(BaseTest):
    expected_item_url = Config.config.Test_Data.ITEM_URL
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_url = Config.config.Test_Data.BASE_URL

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("item", ['Sauce Labs Backpack',
                                      'Sauce Labs Bike Light',
                                      'Sauce Labs Bolt T-Shirt',
                                      'Sauce Labs Fleece Jacket',
                                      'Sauce Labs Onesie',
                                      'Test.allTheThings() T-Shirt (Red)'
                                      ])
    def test_add_to_cart(self, item):
        self.inventoryPage.add_item_link(item)
        assert self.expected_item_url in self.itemPage.check_url()
        self.itemPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("item", ['Sauce Labs Backpack',
                                      'Sauce Labs Bike Light',
                                      'Sauce Labs Bolt T-Shirt',
                                      'Sauce Labs Fleece Jacket',
                                      'Sauce Labs Onesie',
                                      'Test.allTheThings() T-Shirt (Red)'
                                      ])
    def test_remove_from_cart(self, item):
        self.inventoryPage.add_item_link(item)
        assert self.expected_item_url in self.itemPage.check_url()
        self.itemPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'
        self.itemPage.remove_from_cart()
        status = self.inventoryPage.empty_cart()
        assert status == True

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("item", ['Sauce Labs Backpack',
                                      'Sauce Labs Bike Light',
                                      'Sauce Labs Bolt T-Shirt',
                                      'Sauce Labs Fleece Jacket',
                                      'Sauce Labs Onesie',
                                      'Test.allTheThings() T-Shirt (Red)'
                                      ])
    def test_back_to_products(self, item):
        self.inventoryPage.add_item_link(item)
        assert self.expected_item_url in self.itemPage.check_url()
        self.itemPage.back_to_products()
        assert self.inventoryPage.check_url() == self.expected_inventory_url

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("item", ['Sauce Labs Backpack',
                                      'Sauce Labs Bike Light',
                                      'Sauce Labs Bolt T-Shirt',
                                      'Sauce Labs Fleece Jacket',
                                      'Sauce Labs Onesie',
                                      'Test.allTheThings() T-Shirt (Red)'
                                      ])
    def test_compare_item(self, item):
        name = self.inventoryPage.get_item_name(item)
        desc = self.inventoryPage.get_item_description(item)
        price = self.inventoryPage.get_item_price(item)
        self.inventoryPage.add_item_link(item)
        assert self.expected_item_url in self.itemPage.check_url()
        assert self.itemPage.get_item_name() == name
        assert self.itemPage.get_item_description() == desc
        assert self.itemPage.get_item_price() == price