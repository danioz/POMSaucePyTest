import allure

from Pages.BasePage import BasePage
from Pages.Cart.elements import Elements


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Cart Page")
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

    @allure.step("Getting quantity of item in the cart")
    def get_qty_cart(self):
        self.wait_for_element(Elements.CART_QUANTITY)
        return self.get_element_text(Elements.CART_QUANTITY)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        self.wait_for_element(Elements.ITEM_PRICE)
        return self.get_element_text(Elements.ITEM_PRICE)

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.wait_for_element(Elements.BTN_REMOVE_FROM_CART)
        self.do_click(Elements.BTN_REMOVE_FROM_CART)

    @allure.step("Verification of the empty cart")
    def empty_cart(self):
        return self.is_not_visible(Elements.ITEM_PRICE)

    @allure.step("Checking-out")
    def checkout(self):
        self.wait_for_element(Elements.BTN_CHECKOUT)
        self.do_click(Elements.BTN_CHECKOUT)

    @allure.step("Continue shopping")
    def continue_shopping(self):
        self.wait_for_element(Elements.BTN_CONTINUE_SHOPPING)
        self.do_click(Elements.BTN_CONTINUE_SHOPPING)
