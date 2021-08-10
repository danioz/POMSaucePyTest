import allure

from Pages.BasePage import BasePage
from Pages.CheckOut2.elements import Elements

class CheckOutPage_2(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Checkout2 page")
    def get_title(self):
        return self.get_element_text(Elements.TITLE)

    @allure.step("Getting description label")
    def get_desc_label_cart(self):
        return self.get_element_text(Elements.CART_DESC_LABEL)

    @allure.step("Getting quantity label")
    def get_qty_label_cart(self):
        return self.get_element_text(Elements.CART_QUANTITY_LABEL)

    @allure.step("Getting quantity")
    def get_qty_cart(self):
        return self.get_element_text(Elements.CART_QUANTITY)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        return self.get_element_text(Elements.ITEM_PRICE)

    @allure.step("Getting subtotal")
    def get_subtotal(self):
        return self.get_element_text(Elements.SUBTOTAL)

    @allure.step("Getting tax")
    def get_tax(self):
        return self.get_element_text(Elements.TAX)

    @allure.step("Getting total price")
    def get_total_price(self):
        return self.get_element_text(Elements.TOTAL)

    @allure.step("Finishing checkout")
    def finish_checkout(self):
        self.do_click(Elements.BTN_FINISH)
        from Pages.CheckOutFinish.CheckOutFinishPage import CheckOutPage_Finish
        return CheckOutPage_Finish(self.driver)

    @allure.step("Cancelling checkout")
    def cancel_checkout(self):
        self.do_click(Elements.BTN_CANCEL)
        from Pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)
