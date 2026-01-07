# Тесты для главной страницы приложения (режим гостя).
import pytest
from ui.pages.index_page import IndexPageHelper


class TestIndexPageGuest:
    """Класс с тестами для неавторизованного пользователя на главной странице."""

    def test_guest_sees_welcome_message(self, browser):
        """
        Проверяет, что неавторизованный пользователь (гость) видит приветствие "Добро пожаловать, Гость!"
        при открытии главной страницы.
        """
        index_page = IndexPageHelper(browser)
        index_page.go_to_site()  # открывает BASE_URL из конфига

        actual_text = index_page.get_guest_welcome_text()
        expected_text = "Добро пожаловать, Гость!"
        assert actual_text == expected_text, f"Ожидалось '{expected_text}', получено: '{actual_text}'"