import allure

from Pages.BasePage import BasePage
from Pages.Cart.elements import Elements


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Cart Page")
    def get_title(self):
        return self.get_element_text(Elements.TITLE)

    @allure.step("Getting description label")
    def get_desc_label_cart(self):
        return self.get_element_text(Elements.CART_DESC_LABEL)

    @allure.step("Getting quantity label")
    def get_qty_label_cart(self):
        return self.get_element_text(Elements.CART_QUANTITY_LABEL)

    @allure.step("Getting quantity of item in the cart")
    def get_qty_cart(self):
        return self.get_element_text(Elements.CART_QUANTITY)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        return self.get_element_text(Elements.ITEM_PRICE)

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.do_click(Elements.BTN_REMOVE_FROM_CART)
        return self

    @allure.step("Verification of the empty cart")
    def empty_cart(self):
        return self.is_not_visible(Elements.ITEM_PRICE)

    @allure.step("Checking-out")
    def checkout(self):
        self.do_click(Elements.BTN_CHECKOUT)
        from Pages.CheckOut1.CheckOut1Page import CheckOutPage_1

        return CheckOutPage_1(self.driver)

    @allure.step("Continue shopping")
    def continue_shopping(self):
        self.do_click(Elements.BTN_CONTINUE_SHOPPING)
        from Pages.Inventory.InventoryPage import InventoryPage

        return InventoryPage(self.driver)
