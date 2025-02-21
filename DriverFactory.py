"""Driver Factory to select driver based on browser type"""
from selenium import webdriver


class DriverFactory:
    """Class to define browser selection"""
    @staticmethod
    def get_driver(browser="chrome"):
        """Function to select browser"""
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser: Use 'chrome' or 'firefox'")
