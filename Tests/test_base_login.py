import pytest

from Config.config import Test_Data


@pytest.mark.usefixtures("init_driver")
class BaseLoginTest:
    def setup_method(self):
        self.driver.get(Test_Data.BASE_URL)
