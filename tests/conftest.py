import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.test_settings import BASE_URL


@pytest.fixture(scope="function")
def browser():
    # Автоматическая загрузка ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Отключает визуальное представления браузера
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()