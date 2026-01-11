# Загружает конфигурацию из .env
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USER_NAME = os.getenv("USER_NAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")
API_BASE_URL = os.getenv("API_BASE_URL")
USER_EMAIL = os.getenv("USER_EMAIL")

# Задержки между действиями (в секундах)
UI_DELAY_BEFORE_ACTION = float(3.5)