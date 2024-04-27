from pages.base_page import BasePage
from locators.inventory_page_locators import *
from env import *

import allure


class InventoryPage(BasePage):

    # TITLE

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_swag_labs_title_has_text_(self, data):
        self.check_element_shown(locator=TITLE)
        self.check_element_has_text(locator=TITLE, data=data)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_products_title_has_text_(self, data):
        self.check_element_shown(locator=PRODUCTS)
        self.check_element_has_text(locator=PRODUCTS, data=data)

    # HAMBURGER_MENU

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

    @allure.step(
        'Проверить, что кнопка "All Items" в гамбургер меню редиректит Пользователя на страницу "Inventory Page".')
    def check_all_items_option_leads_to_iventory_page(self):
        self.check_element_shown(locator=ALL_ITEMS)
        self.click_element(locator=ALL_ITEMS)
        self.check_url(INVENTORY_ENDPOINT)

    @allure.step('Проверить, что кнопка "Logout" в гамбургер меню редиректит Пользователя на страницу "Login Page".')
    def check_logout_option_leads_to_login_page(self):
        self.check_element_shown(locator=LOGOUT)
        self.click_element(locator=LOGOUT)
        self.check_url(LOGIN_ENDPOINT)

    # BASKET

    @allure.step('Проверить, что присутствует кнопка "Корзина".')
    def check_basket_icon_shown(self):
        self.check_element_shown(locator=TITLE)

    @allure.step('Открыть пустую корзину.')
    def open_empty_basket(self):
        self.click_element(locator=BASKET)

    @allure.step('Проверить, что открывается пустая корзина.')
    def check_basket_page_opened(self):
        self.check_url(BASKET_ENDPOINT)

    # SORT_MENU

    @allure.step('Проверить, что присутствует поле выбора сортировки.')
    def check_sort_menu_shown(self):
        self.check_element_shown(locator=SORT_MENU)

    @allure.step('Проверить, что присутствует кнопка "раскрыть" в поле выбора сортировки.')
    def check_sort_menu_button_shown(self):
        self.check_element_shown(locator=SORT_MENU_BUTTON)

    # ITEMS

    @allure.step('Проверить, что название товара отображается корректно.')
    def check_product_title(self, data):
        title = data['Title'][0]
        locator = data['Title'][1]
        self.check_element_shown(locator=locator)
        self.check_element_has_text(locator=locator, data=title)

    @allure.step('Проверить, что описание товара отображается корректно.')
    def check_product_description(self, data):
        description = data['Description'][0]
        locator = data['Description'][1]
        self.check_element_shown(locator=locator)
        self.check_element_has_text(locator=locator, data=description)

    @allure.step('Проверить, что отображается корректная цена товара.')
    def check_product_price(self, data):
        price = data['Price'][0]
        locator = data['Price'][1]
        self.check_element_shown(locator=locator)
        self.check_element_has_text(locator=locator, data=price)

    @allure.step('Проверить, что отображается изображение товара.')
    def check_product_image(self, data):
        locator = data['Image']
        self.check_element_shown(locator=locator)

    # FOOTER

    @allure.step('Проверить, что присутствует текст Условий использования: {data}.')
    def check_terms_of_service_has_text_(self, data):
        self.check_element_shown(locator=TERMS)
        self.check_element_has_text(locator=TERMS, data=data)

    @allure.step('Проверить, что кнопка "Твиттер" редиректит Пользователя на страницу "Твиттер".')
    def check_twitter_icon_redirect(self):
        self.check_element_shown(locator=TWITTER)
        self.click_element(locator=TWITTER)
        self.check_outer_url(TWITTER_URL)
