import allure

from Pages.BasePage import BasePage
from Pages.Item.elements import Elements


class ItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Adding item to the cart")
    def add_to_cart(self):
        self.do_click(Elements.BTN_ADD_TO_CART)

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.do_click(Elements.BTN_REMOVE)

    @allure.step("Getting back to the products")
    def back_to_products(self):
        self.do_click(Elements.BTN_BACK_TO_PRODUCTS)
        from Pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)

    @allure.step("Getting name of the item")
    def get_item_name(self):
        return self.get_element_text(Elements.ITEM_NAME)

    @allure.step("Getting description of the item")
    def get_item_description(self):
        return self.get_element_text(Elements.ITEM_DESC)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        return self.get_element_text(Elements.ITEM_PRICE)
