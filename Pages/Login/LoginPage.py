import allure

from Config.config import Test_Data
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BTN_LOGIN = (By.ID, 'login-button')
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")
    INPUTS_PAGE = (By.XPATH, "//input")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Test_Data.BASE_URL)

    @allure.step("Getting title of the Login Page")
    def get_login_page_title(self):
        return self.get_title()

    @allure.step("Providing username")
    def input_username(self, username):
        self.wait_for_element(self.INPUT_USERNAME)
        self.do_send_keys(self.INPUT_USERNAME, username)

    @allure.step("Providing password")
    def input_password(self, password):
        self.wait_for_element(self.INPUT_PASSWORD)
        self.do_send_keys(self.INPUT_PASSWORD, password)

    @allure.step("Clicking login button")
    def click_login(self):
        self.wait_for_element(self.BTN_LOGIN)
        self.do_click(self.BTN_LOGIN)

    @allure.step("Getting error message")
    def get_error_message(self):
        self.wait_for_element(self.ERROR_MSG)
        return self.get_element_text(self.ERROR_MSG)

    @allure.step("Getting all inputs from the Login page")
    def get_inputs(self):
        list = []
        self.wait_for_element(self.INPUTS_PAGE)
        inputs = self.get_elements(self.INPUTS_PAGE)
        for input in inputs:
            attribute = self.get_element_attribute(input)
            list.append(attribute)
        return list

    @allure.step("Logging with the provided username and password")
    def do_login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
