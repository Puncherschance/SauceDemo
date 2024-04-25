from pages.base_page import BasePage
from locators.inventory_page_locators import *
from env import *

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

    @allure.step('Проверить, что присутствует текст Условий использования: {data}.')
    def check_terms_of_service_has_text_(self, data):
        self.check_element_shown(locator=TERMS)
        self.check_element_has_text(locator=TERMS, data=data)

    @allure.step('Проверить, что присутствует Гамбургер меню.')
    def check_hamburger_icon_shown(self):
        self.check_element_shown(locator=HAMBURGER)

    @allure.step('Открыть Гамбургер меню.')
    def open_hamburger_menu(self):
        self.check_element_shown(locator=HAMBURGER)
        self.click_element(locator=HAMBURGER)

    @allure.step('Проверить, что в Гамбургер меню присутствует текст опции: {data}.')
    def check_all_items_option_has_text_(self, data):
        self.check_element_shown(locator=ALL_ITEMS)
        self.check_element_has_text(locator=ALL_ITEMS, data=data)

    @allure.step('Проверить, что в Гамбургер меню присутствует текст опции: {data}.')
    def check_logout_option_has_text_(self, data):
        self.check_element_shown(locator=LOGOUT)
        self.check_element_has_text(locator=LOGOUT, data=data)

    @allure.step('Проверить, что присутствует кнопка "Корзина".')
    def check_basket_icon_shown(self):
        self.check_element_shown(locator=TITLE)

    @allure.step('Проверить, что присутствует поле выбора сортировки.')
    def check_sort_menu_shown(self):
        self.check_element_shown(locator=SORT_MENU)

    @allure.step('Проверить, что присутствует кнопка "раскрыть" в поле выбора сортировки.')
    def check_sort_menu_button_shown(self):
        self.check_element_shown(locator=SORT_MENU_BUTTON)

    @allure.step('Проверить, что кнопка "Твиттер" редиректит Пользователя на страницу "Твиттер".')
    def check_twitter_icon_redirect(self):
        self.check_element_shown(locator=TWITTER)
        self.click_element(locator=TWITTER)
        self.check_outer_url(TWITTER_URL)

    @allure.step('Проверить, что кнопка "All Items" в гамбургер меню редиректит Пользователя на страницу "Inventory Page".')
    def check_all_items_option_leads_to_iventory_page(self):
        self.check_element_shown(locator=ALL_ITEMS)
        self.click_element(locator=ALL_ITEMS)
        self.check_url(INVENTORY_ENDPOINT)

    @allure.step('Проверить, что кнопка "Logout" в гамбургер меню редиректит Пользователя на страницу "Login Page".')
    def check_logout_option_leads_to_login_page(self):
        self.check_element_shown(locator=LOGOUT)
        self.click_element(locator=LOGOUT)
        self.check_url(LOGIN_ENDPOINT)
