import allure

from Pages.BasePage import BasePage
from Pages.CheckOut2.elements import Elements

class CheckOutPage_2(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Checkout2 page")
    def get_title(self):
        self.wait_for_element(Elements.TITLE)
        return self.get_element_text(Elements.TITLE)

    @allure.step("Getting description label")
    def get_desc_label_cart(self):
        self.wait_for_element(Elements.CART_DESC_LABEL)
        return self.get_element_text(Elements.CART_DESC_LABEL)

    @allure.step("Getting quantity label")
    def get_qty_label_cart(self):
        self.wait_for_element(Elements.CART_QUANTITY_LABEL)
        return self.get_element_text(Elements.CART_QUANTITY_LABEL)

    @allure.step("Getting quantity")
    def get_qty_cart(self):
        self.wait_for_element(Elements.CART_QUANTITY)
        return self.get_element_text(Elements.CART_QUANTITY)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        self.wait_for_element(Elements.ITEM_PRICE)
        return self.get_element_text(Elements.ITEM_PRICE)

    @allure.step("Getting subtotal")
    def get_subtotal(self):
        self.wait_for_element(Elements.SUBTOTAL)
        return self.get_element_text(Elements.SUBTOTAL)

    @allure.step("Getting tax")
    def get_tax(self):
        self.wait_for_element(Elements.TAX)
        return self.get_element_text(Elements.TAX)

    @allure.step("Getting total price")
    def get_total_price(self):
        self.wait_for_element(Elements.TOTAL)
        return self.get_element_text(Elements.TOTAL)

    @allure.step("Finishing checkout")
    def finish_checkout(self):
        self.wait_for_element(Elements.BTN_FINISH)
        self.do_click(Elements.BTN_FINISH)
        from Pages.CheckOutFinish.CheckOutFinishPage import CheckOutPage_Finish
        return CheckOutPage_Finish(self.driver)

    @allure.step("Cancelling checkout")
    def cancel_checkout(self):
        self.wait_for_element(Elements.BTN_CANCEL)
        self.do_click(Elements.BTN_CANCEL)
        from Pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)
