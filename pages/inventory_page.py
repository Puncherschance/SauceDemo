from pages.base_page import BasePage
from locators.inventory_page_locators import *
from env import *
from helpers.helpers import *


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

    @allure.step('Проверить, что в Гамбургер меню присутствует текст опции: {data}.')
    def check_about_option_has_text_(self, data):
        self.check_element_shown(locator=ABOUT)
        self.check_element_has_text(locator=ABOUT, data=data)

    @allure.step(
        'Проверить, что кнопка "All Items" в гамбургер меню редиректит Пользователя на страницу "Inventory Page".')
    def check_all_items_option_leads_to_iventory_page(self):
        self.check_element_shown(locator=ALL_ITEMS)
        self.click_element(locator=ALL_ITEMS)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    @allure.step('Проверить, что кнопка "Logout" в гамбургер меню редиректит Пользователя на страницу "Login Page".')
    def check_logout_option_leads_to_login_page(self):
        self.check_element_shown(locator=LOGOUT)
        self.click_element(locator=LOGOUT)
        self.check_url(endpoint=LOGIN_ENDPOINT)

    @allure.step('Проверить, что кнопка "About" в гамбургер меню редиректит Пользователя на страницу "About Sauce Demo".')
    def check_about_option_leads_to_about_page(self):
        self.check_element_shown(locator=ABOUT)
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

    @allure.step('Добавить продукт в корзину.')
    def add_product_to_cart(self):
        self.check_element_shown(locator=PRODUCT_1_CART)
        self.click_element(locator=PRODUCT_1_CART)

    @allure.step('Удалить продукт из корзины.')
    def remove_product_from_cart(self):
        self.check_element_shown(locator=PRODUCT_1_CART)
        self.click_element(locator=PRODUCT_1_CART)

    @allure.step('Добавить все возможные продукты в корзину.')
    def add_all_products_to_cart(self):
        for cart_button in product_cart_buttons:
            self.check_element_shown(locator=cart_button)
            self.click_element(locator=cart_button)

    @allure.step('Удалить все возможные продукты из корзины.')
    def remove_all_products_from_cart(self):
        for cart_button in product_cart_buttons:
            self.check_element_shown(locator=cart_button)
            self.click_element(locator=cart_button)

    @allure.step('Проверить, что значок количества продуктов возле корзины показывает значение {value}.')
    def check_cart_badge_value_equal_(self, value):
        self.check_element_shown(locator=CART_BADGE)
        self.check_element_has_text(locator=CART_BADGE, data=value)

    @allure.step('Проверить, что значок количества продуктов возле корзины скрыт.')
    def check_cart_badge_value_not_shown(self):
        self.check_element_not_shown(CART_BADGE)

    # SORT_MENU

    @allure.step('Проверить, что присутствует поле выбора сортировки продуктов.')
    def check_sort_menu_shown(self):
        self.check_element_shown(locator=SORT_MENU)

    @allure.step('Проверить, что присутствует кнопка "раскрыть" в поле выбора сортировки продуктов.')
    def check_sort_menu_button_shown(self):
        self.check_element_shown(locator=SORT_MENU_BUTTON)

    @allure.step('Проверить, что присутствуют все доступные опции сортировки продуктов.')
    def check_all_sorting_options_shown(self):
        self.click_element(locator=SORT_MENU)
        self.check_element_has_text(locator=SORT_MENU, data='Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)')

    @allure.step('Отсортировать предметы по принципу {option}.')
    def sort_products_(self, option):
        self.click_element(locator=SORT_MENU)
        self.select_option(locator=SORT_MENU, option=option)

    @allure.step('Проверить, что продукты сортируются по имени от меньшего к большему.')
    def check_products_sorted_by_alphabet_asc(self):
        product_names = self.get_list_of(data=PRODUCT_NAMES)
        self.check_asc_sorting(product_names)

    @allure.step('Проверить, что продукты сортируются по имени от большего к меньшему.')
    def check_products_sorted_by_alphabet_desc(self):
        product_names = self.get_list_of(data=PRODUCT_NAMES)
        self.check_desc_sorting(product_names)

    @allure.step('Проверить, что продукты сортируются по цене от наименьшей к наибольшей.')
    def check_products_sorted_by_price_asc(self):
        product_prices_text = self.get_list_of(data=PRODUCT_PRICES)
        product_prices = convert_to_float(product_prices_text)
        self.check_asc_sorting(product_prices)

    @allure.step('Проверить, что продукты сортируются по цене от наибольшей к наименьшей.')
    def check_products_sorted_by_price_desc(self):
        product_prices_text = self.get_list_of(data=PRODUCT_PRICES)
        product_prices = convert_to_float(product_prices_text)
        self.check_desc_sorting(product_prices)

    # PRODUCTS

    @allure.step('Проверить, что название продукта отображается корректно.')
    def check_product_name(self, data):
        name = data['Name'][0]
        locator = data['Name'][1]
        self.check_element_shown(locator=locator)
        self.check_element_has_text(locator=locator, data=name)

    @allure.step('Проверить, что описание продукта отображается корректно.')
    def check_product_description(self, data):
        description = data['Description'][0]
        locator = data['Description'][1]
        self.check_element_shown(locator=locator)
        self.check_element_has_text(locator=locator, data=description)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_product_price(self, data):
        price = data['Price'][0]
        locator = data['Price'][1]
        self.check_element_shown(locator=locator)
        self.check_element_has_text(locator=locator, data=price)

    @allure.step('Проверить, что отображается изображение продукта.')
    def check_product_image(self, data):
        locator = data['Image']
        self.check_element_shown(locator=locator)

    @allure.step('Открыть подробное описание продукта, кликнув на название продукта.')
    def expand_product_description_via_clicking_product_name(self, data):
        locator = data['Name'][1]
        self.check_element_shown(locator=locator)
        self.click_element(locator=locator)

    @allure.step('Открыть подробное описание продукта, кликнув на изображение продукта.')
    def expand_product_description_via_clicking_product_image(self, data):
        locator = data['Image']
        self.check_element_shown(locator=locator)
        self.click_element(locator=locator)

    @allure.step('Проверить, что открылась "Product Page".')
    def check_product_page_opened(self, data):
        item_order = data['Order']
        self.check_url(endpoint=PRODUCT_ENDPOINT+item_order)

    # FOOTER

    @allure.step('Проверить, что присутствует текст Условий Использования: {data}.')
    def check_terms_of_service_has_text_(self, data):
        self.check_element_shown(locator=TERMS)
        self.check_element_has_text(locator=TERMS, data=data)

    @allure.step('Проверить, что кнопка "Twitter" редиректит Пользователя на страницу "Twitter".')
    def check_twitter_icon_leads_to_twitter_page(self):
        self.check_element_shown(locator=TWITTER)
        self.click_element(locator=TWITTER)
        self.check_outer_url(url=TWITTER_URL)

    @allure.step('Проверить, что кнопка "Facebook" редиректит Пользователя на страницу "Facebook".')
    def check_facebook_icon_leads_to_facebook_page(self):
        self.check_element_shown(locator=FACEBOOK)
        self.click_element(locator=FACEBOOK)
        self.check_outer_url(url=FACEBOOK_URL)

    @allure.step('Проверить, что кнопка "LinkedIn" редиректит Пользователя на страницу "LinkedIn".')
    def check_linkedin_icon_leads_to_linkedin_page(self):
        self.check_element_shown(locator=LINKEDIN)
        self.click_element(locator=LINKEDIN)
        self.check_outer_url(url=LINKEDIN_URL)
