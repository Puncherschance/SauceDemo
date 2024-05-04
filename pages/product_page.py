from pages.base_page import BasePage
from pages.base_methods import BaseMethods
from locators.product_page_locators import *
from env import *

import allure


class ProductPage(BasePage, BaseMethods):

    # TITLE

    @allure.step('Проверить, что присутствует текст кнопки: {data}.')
    def check_back_to_products_button_has_text_(self, data):
        self.check_element_has_text(locator=BACK_PRODUCTS, data=data)

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

    @allure.step('Проверить, что значок количества продуктов возле корзины показывает значение {value}.')
    def check_cart_badge_value_equal_(self, value):
        self.check_element_has_text(locator=CART_BADGE, data=value)

    @allure.step('Проверить, что значок количества продуктов возле корзины скрыт.')
    def check_cart_badge_value_not_shown(self):
        self.check_element_not_shown(CART_BADGE)

    # PRODUCTS

    @allure.step('Проверить, что название продукта отображается корректно.')
    def check_correct_product_name_shown(self, data):
        name = data['Name'][0]
        self.check_element_has_text(locator=PRODUCT_NAME, data=name)

    @allure.step('Проверить, что описание продукта отображается корректно.')
    def check_correct_product_description_shown(self, data):
        description = data['Description'][0]
        self.check_element_has_text(locator=PRODUCT_DESC, data=description)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_correct_product_price_shown(self, data):
        price = data['Price'][0]
        self.check_element_has_text(locator=PRODUCT_PRICE, data=price)

    @allure.step('Проверить, что отображается изображение продукта.')
    def check_product_image_shown(self):
        self.check_element_shown(locator=PRODUCT_IMAGE)

    @allure.step('Проверить, что присутствует текст кнопки: {data}')
    def check_add_to_cart_button_has_text_(self, data):
        self.check_element_has_text(locator=ADD_CART, data=data)

    @allure.step('Проверить, что присутствует текст кнопки: {data}')
    def check_remove_button_has_text_(self, data):
        self.check_element_has_text(locator=REMOVE, data=data)

    @allure.step('Проверить, что отсутствует кнопка "Remove".')
    def check_remove_button_not_shown(self):
        self.check_element_not_shown(locator=REMOVE)



