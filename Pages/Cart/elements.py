from selenium.webdriver.common.by import By


class Elements:
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_CONTINUE_SHOPPING = (By.ID, 'continue-shopping')
    BTN_CHECKOUT = (By.ID, 'checkout')
    BTN_REMOVE_FROM_CART = (By.XPATH, "//button[text()='Remove']")
    CART_QUANTITY_LABEL = (By.CLASS_NAME, 'cart_quantity_label')
    CART_DESC_LABEL = (By.CLASS_NAME, 'cart_desc_label')
    CART_QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")
