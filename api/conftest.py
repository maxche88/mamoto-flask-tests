"""
Подготовка окружения для API-тестов.
Содержит фикстуру api_client — обёртку над requests.Session, которая:
хранит базовый URL API,
автоматически формирует полный путь к эндпоинту,
может управлять заголовками (например, авторизацией).
"""
import pytest
import requests
from config.test_settings import API_BASE_URL

@pytest.fixture(scope="session")
def api_client():
    """Сессия requests с общими настройками (базовый URL, токены и т.д.)"""
    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()

        def get(self, path, **kwargs):
            return self.session.get(f"{self.base_url}{path}", **kwargs)

        def post(self, path, **kwargs):
            return self.session.post(f"{self.base_url}{path}", **kwargs)

        # можно добавить put, delete и т.д.

    return APIClient(API_BASE_URL)