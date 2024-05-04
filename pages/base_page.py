from pages.base_methods import BaseMethods
from locators.base_page_locators import *
from env import *

import allure


class BasePage(BaseMethods):

    # TITLE

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_swag_labs_title_has_text_(self, data):
        self.check_element_has_text(locator=TITLE, data=data)

    @allure.step('Проверить, что присутствует текст заголовка: {data}.')
    def check_page_title_has_text_(self, data):
        self.check_element_has_text(locator=PAGE_TITLE, data=data)

    # HAMBURGER_MENU

    @allure.step('Проверить, что присутствует Гамбургер меню.')
    def check_hamburger_icon_shown(self):
        self.check_element_shown(locator=HAMBURGER)

    @allure.step('Открыть Гамбургер меню.')
    def open_hamburger_menu(self):
        self.click_element(locator=HAMBURGER)

    @allure.step('Проверить, что в Гамбургер меню присутствует текст опции: {data}.')
    def check_hamburger_option_has_text(self, data):
        name, locator = data[0], data[1]
        self.check_element_has_text(locator=locator, data=name)

    @allure.step('Кликнуть по опции "Reset App State".')
    def select_reset_app_state_option(self):
        self.click_element(locator=RESET)

    @allure.step(
        'Проверить, что кнопка "All Items" в гамбургер меню редиректит Пользователя на страницу "Inventory Page".')
    def check_all_items_option_leads_to_iventory_page(self):
        self.click_element(locator=ALL_ITEMS)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    @allure.step('Проверить, что кнопка "Logout" в гамбургер меню редиректит Пользователя на страницу "Login Page".')
    def check_logout_option_leads_to_login_page(self):
        self.click_element(locator=LOGOUT)
        self.check_url(endpoint=LOGIN_ENDPOINT)

    @allure.step('Проверить, что кнопка "About" в гамбургер меню редиректит Пользователя на страницу "About Sauce Demo".')
    def check_about_option_leads_to_about_page(self):
        self.click_element(locator=ABOUT)
        self.check_url(endpoint=ABOUT_ENDPOINT)

    # CART

    @allure.step('Проверить, что присутствует кнопка "Корзина".')
    def check_cart_icon_shown(self):
        self.check_element_shown(locator=TITLE)

    @allure.step('Открыть пустую корзину.')
    def open_empty_cart(self):
        self.click_element(locator=CART)

    @allure.step('Проверить, что открывается пустая корзина.')
    def check_cart_page_opened(self):
        self.check_url(endpoint=CART_ENDPOINT)

    # FOOTER

    @allure.step('Проверить, что присутствует текст Условий Использования: {data}.')
    def check_terms_of_service_has_text_(self, data):
        self.check_element_has_text(locator=TERMS, data=data)

    @allure.step('Проверить, что кнопка "Twitter" редиректит Пользователя на страницу "Twitter".')
    def check_twitter_icon_leads_to_twitter_page(self):
        self.click_element(locator=TWITTER)
        self.check_outer_url(url=TWITTER_URL)

    @allure.step('Проверить, что кнопка "Facebook" редиректит Пользователя на страницу "Facebook".')
    def check_facebook_icon_leads_to_facebook_page(self):
        self.click_element(locator=FACEBOOK)
        self.check_outer_url(url=FACEBOOK_URL)

    @allure.step('Проверить, что кнопка "LinkedIn" редиректит Пользователя на страницу "LinkedIn".')
    def check_linkedin_icon_leads_to_linkedin_page(self):
        self.click_element(locator=LINKEDIN)
        self.check_outer_url(url=LINKEDIN_URL)


