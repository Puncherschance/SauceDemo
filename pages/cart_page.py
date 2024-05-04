from pages.base_page import BasePage
from pages.base_methods import BaseMethods
from locators.cart_page_locators import *
from env import *

import allure


class CartPage(BasePage, BaseMethods):

    # CART

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_qty_title_has_text_(self, data):
        self.check_element_has_text(locator=QTY, data=data)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_description_title_has_text_(self, data):
        self.check_element_has_text(locator=DESCRIPTION, data=data)

    @allure.step('Проверить, что присутствует текст кнопки: {data}.')
    def check_continue_shopping_button_has_text_(self, data):
        self.check_element_has_text(locator=CONTINUE, data=data)

    @allure.step('Проверить, что кнопка "Continue Shopping" редиректит Пользователя на страницу Inventory Page.')
    def check_continue_shopping_button_leads_to_inventory_page(self):
        self.click_element(locator=CONTINUE)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    @allure.step('Проверить, что присутствует текст кнопки: {data}.')
    def check_checkout_button_has_text_(self, data):
        self.check_element_has_text(locator=CHECKOUT, data=data)

    @allure.step('Кликнуть по кнопке Checkout.')
    def click_checkout_button(self):
        self.click_element(locator=CHECKOUT)
