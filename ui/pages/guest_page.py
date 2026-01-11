# Содержит локаторы и бизнес-методы для всех действий неавторизованного пользователя (гостя).
from selenium.webdriver.common.by import By
from ui.base_page import BasePage


class GuestPageLocators:
    """Класс с локаторами для тестирования всех страниц, доступных гостю."""
    # Главная страница
    LOCATOR_GUEST_WELCOME = (By.CSS_SELECTOR, ".user_greeting h4")
    LOCATOR_FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, ".title_product a.product-title-link")

    # Страница товара
    LOCATOR_OPEN_ASK_MODAL_BTN = (By.ID, "open-ask-modal-btn")

    # Модальное окно "Задать вопрос"
    LOCATOR_ASK_NAME_INPUT = (By.NAME, "name")
    LOCATOR_ASK_EMAIL_INPUT = (By.NAME, "email")
    LOCATOR_ASK_CATEGORY_SELECT = (By.NAME, "category")
    LOCATOR_ASK_MESSAGE_TEXTAREA = (By.NAME, "message")
    LOCATOR_ASK_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn-submit[type='submit']")

    # Уведомление об успешной отправке сообщения
    LOCATOR_SUCCESS_MESS = (By.ID, "custom-notification")

    # Модальное окно "Написать нам"
    LOCATOR_CONTACT_TAB = (By.CSS_SELECTOR, ".guest-contact-tab")

    # Опции в выпадающем списке категории
    LOCATOR_CATEGORY_OPTION_PRODUCT = (By.XPATH, "//select[@name='category']//option[@value='1']")
    LOCATOR_CATEGORY_OPTION_OTHER = (By.XPATH, "//select[@name='category']//option[@value='3']")
    LOCATOR_CATEGORY_OPTION_TECH = (By.XPATH, "//select[@name='category']//option[@value='2']")

    # Поиск на главной странице
    LOCATOR_SEARCH_INPUT = (By.ID, "search-input")
    LOCATOR_SEARCH_BUTTON = (By.ID, "search-btn")

    # Сообщение об отсутствии товаров
    LOCATOR_NO_PRODUCTS_MESSAGE = (By.CSS_SELECTOR, "#product-container p")


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

    def get_success_text(self) -> str:
        """
        Ожидает появления уведомления об успешной отправке и возвращает его текст.
        """
        alert_el = self.find_element(GuestPageLocators.LOCATOR_SUCCESS_MESS, time=10)
        return alert_el.text.strip()

    def open_contact_form_from_main(self):
        """Открывает форму 'Написать нам' с главной страницы."""
        self.click_element(GuestPageLocators.LOCATOR_CONTACT_TAB)

    def fill_contact_form_with_category(self, name: str, email: str, category: str, message: str):
        self.enter_text(GuestPageLocators.LOCATOR_ASK_NAME_INPUT, name)
        self.enter_text(GuestPageLocators.LOCATOR_ASK_EMAIL_INPUT, email)

        # Прямой выбор опции
        option_locator = {
            "1": GuestPageLocators.LOCATOR_CATEGORY_OPTION_PRODUCT,
            "2": GuestPageLocators.LOCATOR_CATEGORY_OPTION_TECH,
            "3": GuestPageLocators.LOCATOR_CATEGORY_OPTION_OTHER,
        }.get(category)
        
        if not option_locator:
            raise ValueError(f"Неизвестная категория: {category}")
        
        self.click_element(option_locator)
        self.enter_text(GuestPageLocators.LOCATOR_ASK_MESSAGE_TEXTAREA, message)

    def send_message_from_main_page(self, name: str, email: str, category: str, message: str):
        """Полный сценарий отправки сообщения с главной страницы."""
        self.open_contact_form_from_main()
        self.fill_contact_form_with_category(name, email, category, message)
        self.submit_ask_form()

    def enter_search_query(self, query: str):
        """Вводит поисковый запрос в поле поиска."""
        self.enter_text(GuestPageLocators.LOCATOR_SEARCH_INPUT, query)

    def click_search_button(self):
        """Нажимает кнопку поиска."""
        self.click_element(GuestPageLocators.LOCATOR_SEARCH_BUTTON)

    def get_first_product_title(self) -> str:
        """
        Возвращает текст заголовка первого отображаемого товара.
        Ожидает появления элемента до 10 секунд.
        """
        element = self.find_element(GuestPageLocators.LOCATOR_FIRST_PRODUCT_LINK, time=10)
        return element.text.strip()

    def get_no_products_message(self) -> str:
        """
        Ожидает появления сообщения 'Товаров не найдено.' и возвращает его текст.
        """
        element = self.find_element(GuestPageLocators.LOCATOR_NO_PRODUCTS_MESSAGE, time=10)
        return element.text.strip()