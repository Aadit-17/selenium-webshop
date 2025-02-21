"""Script to implement login functionality on Login Page"""
from selenium.webdriver.common.by import By
from pages.Page import Page


class LoginPage(Page):
    """Class for login page"""
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log in']")

    def login(self, username, password):
        """Function to log in to website"""
        self.click(self.LOGIN_LINK)
        self.send_keys(self.EMAIL_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
