from pages.base_page import BasePage
from locators.product_page_locators import *
from env import *

import allure


class ProductPage(BasePage):

    # TITLE

    @allure.step('Проверить, что присутствует текст кнопки: {text}.')
    def check_back_to_products_button_has_text_(self, text: str):
        self.check_element_has_text(locator=BACK_PRODUCTS, data=text)

    @allure.step('Проверить, что кнопка "Back to products" редиректит Пользователя на Inventory Page.')
    def check_back_to_products_button_leads_to_iventory_page(self):
        self.click_element(locator=BACK_PRODUCTS)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    # CART

    @allure.step('Добавить продукт в корзину.')
    def add_product_to_cart(self):
        self.click_element(locator=ADD_CART)

    @allure.step('Удалить продукт из корзины.')
    def remove_product_from_cart(self):
        self.click_element(locator=REMOVE)

    # PRODUCTS

    @allure.step('Проверить, что название продукта отображается корректно.')
    def check_correct_product_name_shown(self, product_data: dict[str]):
        name = product_data['Name'][0]
        self.check_element_has_text(locator=PRODUCT_NAME, data=name)

    @allure.step('Проверить, что описание продукта отображается корректно.')
    def check_correct_product_description_shown(self, product_data: dict[str]):
        description = product_data['Description'][0]
        self.check_element_has_text(locator=PRODUCT_DESC, data=description)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_correct_product_price_shown(self, product_data: dict[str]):
        price = product_data['Price'][0]
        self.check_element_has_text(locator=PRODUCT_PRICE, data=price)

    @allure.step('Проверить, что отображается изображение продукта.')
    def check_product_image_shown(self):
        self.check_element_shown(locator=PRODUCT_IMAGE)

    @allure.step('Проверить, что присутствует текст кнопки: {text}')
    def check_add_to_cart_button_has_text_(self, text: str):
        self.check_element_has_text(locator=ADD_CART, data=text)

    @allure.step('Проверить, что присутствует текст кнопки: {text}')
    def check_remove_button_has_text_(self, text: str):
        self.check_element_has_text(locator=REMOVE, data=text)

    @allure.step('Проверить, что отсутствует кнопка "Remove".')
    def check_remove_button_not_shown(self):
        self.check_element_not_shown(locator=REMOVE)

    def check_cart_page_opened_with_correct_product_data(self, product_data: dict[str]):
        name = product_data['Name'][0]
        description = product_data['Description'][0]
        price = product_data['Price'][0]
        self.check_url(endpoint=CART_ENDPOINT)
        self.check_element_has_text(locator=PRODUCT_NAME, data=name)
        self.check_element_has_text(locator=PRODUCT_DESC, data=description)
        self.check_element_has_text(locator=PRODUCT_PRICE, data=price)
