import pytest
from ui.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from config.test_settings import USER_NAME, USER_PASSWORD


class TestLoginPositive:
    def test_login_success_and_welcome_message(self, browser):
        """Позитивный: успешный вход и приветствие с именем пользователя."""
        login_page = LoginPage(browser)
        login_page.login(USER_NAME, USER_PASSWORD)

        WELCOME_HEADER = (By.CSS_SELECTOR, ".user_greeting h4")
        actual_text = login_page.find_element(WELCOME_HEADER).text
        expected_text = f"Добро пожаловать, {USER_NAME}!"
        assert actual_text == expected_text, f"Ожидалось '{expected_text}', получено: '{actual_text}'"


class TestLoginNegative:
    def test_login_empty_password_shows_error(self, browser):
        """Негативный: пароль не введён (username введён)."""
        login_page = LoginPage(browser)
        login_page.open(login_page.PAGE_URL)
        login_page.enter_username(USER_NAME)
        login_page.click_login()
        
        assert browser.current_url.rstrip('/') == login_page.PAGE_URL
        assert login_page.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_empty_username_shows_error(self, browser):
        """Негативный: username не введён (пароль введён)."""
        login_page = LoginPage(browser)
        login_page.open(login_page.PAGE_URL)
        login_page.enter_password(USER_PASSWORD)
        login_page.click_login()
        
        assert browser.current_url.rstrip('/') == login_page.PAGE_URL
        assert login_page.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_both_fields_empty_shows_error(self, browser):
        """Негативный: оба поля пустые."""
        login_page = LoginPage(browser)
        login_page.open(login_page.PAGE_URL)
        login_page.click_login()
        
        assert browser.current_url.rstrip('/') == login_page.PAGE_URL
        assert login_page.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_invalid_credentials_show_error(self, browser):
        """Негативный: заведомо неверные учётные данные."""
        login_page = LoginPage(browser)
        login_page.open(login_page.PAGE_URL)
        login_page.enter_username("nonexistent_user_12345")
        login_page.enter_password("wrong_pass_67890")
        login_page.click_login()
        
        assert browser.current_url.rstrip('/') == login_page.PAGE_URL
        assert login_page.get_error_text() == "Неверное имя пользователя или пароль"

    def test_login_sql_injection_attempt_fails(self, browser):
        """Негативный: попытка SQL-инъекции в поле username."""
        login_page = LoginPage(browser)
        login_page.open(login_page.PAGE_URL)
        login_page.enter_username("admin'--")
        login_page.enter_password("any_password")
        login_page.click_login()
        
        assert browser.current_url.rstrip('/') == login_page.PAGE_URL
        assert login_page.get_error_text() == "Неверное имя пользователя или пароль"