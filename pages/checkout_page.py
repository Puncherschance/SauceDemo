from pages.base_page import BasePage
from locators.checkout_page_locators import *

import allure


class CheckoutPage(BasePage):

    # REQUISITES

    @allure.step('Проверить, что в поле "First Name" присутствует плейсхолдер: {text}.')
    def check_first_name_field_has_placeholder_(self, text: str):
        self.check_placeholder_text(locator=FIRST_NAME, data=text)

    @allure.step('Ввести в поле "First Name" текст: {text}.')
    def enter_first_name_(self, text: str):
        self.enter_data(locator=FIRST_NAME, data=text)

    @allure.step('Проверить, что в поле "Last Name" присутствует плейсхолдер: {text}.')
    def check_last_name_field_has_placeholder_(self, text: str):
        self.check_placeholder_text(locator=LAST_NAME, data=text)

    @allure.step('Ввести в поле "Last Name" текст: {text}.')
    def enter_last_name_(self, text: str):
        self.enter_data(locator=LAST_NAME, data=text)

    @allure.step('Проверить, что в поле "Zip/Postal Code" присутствует плейсхолдер: {text}.')
    def check_postal_field_has_placeholder_(self, text: str):
        self.check_placeholder_text(locator=POSTAL_CODE, data=text)

    @allure.step('Ввести в поле "Zip/Postal Code" текст: {text}.')
    def enter_postal_code_(self, text: str):
        self.enter_data(locator=POSTAL_CODE, data=text)

    @allure.step('Проверить, что для кнопки "Continue" присутствует текст: {text}.')
    def check_continue_button_has_text_(self, text: str):
        self.check_element_has_text(locator=CONTINUE, data=text)

    @allure.step('Кликнуть по кнопке "Continue".')
    def click_continue_button(self):
        self.click_element(locator=CONTINUE)

    @allure.step('Проверить, что для кнопки "Cancel" присутствует текст: {text}.')
    def check_cancel_button_has_text_(self, text: str):
        self.check_element_has_text(locator=CANCEL, data=text)

    @allure.step('Кликнуть по кнопке "Continue".')
    def click_cancel_button(self):
        self.click_element(locator=CANCEL)

    # VALIDATION

    @allure.step('Проверить, что присутствует текст валидации: {text}.')
    def check_validation_has_text_(self, text: str):
        self.check_element_has_text(locator=VALIDATION, data=text)

    @allure.step('Закрыть валидацию.')
    def close_validation(self):
        self.click_element(locator=VALIDAION_CLOSE)

    @allure.step('Проверить, что валидация исчезла.')
    def check_validation_not_shown(self):
        self.check_element_not_shown(locator=VALIDATION)

