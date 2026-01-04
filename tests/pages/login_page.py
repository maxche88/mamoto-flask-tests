from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "email")          # ← заменить на реальный селектор
    PASSWORD_FIELD = (By.ID, "password")    # ← заменить на реальный селектор
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")  # ← адаптировать

    def open_login_page(self):
        self.driver.get("http://192.168.0.18:5000/login")

    def login(self, email, password):
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)