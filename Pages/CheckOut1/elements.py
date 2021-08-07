from selenium.webdriver.common.by import By


class Elements:
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_CONTINUE = (By.ID, 'continue')
    BTN_CANCEL = (By.ID, 'cancel')
    INPUT_FIRST_NAME = (By.ID, 'first-name')
    INPUT_LAST_NAME = (By.ID, 'last-name')
    INPUT_POSTAL_CODE = (By.ID, 'postal-code')
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")
    SVG_ERROR = (By.XPATH, "//*[@data-icon='times-circle']")
    INPUTS_PAGE = (By.XPATH, "//div[@class='form_group']/input")
