import allure

from env import *
from locators.base_page_locators import *
from methods.base_methods import BaseMethods


class BasePage(BaseMethods):

    # TITLE

    @allure.step("Проверить, что присутствует текст заголовка: {text}.")
    def check_swag_labs_title_has_text_(self, text):
        self.check_element_has_text(locator=TITLE, data=text)

    @allure.step("Проверить, что присутствует текст заголовка: {text}.")
    def check_page_title_has_text_(self, text):
        self.check_element_has_text(locator=PAGE_TITLE, data=text)

    @allure.step("Проверить, что присутствует текст заголовка: {text}.")
    def check_qty_title_has_text_(self, text: str):
        self.check_element_has_text(locator=QTY, data=text)

    @allure.step("Проверить, что присутствует текст заголовка: {text}.")
    def check_description_title_has_text_(self, text: str):
        self.check_element_has_text(locator=DESCRIPTION, data=text)

    # HAMBURGER_MENU

    @allure.step("Проверить, что присутствует Гамбургер меню.")
    def check_hamburger_icon_shown(self):
        self.check_element_shown(locator=HAMBURGER)

    @allure.step("Открыть Гамбургер меню.")
    def open_hamburger_menu(self):
        self.click_element(locator=HAMBURGER)

    @allure.step(
        "Проверить, что в Гамбургер меню присутствует текст опции: {hamburger_data}."
    )
    def check_hamburger_option_has_text(self, hamburger_data: tuple[str]):
        name, locator = hamburger_data[0], hamburger_data[1]
        self.check_element_has_text(locator=locator, data=name)

    @allure.step('Кликнуть по опции "Reset App State".')
    def click_reset_app_state_option(self):
        self.click_element(locator=RESET)

    @allure.step(
        'Проверить, что кнопка "All Items" в гамбургер меню редиректит Пользователя на страницу "Inventory Page".'
    )
    def check_all_items_option_leads_to_iventory_page(self):
        self.click_element(locator=ALL_ITEMS)
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    @allure.step(
        'Проверить, что кнопка "Logout" в гамбургер меню редиректит Пользователя на страницу "Login Page".'
    )
    def check_logout_option_leads_to_login_page(self):
        self.click_element(locator=LOGOUT)
        self.check_url(endpoint=LOGIN_ENDPOINT)

    @allure.step(
        'Проверить, что кнопка "About" в гамбургер меню редиректит Пользователя на страницу "About Sauce Demo".'
    )
    def check_about_option_leads_to_about_page(self):
        self.click_element(locator=ABOUT)
        self.check_url(endpoint=ABOUT_ENDPOINT)

    @allure.step("Проверить, что присутствует кнопка закрытия гамбургер-меню.")
    def check_close_hamburger_menu_button_shown(self):
        self.check_element_shown(locator=CLOSE)

    @allure.step("Кликнуть по кнопке закрытия гамбургер-меню.")
    def close_hamburger_menu(self):
        self.click_element(locator=CLOSE)

    @allure.step("Проверить, что гамбургер-меню закрылось.")
    def check_hamburger_menu_closed(self):
        self.check_element_not_shown(locator=CLOSE)
        self.check_element_not_shown(locator=ALL_ITEMS)
        self.check_element_not_shown(locator=ABOUT)
        self.check_element_not_shown(locator=LOGOUT)
        self.check_element_not_shown(locator=RESET)

    # CART

    @allure.step('Проверить, что присутствует кнопка "Корзина".')
    def check_cart_icon_shown(self):
        self.check_element_shown(locator=TITLE)

    @allure.step("Открыть пустую корзину.")
    def open_cart(self):
        self.click_element(locator=CART)

    @allure.step("Проверить, что открывается пустая корзина.")
    def check_cart_page_opened(self):
        self.check_url(endpoint=CART_ENDPOINT)

    @allure.step("Проверить, что значок количества продуктов возле корзины скрыт.")
    def check_cart_badge_value_not_shown(self):
        self.check_element_not_shown(CART_BADGE)

    @allure.step(
        "Проверить, что значок количества продуктов возле корзины показывает значение {value}."
    )
    def check_cart_badge_value_equal_(self, value: str):
        self.check_element_has_text(locator=CART_BADGE, data=value)

    # FOOTER

    @allure.step("Проверить, что присутствует текст Условий Использования: {text}.")
    def check_terms_of_service_has_text_(self, text: str):
        self.check_element_has_text(locator=TERMS, data=text)

    @allure.step(
        'Проверить, что кнопка "Twitter" редиректит Пользователя на страницу "Twitter".'
    )
    def check_twitter_icon_leads_to_twitter_page(self):
        self.click_element(locator=TWITTER)
        self.check_outer_url(url=TWITTER_URL)

    @allure.step(
        'Проверить, что кнопка "Facebook" редиректит Пользователя на страницу "Facebook".'
    )
    def check_facebook_icon_leads_to_facebook_page(self):
        self.click_element(locator=FACEBOOK)
        self.check_outer_url(url=FACEBOOK_URL)

    @allure.step(
        'Проверить, что кнопка "LinkedIn" редиректит Пользователя на страницу "LinkedIn".'
    )
    def check_linkedin_icon_leads_to_linkedin_page(self):
        self.click_element(locator=LINKEDIN)
        self.check_outer_url(url=LINKEDIN_URL)

    # NAVIGATION

    @allure.step("Проверить, что пользователя редиректит на страницу Cart Page.")
    def check_cart_page_opened(self):
        self.check_url(endpoint=CART_ENDPOINT)

    @allure.step("Проверить, что пользователя редиректит на страницу Inventory Page.")
    def check_inventory_page_opened(self):
        self.check_url(endpoint=INVENTORY_ENDPOINT)

    @allure.step("Проверить, что пользователя редиректит на страницу Product Page.")
    def check_product_page_opened(self, product_data: dict[str, str]):
        item_order = product_data["Order"]
        self.check_url(endpoint=PRODUCT_ENDPOINT + item_order)
