from selenium.webdriver.common.by import By


class Elements:
    text = ''

    TITLE = (By.XPATH, "//span[@class='title']")

    ADD_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_BIKE_LIGHT = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    ADD_T_SHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_JACKET = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    ADD_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    ADD_RED_T_SHIRT = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')

    LINK_BACKPACK = (By.CSS_SELECTOR, '#item_4_title_link div')
    LINK_BIKE_LIGHT = (By.CSS_SELECTOR, '#item_0_title_link div')
    LINK_T_SHIRT = (By.CSS_SELECTOR, '#item_1_title_link div')
    LINK_JACKET = (By.CSS_SELECTOR, '#item_5_title_link div')
    LINK_ONESIE = (By.CSS_SELECTOR, '#item_2_title_link div')
    LINK_RED_T_SHIRT = (By.CSS_SELECTOR, '#item_3_title_link div')

    GET_ITEM_NAME = f"//div[@class='inventory_item_name'][text()='{text}']"
    GET_ITEM_DESC = f"//div[@class='inventory_item_name'][text()='{text}']"
    GET_ITEM_PRICE = f"//div[@class='inventory_item_name'][text()='{text}']"

    ADD_ITEM = f"//div[@class='inventory_item_name'][text()='{text}']"

    REMOVE_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')
    REMOVE_BIKE_LIGHT = (By.ID, 'remove-sauce-labs-bike-light')
    REMOVE_T_SHIRT = (By.ID, 'remove-sauce-labs-bolt-t-shirt')
    REMOVE_JACKET = (By.ID, 'remove-sauce-labs-fleece-jacket')
    REMOVE_ONESIE = (By.ID, 'remove-sauce-labs-onesie')
    REMOVE_RED_T_SHIRT = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')

    ADD_TO_CART = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
    REMOVE_FROM_CART = (By.XPATH, "//button[text()='Remove']")
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    CART = (By.CLASS_NAME, 'shopping_cart_link')

