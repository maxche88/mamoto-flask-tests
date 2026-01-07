# Тесты для сценариев неавторизованного пользователя (гостя).
import pytest
from ui.pages.guest_page import GuestPageHelper


class TestGuestMainPage:
    """Класс с тестами для главной страницы в режиме гостя."""

    def test_guest_sees_welcome_message(self, browser):
        """
        Проверяет, что неавторизованный пользователь (гость) видит приветствие "Добро пожаловать, Гость!"
        при открытии главной страницы.
        """
        guest_page = GuestPageHelper(browser)
        guest_page.go_to_site()

        actual_text = guest_page.get_guest_welcome_text()
        expected_text = "Добро пожаловать, Гость!"
        assert actual_text == expected_text, f"Ожидалось '{expected_text}', получено: '{actual_text}'"


class TestGuestProductInquiry:
    """Класс с позитивными тестами для отправки вопроса о товаре от имени гостя."""

    def test_guest_can_send_question_about_product(self, browser):
        """
        Проверяет, что гость может:
        - перейти на главную страницу,
        - кликнуть по первому товару,
        - открыть форму "Задать вопрос",
        - заполнить её и отправить,
        - увидеть сообщение "Ваш вопрос отправлен!".
        """
        guest_page = GuestPageHelper(browser)

        # 1. Открываем главную страницу
        guest_page.go_to_site()

        # 2. Кликаем по первому товару
        guest_page.click_first_product()

        # 3. Отправляем вопрос
        guest_page.send_question_as_guest(
            name="Гость",
            email="guest@example.com",
            message="Есть ли этот товар в наличии?"
        )

        # 4. Проверяем успешное уведомление
        success_text = guest_page.get_success_alert_text()
        assert success_text == "Ваш вопрос отправлен!", \
            f"Ожидалось 'Ваш вопрос отправлен!', получено: '{success_text}'"