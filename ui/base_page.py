# Базовый класс для всех страниц веб-интерфейса.
# Содержит универсальные методы взаимодействия с WebDriver: поиск элементов, переходы, ожидания.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.test_settings import UI_DELAY_BEFORE_ACTION, BASE_URL


class BasePage:
    def __init__(self, driver):
        # Инициализация драйвера и базового URL
        self.driver = driver
        self.base_url = BASE_URL

    def _apply_delay(self):
        """Выполняет задержку между действиями, если она включена в настройках."""
        if UI_DELAY_BEFORE_ACTION > 0:
            time.sleep(UI_DELAY_BEFORE_ACTION)

    def go_to_site(self, path=""):
        """
        Открывает базовую страницу приложения.
        Если указан дополнительный путь (например, '/login'), добавляет его к base_url.
        """
        url = self.base_url.rstrip('/') + '/' + path.lstrip('/')
        return self.driver.get(url)
    
    def find_element(self, locator, time=10):
        """
        Ожидает появления элемента на странице и возвращает его.
        Параметры:
            locator – кортеж с типом и значением локатора (By.ID, "username")
            time – максимальное время ожидания в секундах
        """
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )

    def enter_text(self, locator, word):
        """
        Находит текстовое поле, очищает его и вводит указанный текст.
        Перед вводом выполняется задержка.
        """
        self._apply_delay()
        element = self.find_element(locator)
        element.clear()
        element.send_keys(word)

    def click_element(self, locator):
        """Находит элемент и выполняет по нему клик с предварительной задержкой."""
        self._apply_delay()
        self.find_element(locator).click()
