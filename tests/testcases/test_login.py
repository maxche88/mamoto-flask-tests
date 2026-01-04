import pytest
from tests.pages.login_page import LoginPage
from config.test_settings import ADMIN_EMAIL, ADMIN_PASSWORD


def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    # Пример проверки: после логина — редирект на /dashboard или /
    assert "dashboard" in browser.current_url or browser.current_url.endswith("/")