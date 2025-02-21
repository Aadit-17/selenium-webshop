"""Script to implement class for Books section"""
import time

from selenium.webdriver.common.by import By

from pages.Page import Page


class BooksPage(Page):
    """Class for Books section"""
    FIRST_ITEM = (
        By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/input')
    CART_LINK = (By.LINK_TEXT, "Shopping cart")

    def add_items_to_cart(self):
        """Function to add items to cart"""
        self.click(self.FIRST_ITEM)
        time.sleep(3)

    def go_to_cart(self):
        """Function to go to cart"""
        self.click(self.CART_LINK)
