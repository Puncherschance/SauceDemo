import allure

from env import *
from locators.login_page_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):

    # TITLE

    @allure.step("Проверить, что присутствует текст заголовка: {text}.")
    def check_swag_labs_title_has_text_(self, text):
        self.check_element_has_text(locator=TITLE, data=text)

    # LOGIN_FORM

    @allure.step('Проверить, что в поле "Username" присутствует плейсхолдер: {text}.')
    def check_login_field_has_placeholder_(self, text: str):
        self.check_placeholder_text(locator=LOGIN_FIELD, data=text)

    @allure.step('Проверить, что в поле "Password" присутствует плейсхолдер: {text}.')
    def check_password_field_has_placeholder_(self, text: str):
        self.check_placeholder_text(locator=PASSWORD_FIELD, data=text)

    @allure.step('Проверить, что присутствует кнопка "Login".')
    def check_login_button_has_text_(self, text: str):
        self.check_element_has_text(locator=LOGIN_BUTTON, data=text)

    @allure.step('Ввести в поле "Username" логин: {text}.')
    def enter_username_(self, text: str):
        self.enter_data(locator=LOGIN_FIELD, data=text)

    @allure.step('Ввести в поле "Password" пароль: {text}.')
    def enter_password_(self, text: str):
        self.enter_data(locator=PASSWORD_FIELD, data=text)

    @allure.step('Кликнуть по кнопке "Login".')
    def click_login_button(self):
        self.click_element(locator=LOGIN_BUTTON)

    # VALIDATION

    @allure.step("Проверить, что присутствует текст валидации: {text}.")
    def check_validation_has_text_(self, text: str):
        self.check_element_has_text(locator=VALIDATION, data=text)

    @allure.step("Закрыть валидацию.")
    def close_validation(self):
        self.click_element(locator=VALIDATION_CLOSE)

    @allure.step("Проверить, что валидация исчезла.")
    def check_validation_not_shown(self):
        self.check_element_not_shown(locator=VALIDATION)

    # NAVIGATION

    @allure.step(f"Открыть страницу {BASE_URL+LOGIN_ENDPOINT}.")
    def open_login_page(self):
        self.open_url(endpoint=LOGIN_ENDPOINT)

    @allure.step("Открыть страницу напрямую через url {page_endpoint}.")
    def open_page_by_direct_url(self, page_endpoint: str):
        self.open_url(endpoint=page_endpoint)
