import allure

from Pages.BasePage import BasePage
from Pages.Inventory.elements import Elements
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Inventory page")
    def get_title(self):
        title = self.get_element_text(Elements.TITLE)
        return title

    @allure.step("Entering cart")
    def enter_cart(self):
        self.do_click(Elements.CART)
        return self

    @allure.step("Adding Sauce Labs Backpack")
    def add_backpack(self):
        self.do_click(Elements.ADD_BACKPACK)
        return self

    @allure.step("Adding Sauce Labs Bike Light")
    def add_bike_light(self):
        self.do_click(Elements.ADD_BIKE_LIGHT)
        return self

    @allure.step("Adding Sauce Labs Bolt T-Shirt")
    def add_t_shirt(self):
        self.do_click(Elements.ADD_T_SHIRT)
        return self

    @allure.step("Adding Sauce Labs Fleece Jacket")
    def add_jacket(self):
        self.do_click(Elements.ADD_JACKET)
        return self

    @allure.step("Adding Sauce Labs Onesie")
    def add_onesie(self):
        self.do_click(Elements.ADD_ONESIE)
        return self

    @allure.step("Adding Test.allTheThings() T-Shirt (Red)")
    def add_red_t_shirt(self):
        self.do_click(Elements.ADD_RED_T_SHIRT)
        return self

    @allure.step("Removing Sauce Labs Backpack")
    def remove_backpack(self):
        self.do_click(Elements.REMOVE_BACKPACK)
        return self

    @allure.step("Removing Sauce Labs Bike Light")
    def remove_bike_light(self):
        self.do_click(Elements.REMOVE_BIKE_LIGHT)
        return self

    @allure.step("Removing Sauce Labs Bolt T-Shirt")
    def remove_t_shirt(self):
        self.do_click(Elements.REMOVE_T_SHIRT)
        return self

    @allure.step("Removing Sauce Labs Fleece Jacket")
    def remove_jacket(self):
        self.do_click(Elements.REMOVE_JACKET)
        return self

    @allure.step("Removing Sauce Labs Onesie")
    def remove_onesie(self):
        self.do_click(Elements.ADD_ONESIE)
        return self

    @allure.step("Removing Test.allTheThings() T-Shirt (Red)")
    def remove_red_t_shirt(self):
        self.do_click(Elements.REMOVE_RED_T_SHIRT)
        return self

    @allure.step("Adding item with link")
    def add_item_link(self, item):
        link = (By.XPATH, f"//div[@class='inventory_item_name'][text()='{item}']")
        self.do_click(link)
        from Pages.Item.ItemPage import ItemPage
        return ItemPage(self.driver)

    @allure.step("Getting name of the item")
    def get_item_name(self, item):
        link = (By.XPATH, f"//div[@class='inventory_item_name'][text()='{item}']")
        name = self.get_element_text(link)
        return name

    @allure.step("Getting description of the item")
    def get_item_description(self, item):
        link = (By.XPATH,
                f"//div[@class='inventory_item_name'][text()='{item}']/following::div[@class='inventory_item_desc'][1]")
        return self.get_element_text(link)

    @allure.step("Getting price ot the item")
    def get_item_price(self, item):
        link = (By.XPATH,
                f"//div[@class='inventory_item_name'][text()='{item}']/following::div[@class='inventory_item_price'][1]")
        return self.get_element_text(link)

    @allure.step("Adding item to the cart")
    def add_to_cart(self):
        self.do_click(Elements.ADD_TO_CART)
        return self

    @allure.step("Removing item from the cart")
    def remove_from_cart(self):
        self.do_click(Elements.REMOVE_FROM_CART)
        return self

    @allure.step("Verification of the empty cart")
    def empty_cart(self):
        return self.is_not_visible(Elements.CART_BADGE)

    @allure.step("Checking cart")
    def check_cart(self):
        return self.get_element_text(Elements.CART_BADGE)

    @allure.step("Adding '{1}' to the cart")
    def add_item_to_cart(self, item):
        element = (By.XPATH, f"//button[contains(@id,'add-to-cart') and contains(@id,'{item}')]")
        self.do_click(element)
        return self

    @allure.step("Removing '{1}' from the cart")
    def remove_item_from_cart(self, item):
        element = (By.XPATH, f"//button[contains(@id,'remove') and contains(@id,'{item}')]")
        self.do_click(element)
        return self

    @allure.step("Returning list of available items")
    def list_of_available_item(self):
        item_list = []
        items = Elements.ADD_TO_CART
        self.wait_for_element(items)
        elements = self.get_all_elements(items)
        for element in elements:
            id = str(self.get_element_attribute(element)[23:])
            item_list.append(id)
        return item_list
