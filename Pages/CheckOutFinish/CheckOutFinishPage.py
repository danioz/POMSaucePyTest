import allure

from Pages.BasePage import BasePage
from Pages.CheckOutFinish.elements import Elements


class CheckOutPage_Finish(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Checkout Finish page")
    def get_title(self):
        return self.get_element_text(Elements.TITLE)

    @allure.step("Getting checkout header")
    def get_checkout_header(self):
        return self.get_element_text(Elements.H2_COMPLETE_ORDER)

    @allure.step("Getting checkout message")
    def get_checkout_message(self):
        return self.get_element_text(Elements.COMPLETE_TEXT)

    @allure.step("Getting back home")
    def go_back_home(self):
        self.do_click(Elements.BTN_BACK_HOME)
        from Pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)
