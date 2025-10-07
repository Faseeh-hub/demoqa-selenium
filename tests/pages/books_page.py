# tests/pages/books_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By

class BooksPage(BasePage):
    SEARCH = (By.ID, "searchBox")
    FIRST_BOOK = (By.CSS_SELECTOR, ".rt-tr-group .mr-2")
    ADD_BTN = (By.XPATH, "//button[text()='Add To Your Collection']")
    PROFILE = (By.ID, "gotoProfile")

    def open_books(self):
        self.open("https://demoqa.com/books")

    def search_book(self, text):
        self.type(self.SEARCH, text)

    def select_first(self):
        self.click(self.FIRST_BOOK)

    def add_to_collection(self):
        self.click(self.ADD_BTN)

    def go_profile(self):
        self.click(self.PROFILE)
