import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckOutPage_Finish(BasePage):
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_BACK_HOME = (By.ID, 'back-to-products')
    H2_COMPLETE_ORDER = (By.CSS_SELECTOR, '.complete-header')
    COMPLETE_TEXT = (By.CSS_SELECTOR, '.complete-text')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the Checkout Finish page")
    def get_title(self):
        self.wait_for_element(self.TITLE)
        title = self.get_element_text(self.TITLE)
        return title

    @allure.step("Checking url of the Checkout Finish page")
    def check_url(self):
        return self.get_current_url()

    @allure.step("Getting checkout header")
    def get_checkout_header(self):
        self.wait_for_element(self.H2_COMPLETE_ORDER)
        text = self.get_element_text(self.H2_COMPLETE_ORDER)
        return text

    @allure.step("Getting checkout message")
    def get_checkout_message(self):
        self.wait_for_element(self.COMPLETE_TEXT)
        text = self.get_element_text(self.COMPLETE_TEXT)
        return text

    @allure.step("Getting back home")
    def go_back_home(self):
        self.wait_for_element(self.BTN_BACK_HOME)
        self.do_click(self.BTN_BACK_HOME)
