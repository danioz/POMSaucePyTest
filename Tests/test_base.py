import allure
import pytest
from Config.config import Test_Data
from Pages.Inventory.InventoryPage import InventoryPage
from Pages.Login.LoginPage import LoginPage
from Pages.SideBar.SideBarPage import SideBarPage


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    def setup_method(self):
        # self.loginPage = LoginPage(self.driver)
        # self.inventoryPage = InventoryPage(self.driver)

        self.loginPage.do_login(Test_Data.STANDARD_USER_NAME, Test_Data.PASSWORD)
        assert self.inventoryPage.get_actual_url() == self.expected_inventory_url

    def teardown_method(self):
        # self.sideBarPage = SideBarPage(self.driver)
        # self.loginPage = LoginPage(self.driver)

        self.sideBarPage.do_logout()
        assert self.loginPage.get_actual_url() == self.expected_url
