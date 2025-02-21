"""Script to implement class for Home Page"""
import time

from selenium.webdriver.common.by import By

from pages.Page import Page


class HomePage(Page):
    """Class for Home Page of Ecommerce Website"""
    FIRST_ITEM = (By.XPATH, "(//input[@value='Add to cart'])[2]")
    BOOKS_LINK = (
        By.XPATH,
        '/html/body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ul/li[1]/a')

    def add_items_to_cart(self):
        """Script to add an item to cart"""
        self.click(self.FIRST_ITEM)
        time.sleep(3)

    def go_to_books(self):
        """Script to switch over to books section"""
        self.click(self.BOOKS_LINK)
