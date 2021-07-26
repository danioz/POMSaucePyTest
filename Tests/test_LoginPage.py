import pytest
import allure

import Config.config
from Pages.LoginPage import LoginPage
from Tests.test_base_login import BaseLoginTest
from Config.config import Test_Data


class Test_Smoke(BaseLoginTest):
    expected_url = Config.config.Test_Data.BASE_URL

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("expected_inputs", [['user-name', 'password', 'login-button']])
    def test_inputs_on_the_page(self, expected_inputs):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.check_url() == self.expected_url
        current_inputs = self.loginPage.get_inputs()
        assert current_inputs == expected_inputs


class Test_Login(BaseLoginTest):
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username(Test_Data.STANDARD_USER_NAME)
        self.loginPage.input_password(Test_Data.PASSWORD)
        self.loginPage.click_login()
        assert self.inventoryPage.get_title() == 'PRODUCTS'
        assert self.inventoryPage.check_url() == self.expected_inventory_url

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('....')
    @allure.description('...')
    def test_locked_user(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username(Test_Data.LOCKED_OUT_USER)
        self.loginPage.input_password(Test_Data.PASSWORD)
        self.loginPage.click_login()
        assert self.loginPage.get_error_message() == "Epic sadface: Sorry, this user has been locked out."

    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_password(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username(Test_Data.STANDARD_USER_NAME)
        self.loginPage.click_login()
        assert self.loginPage.get_error_message() == "Epic sadface: Password is required"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_username(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_password(Test_Data.PASSWORD)
        self.loginPage.click_login()
        assert self.loginPage.get_error_message() == "Epic sadface: Username is required"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_not_match_user(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username('admin')
        self.loginPage.input_password('password')
        self.loginPage.click_login()
        assert self.loginPage.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_problem_user(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username(Test_Data.PROBLEM_USER)
        self.loginPage.input_password(Test_Data.PASSWORD)
        self.loginPage.click_login()
        assert self.inventoryPage.get_title() == 'PRODUCTS'

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username, password, error_message",
                             [['locked_out_user', 'secret_sauce',
                               'Epic sadface: Sorry, this user has been locked out.'],
                              ['standard_user', '', 'Epic sadface: Password is required'],
                              ['', 'secret_sauce', 'Epic sadface: Username is required'],
                              ['username', 'password',
                               'Epic sadface: Username and password do not match any user in this service']
                              ])
    def test_failed_login_scenario(self, username, password, error_message):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username(username)
        self.loginPage.input_password(password)
        self.loginPage.click_login()
        assert self.loginPage.get_error_message() == error_message