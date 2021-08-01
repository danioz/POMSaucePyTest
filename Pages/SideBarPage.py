import time
import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SideBarPage(BasePage):
    BTN_BURGER_MENU = (By.ID, 'react-burger-menu-btn')
    BTN_LOGOUT = (By.ID, 'logout_sidebar_link')
    BTN_RESET = (By.ID, 'reset_sidebar_link')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Opening burger menu")
    def open_burger_menu(self):
        self.wait_for_element(self.BTN_BURGER_MENU)
        self.do_click(self.BTN_BURGER_MENU)

    @allure.step("Resetting application state")
    def do_reset(self):
        self.wait_for_element(self.BTN_RESET)
        self.do_click(self.BTN_RESET)

    @allure.step("Clicking logout button")
    def click_logout(self):
        self.wait_for_element(self.BTN_LOGOUT)
        self.do_click(self.BTN_LOGOUT)

    @allure.step("Logging out")
    def do_logout(self):
        self.open_burger_menu()
        self.do_reset()
        time.sleep(1)
        self.click_logout()
