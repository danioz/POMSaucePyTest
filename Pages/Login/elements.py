from selenium.webdriver.common.by import By


class Elements:
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BTN_LOGIN = (By.ID, 'login-button')
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")
    INPUTS_PAGE = (By.XPATH, "//input")
