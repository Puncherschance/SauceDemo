from pages.base_page import BasePage
from locators.cart_page_locators import *
from env import *

import allure


class CartPage(BasePage):

    # TITLE

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_swag_labs_title_has_text_(self, data):
        self.check_element_shown(locator=TITLE)
        self.check_element_has_text(locator=TITLE, data=data)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_your_cart_title_has_text_(self, data):
        self.check_element_shown(locator=YOUR_CART)
        self.check_element_has_text(locator=YOUR_CART, data=data)

    # CART

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_qty_title_has_text_(self, data):
        self.check_element_shown(locator=QTY)
        self.check_element_has_text(locator=QTY, data=data)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_description_title_has_text_(self, data):
        self.check_element_shown(locator=DESCRIPTION)
        self.check_element_has_text(locator=DESCRIPTION, data=data)

    @allure.step('Проверить, что присутствует текст кнопки: {data}.')
    def check_continue_shopping_button_has_text_(self, data):
        self.check_element_shown(locator=CONTINUE)
        self.check_element_has_text(locator=CONTINUE, data=data)

    @allure.step('Проверить, что кнопка "Continue Shopping" редиректит Пользователя на страницу Inventory Page.')
    def check_continue_shopping_button_leads_to_inventory_page(self):
        self.check_element_shown(locator=CONTINUE)
        self.click_element(locator=CONTINUE)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    # FOOTER

    @allure.step('Проверить, что присутствует текст Условий использования: {data}.')
    def check_terms_of_service_has_text_(self, data):
        self.check_element_shown(locator=TERMS)
        self.check_element_has_text(locator=TERMS, data=data)

    @allure.step('Проверить, что кнопка "Твиттер" редиректит Пользователя на страницу "Твиттер".')
    def check_twitter_icon_redirect(self):
        self.check_element_shown(locator=TWITTER)
        self.click_element(locator=TWITTER)
        self.check_outer_url(url=TWITTER_URL)
