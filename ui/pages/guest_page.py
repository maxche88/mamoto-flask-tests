# Содержит локаторы и бизнес-методы для всех действий неавторизованного пользователя (гостя).
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from ui.base_page import BasePage


class GuestPageLocators:
    """Класс с локаторами для всех страниц, доступных гостю."""
    # Главная страница
    LOCATOR_GUEST_WELCOME = (By.CSS_SELECTOR, ".user_greeting h4")
    LOCATOR_FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, ".title_product a.product-title-link")

    # Страница товара
    LOCATOR_OPEN_ASK_MODAL_BTN = (By.ID, "open-ask-modal-btn")

    # Модальное окно "Задать вопрос"
    LOCATOR_ASK_NAME_INPUT = (By.NAME, "name")
    LOCATOR_ASK_EMAIL_INPUT = (By.NAME, "email")
    LOCATOR_ASK_MESSAGE_TEXTAREA = (By.NAME, "message")
    LOCATOR_ASK_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn-submit[type='submit']")

    # Уведомление об успешной отправке
    LOCATOR_SUCCESS_ALERT = (By.XPATH, "//*[contains(text(), 'Ваш вопрос отправлен!')]")



class GuestPageHelper(BasePage):
    """Класс-помощник для выполнения всех действий от имени гостя."""

    # Главная страница
    def get_guest_welcome_text(self):
        """Возвращает текст приветствия на главной странице для гостя."""
        welcome_el = self.find_element(GuestPageLocators.LOCATOR_GUEST_WELCOME, time=5)
        return welcome_el.text.strip()

    def click_first_product(self):
        """Кликает по первой найденной ссылке на товар на главной странице."""
        self.click_element(GuestPageLocators.LOCATOR_FIRST_PRODUCT_LINK)

    # Страница товара
    def open_ask_question_modal(self):
        """Нажимает кнопку 'Отправить сообщение' на странице товара."""
        self.click_element(GuestPageLocators.LOCATOR_OPEN_ASK_MODAL_BTN)

    # Модальное окно с формой
    def fill_ask_form(self, name: str, email: str, message: str):
        """Заполняет форму 'Задать вопрос' в модальном окне."""
        self.enter_text(GuestPageLocators.LOCATOR_ASK_NAME_INPUT, name)
        self.enter_text(GuestPageLocators.LOCATOR_ASK_EMAIL_INPUT, email)
        self.enter_text(GuestPageLocators.LOCATOR_ASK_MESSAGE_TEXTAREA, message)

    def submit_ask_form(self):
        """Нажимает кнопку отправки в форме 'Задать вопрос'."""
        self.click_element(GuestPageLocators.LOCATOR_ASK_SUBMIT_BUTTON)

    def send_question_as_guest(self, name: str, email: str, message: str):
        """
        Полный сценарий: открыть форму, заполнить и отправить вопрос.
        """
        self.open_ask_question_modal()
        self.fill_ask_form(name, email, message)
        self.submit_ask_form()

    # Проверки
    def get_success_alert_text(self) -> str:
        """
        Ожидает появления уведомления об успешной отправке и возвращает его текст.
        """
        try:
            alert_el = self.find_element(GuestPageLocators.LOCATOR_SUCCESS_ALERT, time=10)
            return alert_el.text.strip()
        except TimeoutException:
            return ""