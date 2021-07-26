import pytest
from Config.config import Test_Data


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    def setup_method(self):
        self.loginPage.do_login(Test_Data.STANDARD_USER_NAME, Test_Data.PASSWORD)
        assert self.inventoryPage.check_url() == self.expected_inventory_url

    def teardown_method(self):
        self.sideBarPage.do_logout()
        assert self.loginPage.check_url() == self.expected_url
