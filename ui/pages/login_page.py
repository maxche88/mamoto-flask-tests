# Содержит локаторы элементов формы входа и бизнес-методы для взаимодействия с ней.
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from ui.base_page import BasePage


class LoginPageLocators:
    """Класс с локаторами для страницы входа."""
    LOCATOR_USERNAME_FIELD = (By.ID, "username")
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_LOGIN_BUTTON = (By.ID, "submitBtn")
    LOCATOR_ERROR_MESSAGE = (By.ID, "errorMessages")
    LOCATOR_WELCOME_HEADER = (By.CSS_SELECTOR, ".user_greeting h4")


class LoginPageHelper(BasePage):
    """Класс-помощник для выполнения действий на странице входа."""

    def enter_username(self, word):
        """Находит поле ввода имени пользователя, очищает его и вводит переданный текст."""
        self.enter_text(LoginPageLocators.LOCATOR_USERNAME_FIELD, word)

    def enter_password(self, word):
        """Находит поле ввода пароля, очищает его и вводит переданный текст."""
        self.enter_text(LoginPageLocators.LOCATOR_PASSWORD_FIELD, word)

    def click_login_button(self):
        """Находит кнопку 'Войти' и выполняет по ней клик."""
        self.click_element(LoginPageLocators.LOCATOR_LOGIN_BUTTON)

    def login(self, username, password):
        """Выполняет полный сценарий входа: переход на страницу, ввод данных, нажатие кнопки."""
        self.go_to_site("/login")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_text(self):
        """
        Пытается найти сообщение об ошибке на странице.
        Если элемент не появляется в течение 3 секунд — возвращает пустую строку.
        """
        try:
            error_el = self.find_element(LoginPageLocators.LOCATOR_ERROR_MESSAGE, time=3)
            return error_el.text.strip()
        except TimeoutException:
            return ""

    def get_welcome_text(self):
        """Возвращает текст приветственного сообщения после успешного входа."""
        welcome_el = self.find_element(LoginPageLocators.LOCATOR_WELCOME_HEADER, time=5)
        return welcome_el.text