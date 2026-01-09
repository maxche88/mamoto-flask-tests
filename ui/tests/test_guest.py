# Тесты для сценариев неавторизованного пользователя (гостя).
import pytest
from ui.pages.guest_page import GuestPageHelper
from config.test_settings import USER_NAME, USER_EMAIL


class TestGuestPositive:
    """Класс с тестами для доступных страниц пользователя с ролью гость (не авторизированный)."""

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

    def test_guest_can_send_message_from_main_page(self, browser):
        """
        Проверяет, что гость может отправить сообщение через форму 'Написать нам' на главной странице:
        - нажимает на вкладку 'Написать нам',
        - заполняет имя, email, выбирает категорию и текст сообщения,
        - нажимает 'Отправить',
        - видит уведомление об успешной отправке.
        """
        guest_page = GuestPageHelper(browser)
        guest_page.go_to_site()  # открываем главную страницу

        guest_page.send_message_from_main_page(
            name=USER_NAME,
            email=USER_EMAIL,
            category="2",  # Например, "Технический"
            message="Тестовое сообщение с главной страницы."
        )

        success_text = guest_page.get_success_text()
        expected_text = "Ваше обращение отправлено."
        assert success_text == expected_text, f"Ожидалось '{expected_text}', получено: '{success_text}'"

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
            name=USER_NAME,
            email=USER_EMAIL,
            message="Есть ли этот товар в наличии?"
        )

        # 4. Проверяем успешное уведомление
        success_text = guest_page.get_success_text()
        assert success_text == "Ваш вопрос отправлен!", \
            f"Ожидалось 'Ваш вопрос отправлен!', получено: '{success_text}'"