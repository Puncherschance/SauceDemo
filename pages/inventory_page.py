from pages.base_page import BasePage
from resources.resources import *

import allure


class InventoryPage(BasePage):

    # CART

    @allure.step('Добавить продукт в корзину.')
    def add_product_to_cart(self):
        self.click_element(locator=PRODUCT_1_CART)

    @allure.step('Добавить случайный продукт в корзину.')
    def add_random_product_to_cart(self, product: dict[str, str]):
        locator = product['Add to cart Button']
        self.click_element(locator=locator)

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

    # SORT_MENU

    @allure.step('Проверить, что присутствует поле выбора сортировки продуктов.')
    def check_sort_menu_shown(self):
        self.check_element_shown(locator=SORT_MENU)

    @allure.step('Кликнуть по меню сортировки.')
    def click_sort_menu(self):
        self.click_element(locator=SORT_MENU)

    @allure.step('Кликнуть по кнопке со значком треугольника в меню сортировки.')
    def click_sort_menu_button(self):
        self.click_element(locator=SORT_MENU_BUTTON)

    @allure.step('Проверить, что присутствуют все доступные опции сортировки продуктов.')
    def check_all_sorting_options_shown(self):
        self.check_element_has_text(locator=SORT_MENU, data='Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)')

    @allure.step('Отсортировать предметы по принципу {option}.')
    def sort_products_(self, option: str):
        self.click_element(locator=SORT_MENU)
        self.check_dropdown_option_shown(locator=SORT_MENU, data=option)
        self.select_dropdown_option(locator=SORT_MENU, data=option)

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
    def check_product_name_shown(self, product_data: dict[str, str]):
        name = product_data['Name'][0]
        locator = product_data['Name'][1]
        self.check_element_has_text(locator=locator, data=name)

    @allure.step('Проверить, что описание продукта отображается корректно.')
    def check_product_description_shown(self, product_data: dict[str, str]):
        description = product_data['Description'][0]
        locator = product_data['Description'][1]
        self.check_element_has_text(locator=locator, data=description)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_product_price_shown(self, product_data: dict[str, str]):
        price = product_data['Price'][0]
        locator = product_data['Price'][1]
        self.check_element_has_text(locator=locator, data=price)

    @allure.step('Проверить, что отображается изображение продукта.')
    def check_product_image_shown(self, product_data: dict[str, str]):
        locator = product_data['Image']
        self.check_element_shown(locator=locator)

    @allure.step('Проверить, что отображается кнопка "Add o cart".')
    def check_add_to_cart_button_shown(self, product_data: dict[str, str]):
        locator = product_data['Add to cart Button']
        self.check_element_has_text(locator=locator, data='Add to cart')

    @allure.step('Открыть подробное описание продукта, кликнув на название продукта.')
    def expand_product_description_via_clicking_product_name(self, product_data: dict[str, str]):
        locator = product_data['Name'][1]
        self.click_element(locator=locator)

    @allure.step('Открыть подробное описание продукта, кликнув на изображение продукта.')
    def expand_product_description_via_clicking_product_image(self, product_data: dict[str, str]):
        locator = product_data['Image']
        self.click_element(locator=locator)

    @allure.step('Проверить, что текст всех кнопок "Remove" изменился на "Add to сart".')
    def check_remove_buttons_return_to_initial_state(self):
        for item in INVENTORY_ITEMS:
            locator = item['Add to cart Button']
            self.check_element_has_text(locator=locator, data='Add to cart')

    # NAVIGATION

    @allure.step('Проверить, что пользователь переходит на страницу Product Page.')
    def check_product_page_opened(self, product_data: dict[str, str]):
        item_order = product_data['Order']
        self.check_url(endpoint=PRODUCT_ENDPOINT + item_order)
