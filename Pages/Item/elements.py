from selenium.webdriver.common.by import By


class Elements:
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_BACK_TO_PRODUCTS = (By.ID, 'back-to-products')
    BTN_ADD_TO_CART = (By.XPATH, "//button[contains(@id,'add-to-cart-')]")
    BTN_REMOVE = (By.XPATH, "//button[contains(@id,'remove-')]")
    ITEM_NAME = (By.CSS_SELECTOR, '.inventory_details_name.large_size')
    ITEM_DESC = (By.CSS_SELECTOR, '.inventory_details_desc.large_size')
    ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_details_price')
