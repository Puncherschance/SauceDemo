from pages.base_page import BasePage
from locators.inventory_page_locators import *

import allure


class InventoryPage(BasePage):

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_swag_labs_title_has_text_(self, data):
        self.check_element_shown(locator=TITLE)
        self.check_element_has_text(locator=TITLE, data=data)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_products_title_has_text_(self, data):
        self.check_element_shown(locator=PRODUCTS)
        self.check_element_has_text(locator=PRODUCTS, data=data)

    @allure.step('Проверить, что присутствует Гамбургер меню.')
    def check_hamburger_icon_shown(self):
        self.check_element_shown(locator=TITLE)
