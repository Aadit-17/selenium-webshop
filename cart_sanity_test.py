"""Main Script to implement Ecommerce website testing"""
import time
from DriverFactory import DriverFactory
from login_credentials import USERNAME, PASSWORD
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from pages.BooksPage import BooksPage


def test_shopping_cart():
    """Function to test Shopping Cart functionality"""
    driver = DriverFactory.get_driver("chrome")
    driver.maximize_window()

    try:
        # Open Website and Login
        login_page = LoginPage(driver)
        login_page.open_page("https://demowebshop.tricentis.com/")
        login_page.login(USERNAME, PASSWORD)
        time.sleep(3)

        # Add an item to cart
        home_page = HomePage(driver)
        home_page.add_items_to_cart()
        time.sleep(3)

        # Go to Books Section
        home_page.go_to_books()
        time.sleep(3)

        # Open Books section and add a book to cart
        books_page = BooksPage(driver)
        books_page.add_items_to_cart()
        time.sleep(3)
        books_page.go_to_cart()

        # Go to Shopping Cart page and remove an item
        cart_page = CartPage(driver)
        cart_page.remove_first_item()
        time.sleep(3)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_cart()
