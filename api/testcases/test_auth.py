"""
Файл с тестами конкретного API-модуля.
Проверяет:
коды ответа (200, 401, 404 и т.д.),
структуру JSON-ответа,
корректность данных в ответе.
"""
import pytest
from config.test_settings import USER_NAME, USER_PASSWORD

def test_login_success(api_client):
    response = api_client.post("/auth/login", json={
        "email": USER_NAME,
        "password": USER_PASSWORD
    })
    assert response.status_code == 200
    assert "access_token" in response.json()