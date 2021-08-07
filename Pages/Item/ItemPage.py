import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ItemPage(BasePage):
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_BACK_TO_PRODUCTS = (By.ID, 'back-to-products')
    BTN_ADD_TO_CART = (By.XPATH, "//button[contains(@id,'add-to-cart-')]")
    BTN_REMOVE = (By.XPATH, "//button[contains(@id,'remove-')]")
    ITEM_NAME = (By.CSS_SELECTOR, '.inventory_details_name.large_size')
    ITEM_DESC = (By.CSS_SELECTOR, '.inventory_details_desc.large_size')
    ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_details_price')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Adding item to the cart")
    def add_to_cart(self):
        self.wait_for_element(self.BTN_ADD_TO_CART)
        self.do_click(self.BTN_ADD_TO_CART)

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.wait_for_element(self.BTN_REMOVE)
        self.do_click(self.BTN_REMOVE)

    @allure.step("Getting back to the products")
    def back_to_products(self):
        self.wait_for_element(self.BTN_BACK_TO_PRODUCTS)
        self.do_click(self.BTN_BACK_TO_PRODUCTS)

    @allure.step("Getting name of the item")
    def get_item_name(self):
        self.wait_for_element(self.ITEM_NAME)
        return self.get_element_text(self.ITEM_NAME)

    @allure.step("Getting description of the item")
    def get_item_description(self):
        self.wait_for_element(self.ITEM_DESC)
        return self.get_element_text(self.ITEM_DESC)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        self.wait_for_element(self.ITEM_PRICE)
        return self.get_element_text(self.ITEM_PRICE)