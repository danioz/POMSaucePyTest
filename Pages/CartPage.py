import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_CONTINUE_SHOPPING = (By.ID, 'continue-shopping')
    BTN_CHECKOUT = (By.ID, 'checkout')
    BTN_REMOVE_FROM_CART = (By.XPATH, "//button[text()='Remove']")
    CART_QUANTITY_LABEL = (By.CLASS_NAME, 'cart_quantity_label')
    CART_DESC_LABEL = (By.CLASS_NAME, 'cart_desc_label')
    CART_QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Cart Page")
    def get_title(self):
        self.wait_for_element(self.TITLE)
        return self.get_element_text(self.TITLE)

    @allure.step("Getting description label")
    def get_desc_label_cart(self):
        self.wait_for_element(self.CART_DESC_LABEL)
        return self.get_element_text(self.CART_DESC_LABEL)

    @allure.step("Getting quantity label")
    def get_qty_label_cart(self):
        self.wait_for_element(self.CART_QUANTITY_LABEL)
        return self.get_element_text(self.CART_QUANTITY_LABEL)

    @allure.step("Getting quantity of item in the cart")
    def get_qty_cart(self):
        self.wait_for_element(self.CART_QUANTITY)
        return self.get_element_text(self.CART_QUANTITY)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        self.wait_for_element(self.ITEM_PRICE)
        return self.get_element_text(self.ITEM_PRICE)

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.wait_for_element(self.BTN_REMOVE_FROM_CART)
        self.do_click(self.BTN_REMOVE_FROM_CART)

    @allure.step("Verification of the empty cart")
    def empty_cart(self):
        return self.is_not_visible(self.ITEM_PRICE)

    @allure.step("Checking-out")
    def checkout(self):
        self.wait_for_element(self.BTN_CHECKOUT)
        self.do_click(self.BTN_CHECKOUT)

    @allure.step("Continue shopping")
    def continue_shopping(self):
        self.wait_for_element(self.BTN_CONTINUE_SHOPPING)
        self.do_click(self.BTN_CONTINUE_SHOPPING)
