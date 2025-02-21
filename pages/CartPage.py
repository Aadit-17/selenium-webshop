"""Script to implement class for Shopping Cart page"""
import time

from selenium.webdriver.common.by import By

from pages.Page import Page


class CartPage(Page):
    """Class for Shopping Cart page"""
    REMOVE_ITEM = (By.NAME, "removefromcart")
    UPDATE_CART_BUTTON = (By.NAME, "updatecart")

    def remove_first_item(self):
        """Function to remove item from shopping cart and update it"""
        time.sleep(3)
        self.click(self.REMOVE_ITEM)
        self.click(self.UPDATE_CART_BUTTON)
