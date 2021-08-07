import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckOutPage_2(BasePage):
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_FINISH = (By.ID, 'finish')
    BTN_CANCEL = (By.ID, 'cancel')
    CART_QUANTITY_LABEL = (By.CLASS_NAME, 'cart_quantity_label')
    CART_DESC_LABEL = (By.CLASS_NAME, 'cart_desc_label')
    CART_QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    SUBTOTAL = (By.CLASS_NAME, 'summary_subtotal_label')
    TAX = (By.CLASS_NAME, 'summary_tax_label')
    TOTAL = (By.CLASS_NAME, 'summary_total_label')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Checkout2 page")
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

    @allure.step("Getting quantity")
    def get_qty_cart(self):
        self.wait_for_element(self.CART_QUANTITY)
        return self.get_element_text(self.CART_QUANTITY)

    @allure.step("Getting price of the item")
    def get_item_price(self):
        self.wait_for_element(self.ITEM_PRICE)
        return self.get_element_text(self.ITEM_PRICE)

    @allure.step("Getting subtotal")
    def get_subtotal(self):
        self.wait_for_element(self.SUBTOTAL)
        return self.get_element_text(self.SUBTOTAL)

    @allure.step("Getting tax")
    def get_tax(self):
        self.wait_for_element(self.TAX)
        return self.get_element_text(self.TAX)

    @allure.step("Getting total price")
    def get_total_price(self):
        self.wait_for_element(self.TOTAL)
        return self.get_element_text(self.TOTAL)

    @allure.step("Finishing checkout")
    def finish_checkout(self):
        self.wait_for_element(self.BTN_FINISH)
        self.do_click(self.BTN_FINISH)

    @allure.step("Cancelling checkout")
    def cancel_checkout(self):
        self.wait_for_element(self.BTN_CANCEL)
        self.do_click(self.BTN_CANCEL)
