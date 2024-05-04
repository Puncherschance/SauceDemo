from pages.base_methods import BaseMethods
from pages.base_page import BasePage
from locators.inventory_page_locators import *
from env import *

import allure


class InventoryPage(BasePage, BaseMethods):

    # CART

    @allure.step('Добавить продукт в корзину.')
    def add_product_to_cart(self):
        self.click_element(locator=PRODUCT_1_CART)

    @allure.step('Удалить продукт из корзины.')
    def remove_product_from_cart(self):
        self.click_element(locator=PRODUCT_1_CART)

    @allure.step('Добавить все возможные продукты в корзину.')
    def add_all_products_to_cart(self):
        for cart_button in PRODUCT_CART_BUTTONS:
            self.click_element(locator=cart_button)

    @allure.step('Удалить все возможные продукты из корзины.')
    def remove_all_products_from_cart(self):
        for cart_button in PRODUCT_CART_BUTTONS:
            self.click_element(locator=cart_button)

    @allure.step('Проверить, что значок количества продуктов возле корзины показывает значение {value}.')
    def check_cart_badge_value_equal_(self, value):
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
        product_prices = self.get_list_of(data=PRODUCT_PRICES)
        product_prices = self.convert_to_float(product_prices)
        self.check_asc_sorting(product_prices)

    @allure.step('Проверить, что продукты сортируются по цене от наибольшей к наименьшей.')
    def check_products_sorted_by_price_desc(self):
        product_prices = self.get_list_of(data=PRODUCT_PRICES)
        product_prices = self.convert_to_float(product_prices)
        self.check_desc_sorting(product_prices)

    # PRODUCTS

    @allure.step('Проверить, что название продукта отображается корректно.')
    def check_product_name_shown(self, data):
        name, locator = data['Name'][0], data['Name'][1]
        self.check_element_has_text(locator=locator, data=name)

    @allure.step('Проверить, что описание продукта отображается корректно.')
    def check_product_description_shown(self, data):
        description, locator = data['Description'][0], data['Description'][1]
        self.check_element_has_text(locator=locator, data=description)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_product_price_shown(self, data):
        price, locator = data['Price'][0], data['Price'][1]
        self.check_element_has_text(locator=locator, data=price)

    @allure.step('Проверить, что отображается изображение продукта.')
    def check_product_image_shown(self, data):
        locator = data['Image']
        self.check_element_shown(locator=locator)

    @allure.step('Проверить, что отображается кнопка "Add o cart".')
    def check_add_to_cart_button_shown(self, data):
        locator = data['Add to cart Button']
        self.check_element_has_text(locator=locator, data='Add to cart')

    @allure.step('Открыть подробное описание продукта, кликнув на название продукта.')
    def expand_product_description_via_clicking_product_name(self, data):
        locator = data['Name'][1]
        self.click_element(locator=locator)

    @allure.step('Открыть подробное описание продукта, кликнув на изображение продукта.')
    def expand_product_description_via_clicking_product_image(self, data):
        locator = data['Image']
        self.click_element(locator=locator)

    @allure.step('Проверить, что открылась "Product Page".')
    def check_product_page_opened(self, data):
        item_order = data['Order']
        self.check_url(endpoint=PRODUCT_ENDPOINT+item_order)


