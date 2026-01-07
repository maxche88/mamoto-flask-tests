# Содержит позитивные и негативные тесты для сценария входа в систему.
import pytest
from ui.pages.login_page import LoginPageHelper
from config.test_settings import USER_NAME, USER_PASSWORD


class TestLoginPositive:
    """Класс с позитивными тестами: проверка успешного входа."""

    def test_login_success_and_welcome_message(self, browser):
        """
        Проверяет, что при вводе корректных учётных данных пользователь попадает на главную страницу,
        и отображается приветственное сообщение с его именем.
        """
        testpage = LoginPageHelper(browser)
        testpage.login(USER_NAME, USER_PASSWORD)

        actual_text = testpage.get_welcome_text()
        expected_text = f"Добро пожаловать, {USER_NAME}!"
        assert actual_text == expected_text, f"Ожидалось '{expected_text}', получено: '{actual_text}'"


class TestLoginNegative:
    """Класс с негативными тестами: проверка реакции системы на некорректные данные."""

    def test_login_empty_password_shows_error(self, browser):
        """Проверяет, что ошибка отображается, если пароль не введён."""
        testpage = LoginPageHelper(browser)
        testpage.go_to_site("/login")
        testpage.enter_username(USER_NAME)
        testpage.click_login_button()

        assert browser.current_url.rstrip('/') == testpage.base_url + "/login"
        assert testpage.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_empty_username_shows_error(self, browser):
        """Проверяет, что ошибка отображается, если имя пользователя не введено."""
        testpage = LoginPageHelper(browser)
        testpage.go_to_site("/login")
        testpage.enter_password(USER_PASSWORD)
        testpage.click_login_button()

        assert browser.current_url.rstrip('/') == testpage.base_url + "/login"
        assert testpage.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_both_fields_empty_shows_error(self, browser):
        """Проверяет, что ошибка отображается, если оба поля пусты."""
        testpage = LoginPageHelper(browser)
        testpage.go_to_site("/login")
        testpage.click_login_button()

        assert browser.current_url.rstrip('/') == testpage.base_url + "/login"
        assert testpage.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_invalid_credentials_show_error(self, browser):
        """Проверяет, что ошибка отображается при вводе заведомо неверных данных."""
        testpage = LoginPageHelper(browser)
        testpage.go_to_site("/login")
        testpage.enter_username("nonexistent_user_12345")
        testpage.enter_password("wrong_pass_67890")
        testpage.click_login_button()

        assert browser.current_url.rstrip('/') == testpage.base_url + "/login"
        assert testpage.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_sql_injection_attempt_fails(self, browser):
        """Проверяет, что попытка SQL-инъекции блокируется и приводит к ошибке."""
        testpage = LoginPageHelper(browser)
        testpage.go_to_site("/login")
        testpage.enter_username("admin'--")
        testpage.enter_password("any_password")
        testpage.click_login_button()

        assert browser.current_url.rstrip('/') == testpage.base_url + "/login"
        assert testpage.get_error_text() == "Неверное имя пользователя или пароль"