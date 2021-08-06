import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
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

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Inventory page")
    def get_title(self):
        self.wait_for_element(self.TITLE)
        title = self.get_element_text(self.TITLE)
        return title

    @allure.step("Entering cart")
    def enter_cart(self):
        self.wait_for_element(self.CART)
        self.do_click(self.CART)

    @allure.step("Adding Sauce Labs Backpack")
    def add_backpack(self):
        self.wait_for_element(self.ADD_BACKPACK)
        self.do_click(self.ADD_BACKPACK)

    @allure.step("Adding Sauce Labs Bike Light")
    def add_bike_light(self):
        self.wait_for_element(self.ADD_BIKE_LIGHT)
        self.do_click(self.ADD_BIKE_LIGHT)

    @allure.step("Adding Sauce Labs Bolt T-Shirt")
    def add_t_shirt(self):
        self.wait_for_element(self.ADD_T_SHIRT)
        self.do_click(self.ADD_T_SHIRT)

    @allure.step("Adding Sauce Labs Fleece Jacket")
    def add_jacket(self):
        self.wait_for_element(self.ADD_JACKET)
        self.do_click(self.ADD_JACKET)

    @allure.step("Adding Sauce Labs Onesie")
    def add_onesie(self):
        self.wait_for_element(self.ADD_ONESIE)
        self.do_click(self.ADD_ONESIE)

    @allure.step("Adding Test.allTheThings() T-Shirt (Red)")
    def add_red_t_shirt(self):
        self.wait_for_element(self.ADD_RED_T_SHIRT)
        self.do_click(self.ADD_RED_T_SHIRT)

    @allure.step("Removing Sauce Labs Backpack")
    def remove_backpack(self):
        self.wait_for_element(self.REMOVE_BACKPACK)
        self.do_click(self.REMOVE_BACKPACK)

    @allure.step("Removing Sauce Labs Bike Light")
    def remove_bike_light(self):
        self.wait_for_element(self.REMOVE_BIKE_LIGHT)
        self.do_click(self.REMOVE_BIKE_LIGHT)

    @allure.step("Removing Sauce Labs Bolt T-Shirt")
    def remove_t_shirt(self):
        self.wait_for_element(self.REMOVE_T_SHIRT)
        self.do_click(self.REMOVE_T_SHIRT)

    @allure.step("Removing Sauce Labs Fleece Jacket")
    def remove_jacket(self):
        self.wait_for_element(self.REMOVE_JACKET)
        self.do_click(self.REMOVE_JACKET)

    @allure.step("Removing Sauce Labs Onesie")
    def remove_onesie(self):
        self.wait_for_element(self.ADD_ONESIE)
        self.do_click(self.ADD_ONESIE)

    @allure.step("Removing Test.allTheThings() T-Shirt (Red)")
    def remove_red_t_shirt(self):
        self.wait_for_element(self.REMOVE_RED_T_SHIRT)
        self.do_click(self.REMOVE_RED_T_SHIRT)

    @allure.step("Adding item with link")
    def add_item_link(self, item):
        link = (By.XPATH, f"//div[@class='inventory_item_name'][text()='{item}']")
        self.do_click(link)

    @allure.step("Getting name of the item")
    def get_item_name(self, item):
        link = (By.XPATH, f"//div[@class='inventory_item_name'][text()='{item}']")
        name = self.get_element_text(link)
        return name

    @allure.step("Getting description of the item")
    def get_item_description(self, item):
        link = (By.XPATH, f"//div[@class='inventory_item_name'][text()='{item}']/following::div[@class='inventory_item_desc'][1]")
        return self.get_element_text(link)

    @allure.step("Getting price ot the item")
    def get_item_price(self, item):
        link = (By.XPATH, f"//div[@class='inventory_item_name'][text()='{item}']/following::div[@class='inventory_item_price'][1]")
        return self.get_element_text(link)

    @allure.step("Adding item to the cart")
    def add_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART)
        self.do_click(self.ADD_TO_CART)

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.wait_for_element(self.REMOVE_FROM_CART)
        self.do_click(self.REMOVE_FROM_CART)

    @allure.step("Verification of the empty cart")
    def empty_cart(self):
        return self.is_not_visible(self.CART_BADGE)

    @allure.step("Checking cart")
    def check_cart(self):
        self.wait_for_element(self.CART_BADGE)
        return self.get_element_text(self.CART_BADGE)
