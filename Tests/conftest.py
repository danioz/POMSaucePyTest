import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Pages.Login.LoginPage import LoginPage
from Pages.Inventory.InventoryPage import InventoryPage
from Pages.Item.ItemPage import ItemPage
from Pages.SideBar.SideBarPage import SideBarPage
from Pages.Cart.CartPage import CartPage
from Pages.CheckOut1.CheckOut1Page import CheckOutPage_1
from Pages.CheckOut2.CheckOut2Page import CheckOutPage_2
from Pages.CheckOutFinish.CheckOutFinishPage import CheckOutPage_Finish

web_driver = None


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global web_driver
    options = webdriver.ChromeOptions()
    options.headless = False
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    request.cls.loginPage = LoginPage(web_driver)
    request.cls.inventoryPage = InventoryPage(web_driver)
    request.cls.itemPage = ItemPage(web_driver)
    request.cls.sideBarPage = SideBarPage(web_driver)
    request.cls.cartPage = CartPage(web_driver)
    request.cls.checkout1Page = CheckOutPage_1(web_driver)
    request.cls.checkout2Page = CheckOutPage_2(web_driver)
    request.cls.checkoutFinish = CheckOutPage_Finish(web_driver)

    yield
    web_driver.close()
