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

    @allure.step("Checking url of the page")
    # to nie jest checking, tylko get current page url
    def check_url(self):
        return self.driver.current_url

    def wait_for_element(self, by_locator, timeout=10, pollFrequency=0.5):
        # generalna uwaga co do tych metod z base class. fajnie ze sa, ale za bardzo skomplikowane
        # bardzo duzo z tego jest juz generalnie zaimplementowane w samych metodach. Poczytaj dokumentacje
        # i selenium api. Jezeli webdriverwait sie wywala to juz samo z siebie wywala exception
        # ma tez cos takiego jak parametr "message" gdzie mozesz wpisac jaki blad bedzie wypisywany dla uzytkownika

        element = None
        try:
            self.log.info("Waiting for maximum " + str(timeout) + " seconds for element")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
            # nie wiem czemu sa te ignored exceptions skoro i tak mamy czekanie na element po 
            # visibility. patrz opis metody - jezeli nie spelnione rzuca exception w stylu:
            # element not visible exception
            # ta metoda powinna sie bardziej nazywac wait_until_element_visible - wiadomo o co chodzi wtedy
            
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located(by_locator))
            self.log.info(f"Element {by_locator} appeared on the page")
        except:
            self.log.error(f"Element {by_locator} NOT appeared on the page in {timeout} seconds")
            self.screenshot_allure()
            raise AssertionError(f"Element {by_locator} NOT appeared on the page in {timeout} seconds")
        return element

    # skrocona funkcjonalna wersja bylaby w stylu:
    # w podobnym stylu moga byc inne czekajace na inne warunki
    def wait_until_element_not_visible(self, wait_time, *locator, error_message=''):
        return WebDriverWait(self, wait_time).until(
            EC.invisibility_of_element(locator),
            message=f'{error_message}\n'
        )

    def get_element(self, by_locator):
        element = None
        try:
            self.wait_for_element(by_locator)
        except:
            self.log.error(f"Element {by_locator} NOT got")
            self.screenshot_allure()
            raise AssertionError(f"Element {by_locator} NOT got")
        return self.driver.find_element(by_locator[0], by_locator[1])

    # ta metoda nie ma sensu - uzywa wait_for_element, gdzie mowa o get_elements
    # powinna raczej uzywac czegos w rodzaju wait_for_elements
    def get_elements(self, by_locator):
        elements = None
        try:
            self.wait_for_element(by_locator)
        except:
            self.log.error(f"Elements {by_locator} NOT got")
            self.screenshot_allure()
            raise AssertionError(f"Elements {by_locator} NOT got")
        return self.driver.find_elements(by_locator[0], by_locator[1])

    # podobnie, try/except niepotrzebne zostanie rzucone w przypadku nie znalezienia elementu
    # raise assertions w ogole nie potrzebne
    # powinien byc to bardziej helper w stylu "fill_field"- find_element, send_keys
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
        # to czesto nie dziala w rzeczywistosci
        element.clear()

    # wszedzie podobnie try/except do wywalenia
    # dodatkowa uzyteczna metoda do wykorzystania to wait and click - czyli wait until clickable and click
    def do_click(self, by_locator):
        element = None
        try:
            element = self.get_element(by_locator)
            element.click()
            self.log.info(f"Element: {by_locator} was clicked")
        except:
            self.log.error(f"Element: {by_locator} was NOT clicked")
            self.screenshot_allure()
            raise AssertionError(f"Element: {by_locator} was NOT clicked")

    def get_element_text(self, by_locator):
        element = None
        text = None
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
            text = None
        return text

    def get_element_attribute(self, element, name='id'):
        attribute = None
        try:
            attribute = element.get_attribute(name)
            self.log.info(f"Attribute '{attribute}' for attribute name: '{name}' was found")
        except:
            self.log.error(f"Locator: {name} NOT found")
            self.screenshot_allure()
            raise AssertionError(f"Locator: {name} NOT found")
        return attribute

    # dobra nazwa, ale za duzo tzw. boilerplate. duplikacja, powinno sie wziac metode ktora spradza
    # na invisibility i na tej podstawie zwracac true/false
    def is_not_visible(self, by_locator):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            flag = wait.until(EC.invisibility_of_element_located(by_locator))
            self.log.info(f"Element {by_locator} disappeared from the page")
        except:
            # pass
            self.log.error(f"Locator: {by_locator} did NOT disappear")
            self.screenshot_allure()
            raise AssertionError("Locator: {by_locator} did NOT disappear")
        return flag

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.log.info(f"The locator: {by_locator} is visible")
        return bool(element)

    # wydaje mi sie ze .until zwraca element w przypadku znalezienia, wtedy zamienilbym to na cos takiego
    def get_title(self):
        return WebDriverWait(self.driver, 10).until(EC.title_is)


    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")
