import allure

from Config.config import Test_Data
from Pages.BasePage import BasePage
from Pages.Login.elements import Elements


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Getting title of the Login Page")
    def get_login_page_title(self):
        return self.get_title()

    @allure.step("Providing username: '{1}'")
    def input_username(self, username):
        self.do_send_keys(Elements.INPUT_USERNAME, username)
        return self

    @allure.step("Providing password: '{1}'")
    def input_password(self, password):
        self.do_send_keys(Elements.INPUT_PASSWORD, password)
        return self

    @allure.step("Clicking login button")
    def click_login(self):
        self.do_click(Elements.BTN_LOGIN)
        return self

    @allure.step("Getting error message")
    def get_error_message(self):
        return self.get_element_text(Elements.ERROR_MSG)

    @allure.step("Getting all inputs from the Login page")
    def get_inputs(self):
        list = []
        inputs = self.get_all_elements(Elements.INPUTS_PAGE)
        for input in inputs:
            attribute = self.get_element_attribute(input)
            list.append(attribute)
        return list

    @allure.step("Logging with the provided username: '{1}' and password: '{2}'")
    def do_login(self, username, password):
        self.input_username(username)\
            .input_password(password)\
            .click_login()
        from Pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)

    @allure.step("Validating text of message error: '{1}'")
    def ASSERT_error_message(self, error_message):
        assert self.get_error_message() == error_message
        return self

    @allure.step("Validating actual url")
    def ASSERT_actual_url(self, expected_url):
        assert self.get_actual_url() == expected_url
        return self

    @allure.step("Validating page inputs'")
    def ASSERT_page_inputs(self, expected_inputs):
        assert self.get_inputs() == expected_inputs
        return self
