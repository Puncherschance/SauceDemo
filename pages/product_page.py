from pages.base_page import BasePage
from locators.product_page_locators import *
from env import *


import allure
import time


class ProductPage(BasePage):

    # TITLE

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_swag_labs_title_has_text_(self, data):
        self.check_element_shown(locator=TITLE)
        self.check_element_has_text(locator=TITLE, data=data)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_back_to_products_title_has_text_(self, data):
        self.check_element_shown(locator=BACK_PRODUCTS)
        self.check_element_has_text(locator=BACK_PRODUCTS, data=data)

    @allure.step('Проверить, что кнопка "Back to products" редиректит Пользователя на Inventory Page.')
    def check_back_to_products_tittle_leads_to_iventory_page(self):
        self.check_element_shown(locator=BACK_PRODUCTS)
        self.click_element(locator=BACK_PRODUCTS)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

