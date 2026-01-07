# Содержит локаторы и методы для взаимодействия с главной страницей (для гостя).
from selenium.webdriver.common.by import By
from ui.base_page import BasePage


class IndexPageLocators:
    """Класс с локаторами для главной страницы."""
    LOCATOR_GUEST_WELCOME = (By.CSS_SELECTOR, ".user_greeting h4")


class IndexPageHelper(BasePage):
    """Класс-помощник для работы с главной страницей неавторизованного пользователя."""

    def get_guest_welcome_text(self):
        """Возвращает текст приветствия для гостя."""
        welcome_el = self.find_element(IndexPageLocators.LOCATOR_GUEST_WELCOME, time=5)
        return welcome_el.text