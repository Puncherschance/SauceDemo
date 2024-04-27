from pages.base_page import BasePage
from locators.login_page_locators import *
from env import *

import allure


class LoginPage(BasePage):

    # TITLE

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_swag_labs_title_has_text_(self, data):
        self.check_element_shown(locator=TITLE)
        self.check_element_has_text(locator=TITLE, data=data)

    # LOGIN_FORM

    @allure.step('Проверить, что в поле "Username" присутствует плейсхолдер: {data}.')
    def check_login_field_has_placeholder_(self, data):
        self.check_element_shown(locator=LOGIN_FIELD)
        self.check_placeholder_text(locator=LOGIN_FIELD, data=data)

    @allure.step('Проверить, что в поле "Password" присутствует плейсхолдер: {data}.')
    def check_password_field_has_placeholder_(self, data):
        self.check_element_shown(locator=PASSWORD_FIELD)
        self.check_placeholder_text(locator=PASSWORD_FIELD, data=data)

    @allure.step('Проверить, что присутствует кнопка "Login".')
    def check_login_button_is_shown(self):
        self.check_element_shown(locator=LOGIN_BUTTON)

    @allure.step('Ввести в поле "Username" логин: {data}.')
    def enter_username_(self, data):
        self.check_element_shown(locator=LOGIN_FIELD)
        self.enter_data(locator=LOGIN_FIELD, data=data)

    @allure.step('Ввести в поле "Password" пароль: {data}.')
    def enter_password_(self, data):
        self.check_element_shown(locator=PASSWORD_FIELD)
        self.enter_data(locator=PASSWORD_FIELD, data=data)

    @allure.step('Кликнуть по кнопке "Login".')
    def click_login_button(self):
        self.check_element_shown(locator=LOGIN_BUTTON)
        self.click_element(locator=LOGIN_BUTTON)

    # VALIDATION

    @allure.step('Проверить, что присутствует текст валидации: {data}.')
    def check_validation_has_text_(self, data):
        self.check_element_shown(locator=EPIC_SADFACE)
        self.check_element_has_text(locator=EPIC_SADFACE, data=data)

    @allure.step('Закрыть валидацию.')
    def close_validation(self):
        self.check_element_shown(locator=VALIDATION_CLOSE)
        self.click_element(locator=VALIDATION_CLOSE)

    @allure.step('Проверить, что валидация исчезла.')
    def check_validation_not_shown(self):
        self.check_element_not_shown(locator=EPIC_SADFACE)

    # NAVIGATION

    @allure.step(f'Открыть страницу {BASE_URL+LOGIN_ENDPOINT}.')
    def open_login_page(self):
        self.open_url(endpoint=LOGIN_ENDPOINT)

    @allure.step(f'Открыть страницу {BASE_URL + INVENTORY_ENDPOINT}.')
    def open_inventory_page_by_direct_link(self):
        self.open_url(endpoint=INVENTORY_ENDPOINT)

    @allure.step('Проверить, что открылась страница "Inventory".')
    def check_inventory_page_opened(self):
        self.check_url(endpoint=INVENTORY_ENDPOINT)
