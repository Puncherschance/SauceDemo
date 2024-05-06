from pages.base_page import BasePage
from locators.cart_page_locators import *
from env import *

import allure


class CartPage(BasePage):

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

    @allure.step('Проверить, что пользователь остается на странице Cart Page.')
    def check_user_stays_on_cart_page(self):
        self.check_url(endpoint=CART_ENDPOINT)

    # PRODUCTS

    @allure.step('Проверить, что отображается корректное название продукта.')
    def check_product_name_has_correct_text(self, data):
        name = data['Name'][0]
        self.check_element_has_text(locator=PRODUCT_NAME, data=name)

    @allure.step('Проверить, что отображается корректное описание продукта.')
    def check_product_description_has_correct_text(self, data):
        description = data['Description'][0]
        self.check_element_has_text(locator=PRODUCT_DESC, data=description)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_product_has_correct_price(self, data):
        price = data['Price'][0]
        self.check_element_has_text(locator=PRODUCT_PRICE, data=price)

    @allure.step('Проверить, что отображается количество продукта {qty}.')
    def check_product_has_qty_(self, qty):
        self.check_element_has_text(locator=PRODUCT_QTY, data=qty)

    @allure.step('Проверить, что отображается кнопка "Remove".')
    def check_remove_button_has_text_(self, data):
        self.check_element_has_text(locator=REMOVE, data=data)

    @allure.step('Кликнуть по названию продукта.')
    def click_product_name(self):
        self.click_element(locator=PRODUCT_NAME)

    @allure.step('Проверить, что открылась страница Product Page с корректным описанием продукта.')
    def check_product_page_opened_with_correct_product_data(self, data):
        item_order = data['Order']
        name = data['Name'][0]
        description = data['Description'][0]
        price = data['Price'][0]
        self.check_url(endpoint=PRODUCT_ENDPOINT + item_order)
        self.check_element_has_text(locator=PRODUCT_NAME, data=name)
        self.check_element_has_text(locator=PRODUCT_DESC, data=description)
        self.check_element_has_text(locator=PRODUCT_PRICE, data=price)


