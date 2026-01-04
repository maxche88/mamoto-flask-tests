"""
Файл с тестами конкретного API-модуля.
Проверяет:
коды ответа (200, 401, 404 и т.д.),
структуру JSON-ответа,
корректность данных в ответе.
"""
import pytest
from config.test_settings import ADMIN_EMAIL, ADMIN_PASSWORD

def test_login_success(api_client):
    response = api_client.post("/auth/login", json={
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    })
    assert response.status_code == 200
    assert "access_token" in response.json()