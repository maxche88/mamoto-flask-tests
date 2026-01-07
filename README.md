# Mamoto Flask — QA Automation Tests

Automated UI tests for the `mamoto-flask-site` web application.

## Setup

1. Python 3.9+
2. Create virtual env:
   ```powershell
   python -m venv venv
   venv\Scripts\activate  # Windows

## Run tests

Все команды выполняются из **корневой директории проекта**.

```bash
# Запуск всех UI-тестов
pytest ui/tests/ -v

# Запуск только тестов входа
pytest ui/tests/test_login.py -v
# Запуск одного конкретного теста
pytest ui/tests/test_index.py::TestIndexPageGuest -v  # Запустить тесты данного класса 
pytest ui/tests/test_login.py::TestLoginPositive::test_login_success_and_welcome_message -v
# Запуск с подробным выводом и возможностью увидеть причину падения
pytest ui/tests/ -v --tb=short
# Запуск без вывода логов от WebDriver Manager
pytest ui/tests/ -v --disable-warnings

# Запуск в headless-режиме (без отображения браузера)
Раскомментируйте строку в ui/conftest.py
options.add_argument("--headless")
