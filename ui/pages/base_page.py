# Базовый класс для всех страниц. Содержит универсальные методы работы с WebDriver: ожидания, клики, ввод текста. Все страницы наследуются от него.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_settings import UI_DELAY_BEFORE_ACTION
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.ui_delay = UI_DELAY_BEFORE_ACTION

    def _apply_delay(self):
        """Выполняет задержку, если она включена."""
        if self.ui_delay > 0:
            time.sleep(self.ui_delay)

    def open(self, url: str):
        """Открыть страницу по заданному URL."""
        self._apply_delay()
        self.driver.get(url)

    def find_element(self, locator):
        """Найти элемент"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Клик на элемент"""
        self._apply_delay()  # задержка перед кликом
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Ввод текста"""
        self._apply_delay()  # задержка перед вводом
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)