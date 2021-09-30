import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
import Utils.custom_logger as cl
import logging


class BasePage:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot_allure(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='FAIL', attachment_type=AttachmentType.PNG)

    @allure.step("Getting url of the page")
    def get_actual_url(self):
        return self.driver.current_url

    def visible(self, by_locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.5).\
                until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def clickable(self, by_locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.5). \
                until(EC.element_to_be_clickable(by_locator))
            return True
        except:
            return False

    def wait_for_element(self, by_locator, timeout=10):
        if self.visible(by_locator, timeout):
            self.log.info(f"Element {by_locator} appeared on the page")
            return self
        raise AssertionError(f"Element {by_locator} NOT appeared on the page in {timeout} seconds")

    def wait_for_element_to_be_clickable(self, by_locator, timeout=10):
        if self.clickable(by_locator, timeout):
            self.log.info(f"Element {by_locator} clickable on the page")
            return self
        if self.visible(by_locator):
            raise AssertionError(f"Element {by_locator} NOT click-able on the page in {timeout} seconds")
        raise AssertionError(f"Element {by_locator} NOT appeared on the page in {timeout} seconds")

    def get_element(self, by_locator, timeout=10):
        self.wait_for_element(by_locator, timeout)
        return self.driver.find_element(by_locator[0], by_locator[1])

    def get_all_elements(self, by_locator, timeout=10):
        self.wait_for_element(by_locator, timeout)
        return self.driver.find_elements(by_locator[0], by_locator[1])

    def do_send_keys(self, by_locator, text):
        try:
            element = self.get_element(by_locator)
            element.send_keys(text)
            self.log.info(f"An input '{text}' typed into: {by_locator}")
        except:
            self.log.error(f"An exception occured while typing an input into: {by_locator}")
            self.screenshot_allure()
            raise AssertionError(f"An exception occured while typing an input into: {by_locator}")

    def do_clear_text(self, by_locator):
        element = self.get_element(by_locator)
        element.clear()

    def do_click(self, by_locator):
        self.wait_for_element_to_be_clickable(by_locator)
        try:
            self.get_element(by_locator).click()
            self.log.info(f"Element: {by_locator} was clicked")
        except:
            self.log.error(f"Element: {by_locator} was NOT clicked")
            self.screenshot_allure()
            raise AssertionError(f"Element: {by_locator} was NOT clicked")

    def get_element_text(self, by_locator):
        try:
            element = self.get_element(by_locator)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
                self.log.info(f"Text '{text}' at the {by_locator} was found")
        except:
            self.log.error(f"Failed to find TEXT on locator: {by_locator}")
            self.screenshot_allure()
            raise AssertionError(f"Failed to find TEXT on locator: {by_locator}")
        return text

    def get_element_attribute(self, element, name='id'):
        self.log.info(f"Attribute for attribute name: '{name}' was found")
        return element.get_attribute(name)

    def is_not_visible(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.5).\
                until(EC.invisibility_of_element_located(by_locator))
            self.log.info(f"Element {by_locator} disappeared from the page")
        except:
            self.log.error(f"Locator: {by_locator} did NOT disappear")
            self.screenshot_allure()
            raise AssertionError("Locator: {by_locator} did NOT disappear")
            return False
        return True

    def get_title(self):
        WebDriverWait(self.driver, 10).until(EC.title_is)
        self.log.info("Found the title of the page: ")
        return self.driver.title

    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")
