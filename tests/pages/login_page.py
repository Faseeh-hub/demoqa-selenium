# tests/pages/login_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login")
    LOGOUT_BTN = (By.ID, "submit")

    def open_login(self):
        self.open("https://demoqa.com/login")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        return self.is_visible(self.LOGOUT_BTN)
