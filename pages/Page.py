"""Script to create base Page class"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    """Base page class"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        """Function to open page"""
        self.driver.get(url)

    def get_element(self, locator):
        """Function to get element using locator"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Function to click on an element using locator"""
        self.get_element(locator).click()

    def send_keys(self, locator, text):
        """Function to write text to a locator element"""
        self.get_element(locator).send_keys(text)

    def get_text(self, locator):
        """Function to retrieve text from a locator"""
        return self.get_element(locator).text
