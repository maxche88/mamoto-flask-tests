# Форма входа. Содержит локаторы (селекторы полей) и бизнес-метод login().

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = "http://192.168.0.18:5000/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submitBtn")
    ERROR_MESSAGE = (By.ID, "errorMessages")
    
    def enter_username(self, username: str):
        """Ввести username."""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """Ввести пароль."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Нажать кнопку 'Войти'."""
        self.click_element(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Выполнить полный сценарий входа."""
        self.open(self.PAGE_URL)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_text(self) -> str:
        """Возвращает текст сообщения об ошибке, если оно отображается. Иначе — пустая строка."""
        try:
            error_element = self.find_element(self.ERROR_MESSAGE)
            return error_element.text.strip()
        except TimeoutException:
            return ""