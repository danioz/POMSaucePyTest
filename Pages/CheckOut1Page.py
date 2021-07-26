import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckOutPage_1(BasePage):
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_CONTINUE = (By.ID, 'continue')
    BTN_CANCEL = (By.ID, 'cancel')
    INPUT_FIRST_NAME = (By.ID, 'first-name')
    INPUT_LAST_NAME = (By.ID, 'last-name')
    INPUT_POSTAL_CODE = (By.ID, 'postal-code')
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")
    SVG_ERROR = (By.XPATH, "//*[@data-icon='times-circle']")
    INPUTS_PAGE = (By.XPATH, "//div[@class='form_group']/input")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Checkout1 page")
    def get_title(self):
        self.wait_for_element(self.TITLE)
        title = self.get_element_text(self.TITLE)
        return title

    @allure.step("Checking url of the Checkout1 page")
    def check_url(self):
        return self.get_current_url()

    @allure.step("Getting inputs from the Checkout1 page")
    def get_inputs(self, name):
        list = []
        self.wait_for_element(self.INPUTS_PAGE)
        inputs = self.get_elements(self.INPUTS_PAGE)
        for input in inputs:
            attribute = self.get_element_attribute(input, name)
            list.append(attribute)
        return list

    @allure.step("Providing first name")
    def input_first_name(self, first_name):
        self.wait_for_element(self.INPUT_FIRST_NAME)
        self.do_send_keys(self.INPUT_FIRST_NAME, first_name)

    @allure.step("Providing last name")
    def input_last_name(self, last_name):
        self.wait_for_element(self.INPUT_LAST_NAME)
        self.do_send_keys(self.INPUT_LAST_NAME, last_name)

    @allure.step("Providing postal code")
    def input_postal_code(self, postal_code):
        self.wait_for_element(self.INPUT_POSTAL_CODE)
        self.do_send_keys(self.INPUT_POSTAL_CODE, postal_code)

    @allure.step("Clearing first name ")
    def clear_first_name(self):
        self.do_clear_text(self.INPUT_FIRST_NAME)

    @allure.step("Clearing last name")
    def clear_last_name(self):
        self.do_clear_text(self.INPUT_LAST_NAME)

    @allure.step("Clearing postal code")
    def clear_postal_code(self):
        self.do_clear_text(self.INPUT_POSTAL_CODE)

    @allure.step("Getting error message")
    def get_error_message(self):
        self.wait_for_element(self.ERROR_MSG)
        text = self.get_element_text(self.ERROR_MSG)
        return text

    @allure.step("Getting error SVG")
    def get_error_svg(self):
        self.wait_for_element(self.SVG_ERROR)
        element = self.get_element(self.SVG_ERROR)
        return True if element != None else False

    @allure.step("Continue checkout")
    def continue_checkout(self):
        self.wait_for_element(self.BTN_CONTINUE)
        self.do_click(self.BTN_CONTINUE)

    @allure.step("Cancelling checkout")
    def cancel_checkout(self):
        self.wait_for_element(self.BTN_CANCEL)
        self.do_click(self.BTN_CANCEL)
