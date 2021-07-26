import pytest
import allure

import Config.config
from Tests.test_base import BaseTest


class Test_Inventory(BaseTest):
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_url = Config.config.Test_Data.BASE_URL

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self):
        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'

    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_from_cart(self):
        self.inventoryPage.add_to_cart()
        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '2'
        self.inventoryPage.remove_from_cart()
        assert self.inventoryPage.check_cart() == '1'

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_and_empty_cart(self):
        self.inventoryPage.add_to_cart()
        assert self.inventoryPage.check_cart() == '1'
        self.inventoryPage.remove_from_cart()
        status = self.inventoryPage.empty_cart()
        assert True == status