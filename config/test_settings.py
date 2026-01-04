"""
Загружает конфигурацию из .env и предоставляет переменные (BASE_URL, ADMIN_EMAIL и т.д.) для всего проекта.
"""
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
API_BASE_URL = os.getenv("API_BASE_URL")