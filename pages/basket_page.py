from pages.base_page import BasePage
from locators.basket_page_locators import *
from env import *

import allure


# TITLE

class BasketPage(BasePage):

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
