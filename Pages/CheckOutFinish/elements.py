from selenium.webdriver.common.by import By


class Elements:
    TITLE = (By.XPATH, "//span[@class='title']")
    BTN_BACK_HOME = (By.ID, 'back-to-products')
    H2_COMPLETE_ORDER = (By.CSS_SELECTOR, '.complete-header')
    COMPLETE_TEXT = (By.CSS_SELECTOR, '.complete-text')
