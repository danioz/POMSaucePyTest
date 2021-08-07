from selenium.webdriver.common.by import By


class Elements:
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
