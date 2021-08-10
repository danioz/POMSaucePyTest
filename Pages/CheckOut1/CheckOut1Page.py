import allure

from Pages.BasePage import BasePage
from Pages.CheckOut1.elements import Elements

class CheckOutPage_1(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Checkout1 page")
    def get_title(self):
        self.wait_for_element(Elements.TITLE)
        return self.get_element_text(Elements.TITLE)

    @allure.step("Getting inputs from the Checkout1 page")
    def get_inputs(self, name):
        list = []
        self.wait_for_element(Elements.INPUTS_PAGE)
        inputs = self.get_elements(Elements.INPUTS_PAGE)
        for input in inputs:
            attribute = self.get_element_attribute(input, name)
            list.append(attribute)
        return list

    @allure.step("Providing first name")
    def input_first_name(self, first_name):
        self.wait_for_element(Elements.INPUT_FIRST_NAME)
        self.do_send_keys(Elements.INPUT_FIRST_NAME, first_name)

    @allure.step("Providing last name")
    def input_last_name(self, last_name):
        self.wait_for_element(Elements.INPUT_LAST_NAME)
        self.do_send_keys(Elements.INPUT_LAST_NAME, last_name)

    @allure.step("Providing postal code")
    def input_postal_code(self, postal_code):
        self.wait_for_element(Elements.INPUT_POSTAL_CODE)
        self.do_send_keys(Elements.INPUT_POSTAL_CODE, postal_code)

    @allure.step("Clearing first name ")
    def clear_first_name(self):
        self.do_clear_text(Elements.INPUT_FIRST_NAME)

    @allure.step("Clearing last name")
    def clear_last_name(self):
        self.do_clear_text(Elements.INPUT_LAST_NAME)

    @allure.step("Clearing postal code")
    def clear_postal_code(self):
        self.do_clear_text(Elements.INPUT_POSTAL_CODE)

    @allure.step("Getting error message")
    def get_error_message(self):
        self.wait_for_element(Elements.ERROR_MSG)
        return self.get_element_text(Elements.ERROR_MSG)

    @allure.step("Getting error SVG")
    def get_error_svg(self):
        self.wait_for_element(Elements.SVG_ERROR)
        element = self.get_element(Elements.SVG_ERROR)
        return True if element != None else False

    @allure.step("Continue checkout")
    def continue_checkout(self):
        self.wait_for_element(Elements.BTN_CONTINUE)
        self.do_click(Elements.BTN_CONTINUE)
        from Pages.CheckOut2.CheckOut2Page import CheckOutPage_2
        return CheckOutPage_2(self.driver)

    @allure.step("Cancelling checkout")
    def cancel_checkout(self):
        self.wait_for_element(Elements.BTN_CANCEL)
        self.do_click(Elements.BTN_CANCEL)
        from Pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)
