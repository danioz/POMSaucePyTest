import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from Pages.Login.LoginPage import LoginPage
from Pages.Inventory.InventoryPage import InventoryPage
from Pages.SideBar.SideBarPage import SideBarPage

web_driver = None


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    if request.param == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    if request.param == "opera":
        web_driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    request.cls.loginPage = LoginPage(web_driver)
    request.cls.inventoryPage = InventoryPage(web_driver)
    request.cls.sideBarPage = SideBarPage(web_driver)

    yield
    web_driver.quit()
