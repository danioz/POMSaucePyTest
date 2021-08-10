import allure

from Pages.BasePage import BasePage
from Pages.Item.elements import Elements


class ItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Adding item to the cart")
    def add_to_cart(self):
        self.wait_for_element(Elements.BTN_ADD_TO_CART)
        self.do_click(Elements.BTN_ADD_TO_CART)

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.wait_for_element(Elements.BTN_REMOVE)
        self.do_click(Elements.BTN_REMOVE)

    @allure.step("Getting back to the products")
    def back_to_products(self):
        self.wait_for_element(Elements.BTN_BACK_TO_PRODUCTS)
        self.do_click(Elements.BTN_BACK_TO_PRODUCTS)
        from Pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)

    @allure.step("Getting name of the item")
    def get_item_name(self):
        self.wait_for_element(Elements.ITEM_NAME)
        return self.get_element_text(Elements.ITEM_NAME)

    @allure.step("Getting description of the item")
    def get_item_description(self):
        self.wait_for_element(Elements.ITEM_DESC)
        return self.get_element_text(Elements.ITEM_DESC)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        self.wait_for_element(Elements.ITEM_PRICE)
        return self.get_element_text(Elements.ITEM_PRICE)
