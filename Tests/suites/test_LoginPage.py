import pytest
import allure

import Config.config
from Pages.Inventory.InventoryPage import InventoryPage
from Pages.Login.LoginPage import LoginPage
from Tests.test_base_login import BaseLoginTest
from Config.config import Test_Data


@allure.suite('Smoke tests')
@allure.sub_suite('Smoke tests')
class Test_Smoke(BaseLoginTest):
    expected_url = Config.config.Test_Data.BASE_URL
    expected_title = 'PRODUCTS'

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Verifying login inputs')
    @allure.description('Open login page and verifying all login inputs')
    @pytest.mark.parametrize("expected_inputs", [['user-name', 'password', 'login-button']])
    def test_inputs_on_the_page(self, expected_inputs):
        self.loginPage = LoginPage(self.driver)

        self.loginPage \
            .ASSERT_actual_url(self.expected_url) \
            .ASSERT_page_inputs(expected_inputs)


@allure.suite('Login Test')
@allure.sub_suite('Login Test')
class Test_Login(BaseLoginTest):
    expected_inventory_url = Config.config.Test_Data.INVENTORY_URL
    expected_title = 'PRODUCTS'

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Verifying correct user login procedure')
    @allure.description('Open login page, provide correct login inputs and confirming correct login')
    def test_login(self):
        self.loginPage = LoginPage(self.driver)

        self.loginPage \
            .input_username(Test_Data.STANDARD_USER_NAME) \
            .input_password(Test_Data.PASSWORD) \
            .click_login() \
            .ASSERT_actual_url(self.expected_inventory_url)

        self.inventoryPage \
            .ASSERT_actual_title(self.expected_title)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Verifying locked-out user login procedure')
    @allure.description('Open login page, provide locked-out user login inputs and confirming getting error message')
    def test_locked_user(self):
        self.loginPage = LoginPage(self.driver)
        error_message = "Epic sadface: Sorry, this user has been locked out."

        self.loginPage \
            .input_username(Test_Data.LOCKED_OUT_USER) \
            .input_password(Test_Data.PASSWORD) \
            .click_login() \
            .then() \
            .ASSERT_error_message(error_message)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Verifying no password login procedure')
    @allure.description('Open login page, provide only user login and confirming getting error message')
    def test_no_password(self):
        self.loginPage = LoginPage(self.driver)
        error_message = "Epic sadface: Password is required"

        self.loginPage \
            .input_username(Test_Data.STANDARD_USER_NAME) \
            .click_login() \
            .then() \
            .ASSERT_error_message(error_message)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Verifying no username login procedure')
    @allure.description('Open login page, provide only user password and confirming getting error message')
    def test_no_username(self):
        self.loginPage = LoginPage(self.driver)
        error_message = "Epic sadface: Username is required"

        self.loginPage \
            .input_password(Test_Data.PASSWORD) \
            .click_login() \
            .then() \
            .ASSERT_error_message(error_message)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Verifying not correct login procedure')
    @allure.description('Open login page, provide incorrect credentials and confirming getting error message')
    def test_not_match_user(self):
        self.loginPage = LoginPage(self.driver)
        error_message = "Epic sadface: Username and password do not match any user in this service"

        self.loginPage \
            .input_username('admin') \
            .input_password('password') \
            .click_login() \
            .then() \
            .ASSERT_error_message(error_message)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Verifying problem user login procedure')
    @allure.description('Open login page, provide problem-user credentials and confirming login')
    def test_problem_user(self):
        self.loginPage = LoginPage(self.driver)

        self.loginPage \
            .input_username(Test_Data.PROBLEM_USER) \
            .input_password(Test_Data.PASSWORD) \
            .click_login() \
            .then()

        self.inventoryPage \
            .ASSERT_actual_title(self.expected_title)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Verifying getting error messages')
    @allure.description('Open login page, provide incorrect credentials and confirming getting error messages')
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
        self.inventoryPage = InventoryPage(self.driver)

        self.loginPage \
            .input_username(username) \
            .input_password(password) \
            .click_login() \
            .then() \
            .ASSERT_error_message(error_message)
