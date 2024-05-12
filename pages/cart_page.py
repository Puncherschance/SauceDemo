from pages.base_page import BasePage
from locators.cart_page_locators import *
from env import *

import allure


class CartPage(BasePage):

    # CART

    @allure.step('Проверить, что присутствует текст кнопки: {text}.')
    def check_continue_shopping_button_has_text_(self, text: str):
        self.check_element_has_text(locator=CONTINUE, data=text)

    @allure.step('Проверить, что кнопка "Continue Shopping" редиректит Пользователя на страницу Inventory Page.')
    def check_continue_shopping_button_leads_to_inventory_page(self):
        self.click_element(locator=CONTINUE)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    @allure.step('Проверить, что присутствует текст кнопки: {text}.')
    def check_checkout_button_has_text_(self, text: str):
        self.check_element_has_text(locator=CHECKOUT, data=text)

    @allure.step('Кликнуть по кнопке Checkout.')
    def click_checkout_button(self):
        self.click_element(locator=CHECKOUT)

    @allure.step('Проверить, что пользователь остается на странице Cart Page.')
    def check_user_stays_on_cart_page(self):
        self.check_url(endpoint=CART_ENDPOINT)

    # PRODUCTS

    @allure.step('Проверить, что отображается корректное название продукта.')
    def check_product_name_has_correct_text(self, product_data: dict[str, str]):
        name = product_data['Name'][0]
        self.check_element_has_text(locator=PRODUCT_NAME, data=name)

    @allure.step('Проверить, что отображаются корректные названия продуктов.')
    def check_product_names_has_correct_text(self, products_data: tuple):
        name_1 = products_data[0]['Name'][0]
        name_2 = products_data[1]['Name'][0]
        self.check_element_has_text(locator=PRODUCT_1_NAME, data=name_1)
        self.check_element_has_text(locator=PRODUCT_2_NAME, data=name_2)

    @allure.step('Проверить, что отображается корректное описание продукта.')
    def check_product_description_has_correct_text(self, product_data: dict[str, str]):
        description = product_data['Description'][0]
        self.check_element_has_text(locator=PRODUCT_DESC, data=description)

    @allure.step('Проверить, что отображаются корректные описания продуктов.')
    def check_product_descriptions_has_correct_text(self, products_data: tuple):
        description_1 = products_data[0]['Description'][0]
        description_2 = products_data[1]['Description'][0]
        self.check_element_has_text(locator=PRODUCT_1_DESC, data=description_1)
        self.check_element_has_text(locator=PRODUCT_2_DESC, data=description_2)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_product_has_correct_price(self, product_data: dict[str, str]):
        price = product_data['Price'][0]
        self.check_element_has_text(locator=PRODUCT_PRICE, data=price)

    @allure.step('Проверить, что отображаются корректные цены продуктов.')
    def check_products_has_correct_prices(self, products_data: tuple):
        price_1 = products_data[0]['Price'][0]
        price_2 = products_data[1]['Price'][0]
        self.check_element_has_text(locator=PRODUCT_1_PRICE, data=price_1)
        self.check_element_has_text(locator=PRODUCT_2_PRICE, data=price_2)

    @allure.step('Проверить, что отображается количество продукта {value}.')
    def check_product_has_qty_(self, value: str):
        self.check_element_has_text(locator=PRODUCT_QTY, data=value)

    @allure.step('Проверить, что отображается количество продукта {value} для каждого продукта.')
    def check_products_has_qty_(self, value: str):
        self.check_element_has_text(locator=PRODUCT_1_QTY, data=value)
        self.check_element_has_text(locator=PRODUCT_2_QTY, data=value)

    @allure.step('Проверить, что отображается кнопка "Remove".')
    def check_remove_button_has_text_(self, text: str):
        self.check_element_has_text(locator=REMOVE, data=text)

    @allure.step('Кликнуть по названию продукта.')
    def click_product_name(self):
        self.click_element(locator=PRODUCT_NAME)

    @allure.step('Проверить, что информация по продукту не отображается на странице.')
    def check_product_data_not_shown(self):
        self.check_element_not_shown(locator=PRODUCT_NAME)
        self.check_element_not_shown(locator=PRODUCT_DESC)
        self.check_element_not_shown(locator=PRODUCT_PRICE)
        self.check_element_not_shown(locator=PRODUCT_QTY)
        self.check_element_not_shown(locator=REMOVE)

    @allure.step('Проверить, что отображается количество кнопок "Remove" равное {value}.')
    def check_remove_buttons_qty_(self, value: str):
        self.check_element_qty(locator=REMOVE, data=value)

    # NAVIGATION

    @allure.step('Проверить, что кнопка "Checkout" редиректит пользователя на страницу Checkout Page.')
    def check_checkout_page_opened(self):
        self.check_url(endpoint=CHECKOUT_ENDPOINT)

    @allure.step('Проверить, что клие по названию продукта редиректит пользователя на страницу Product Page.')
    def check_product_page_opened(self, product_data: dict[str, str]):
        item_order = product_data['Order']
        self.check_url(endpoint=PRODUCT_ENDPOINT + item_order)
