from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.login_page_locators import *
from env import *

import allure


class LoginPage(BasePage):

    @allure.step(f'Открыть страницу {BASE_PAGE_URL+LOGIN_PAGE_ENDPOINT}.')
    def open_login_page(self):
        self.open_url(endpoint=LOGIN_PAGE_ENDPOINT)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_tittle_has_text_(self, data):
        tittle = self.page.locator(TITTLE)
        expect(tittle, f'Ожидался текст заголовка: {data}. Получен текст заголовка {tittle.text_content()}.').to_have_text(data)

    @allure.step('Проверить, что в поле "Username" присутствует плейсхолдер: {data}.')
    def check_login_field_has_placeholder_(self, data):
        login_field = self.page.locator(LOGIN_FIELD)
        expect(login_field, f'Ожидался текст плейсхолдера: {data}. Получен текст плейсхолдера {login_field.get_attribute("placeholder")}.').to_have_attribute('placeholder', data)

    @allure.step('Проверить, что в поле "Password" присутствует плейсхолдер: {data}.')
    def check_password_field_has_placeholder_(self, data):
        password_field = self.page.locator(PASSWORD_FIELD)
        expect(password_field, f'Ожидался текст плейсхолдера: {data}. Получен текст плейсхолдера {password_field.get_attribute("placeholder")}.').to_have_attribute('placeholder', data)

    @allure.step('Проверить, что присутствует кнопка "Login".')
    def check_login_button_is_shown(self):
        login_button = self.page.locator(LOGIN_BUTTON)
        expect(login_button).to_be_visible()

    @allure.step('Ввести в поле "Username" логин: {data}.')
    def enter_username_(self, data):
        self.page.get_by_placeholder('Username').fill(data)

    @allure.step('Ввести в поле "Username" пароль: {data}.')
    def enter_password_(self, data):
        self.page.get_by_placeholder('Password').fill(data)

    @allure.step('Кликнуть по кнопке "Login".')
    def click_login_button(self):
        self.page.locator(LOGIN_BUTTON).click()

    @allure.step('Проверить, что появилась валидация.')
    def check_validation_is_shown(self):
        validation = self.page.locator(EPIC_SADFACE)
        expect(validation).to_be_visible()

    @allure.step('Проверить, что присутствует текст валидации: {data}.')
    def check_validation_has_text_(self, data):
        validation = self.page.locator(EPIC_SADFACE)
        expect(validation).to_have_text(data)

    @allure.step('Проверить, что открылась страница "Inventory".')
    def check_inventory_page_opened(self):
        expect(self.page).to_have_url(BASE_PAGE_URL+INVENTORY_ENDPOINT)
