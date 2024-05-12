from playwright.sync_api import Page
from resources.resources import *

import pytest
import allure


@pytest.mark.usefixtures('expand_description')
class TestHeader:

    @allure.title('Проверить, что отображается заголовок "Swag Labs".')
    def test_swag_labs_tittle_shown(self, page: Page, product_page):
        product_page.check_swag_labs_title_has_text_('Swag Labs')

    @allure.title('Проверить, что отображается кнопка "Back to Products".')
    def test_back_to_products_button_shown(self, page: Page, product_page):
        product_page.check_back_to_products_button_has_text_('Back to products')

    @allure.title('Проверить, что кнопка "Back to Products" редиректит пользователя на Inventory Page.')
    def test_back_to_products_button_leads_to_inventory_page(self, page: Page, product_page):
        product_page.check_back_to_products_button_leads_to_iventory_page()


@pytest.mark.usefixtures('expand_description')
class TestHamburgerMenu:

    @allure.title('Проверить, что отображается гамбургер-меню.')
    def test_hamburger_icon_shown(self, page: Page, product_page):
        product_page.check_hamburger_icon_shown()

    @allure.title('Проверить, что отображаются все опции гамбургер-меню.')
    @pytest.mark.parametrize('option', HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(self, page: Page, product_page, option):
        product_page.open_hamburger_menu()
        product_page.check_hamburger_option_has_text(option)

    @allure.title('Проверить, что кнопка "All Items" редиректит пользователя на Inventory Page.')
    def test_all_items_option_leads_to_inventory_page(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason='Баг. Падает ошибка 403 Forbidden при открытии страницы.')
    @allure.title('Проверить, что кнопка "About" редиректит пользователя на About Page.')
    def test_about_option_leads_to_about_page(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.check_about_option_leads_to_about_page()

    @allure.title('Проверить, что кнопка "Logout" разлогинивает пользователя и редиректит на Login Page.')
    def test_logout_option_leads_to_logout_page_and_logout_user(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.check_logout_option_leads_to_login_page()

    @pytest.mark.xfail(reason='Баг. После резета страницы состояние кнопки "Remove" не возвращается к исходному.')
    @allure.title('Проверить, что кнопка "Reset App State" удаляет все продукты из корзины.')
    def test_reset_app_state_option_remove_product_from_cart(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.add_product_to_cart()
        product_page.click_reset_app_state_option()
        product_page.check_cart_badge_value_not_shown()
        product_page.check_remove_button_not_shown()
        product_page.check_add_to_cart_button_has_text_('Add to cart')


@pytest.mark.usefixtures('expand_description')
class TestCart:

    @allure.title('Проверить, что отображается иконка "Тележка".')
    def test_cart_icon_shown(self, page: Page, product_page):
        product_page.check_cart_icon_shown()

    @allure.title('Проверить, что пустая корзина успешно открывается.')
    def test_open_empty_cart(self, page: Page, product_page):
        product_page.open_cart()
        product_page.check_cart_page_opened()

    @allure.title('Проверить, корзина с продуктами успешно открывается.')
    def test_open_cart_with_product(self, page: Page, product_page, expand_description):
        product_page.add_product_to_cart()
        product_page.open_cart()
        product_page.check_cart_page_opened_with_correct_product_data(expand_description)

    @allure.title('Проверить, что при добавлении продукта в корзину, бейджик на иконке "Тележка" изменяет значение.')
    def test_cart_badge_appeared_when_add_product(self, page: Page, product_page):
        product_page.check_cart_badge_value_not_shown()
        product_page.add_product_to_cart()
        product_page.check_cart_badge_value_equal_('1')
        product_page.remove_product_from_cart()
        product_page.check_cart_badge_value_not_shown()


@pytest.mark.usefixtures('expand_description')
class TestProduct:

    @allure.title('Проверить, что отображается корректное название продукта.')
    def test_product_name_shown(self, page: Page, product_page, expand_description):
        product_page.check_correct_product_name_shown(expand_description)

    @allure.title('Проверить, что отображается корректное описание продукта.')
    def test_product_description_shown(self, page: Page, product_page, expand_description):
        product_page.check_correct_product_description_shown(expand_description)

    @allure.title('Проверить, что отображается корректная цена продукта.')
    def test_product_price_shown(self, page: Page, product_page, expand_description):
        product_page.check_correct_product_price_shown(expand_description)

    @allure.title('Проверить, что отображается изображение продукта.')
    def test_product_image_shown(self, page: Page, product_page):
        product_page.check_product_image_shown()

    @allure.title('Проверить, что отображается кнопка "Add to cart", если продукт не в корзине.')
    def test_add_to_cart_button_shown(self, page: Page, product_page):
        product_page.check_add_to_cart_button_has_text_('Add to cart')

    @allure.title('Проверить, что отображается кнопка "Remove", если продукт в корзине.')
    def test_remove_button_shown(self, page: Page, product_page):
        product_page.add_product_to_cart()
        product_page.check_remove_button_has_text_('Remove')

    @allure.title('Проверить, что вновь отображается кнопка "Add to cart", если убрать продукт из корзины.')
    def test_remove_button_shown(self, page: Page, product_page):
        product_page.add_product_to_cart()
        product_page.remove_product_from_cart()
        product_page.check_add_to_cart_button_has_text_('Add to cart')


@pytest.mark.usefixtures('expand_description_with_random_product')
class TestFooter:

    @allure.title('Проверить, что присутствует текст условий использования.')
    def test_terms_of_service_has_text(self, page: Page, product_page):
        product_page.check_terms_of_service_has_text_('© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    @allure.title('Проверить, иконка "Twitter" редиректит пользователя на страницу Twitter.')
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, product_page):
        product_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    @allure.title('Проверить, иконка "Facebook" редиректит пользователя на страницу Facebook.')
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, product_page):
        product_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    @allure.title('Проверить, иконка "LinkedIn" редиректит пользователя на страницу LinkedIn.')
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, product_page):
        product_page.check_linkedin_icon_leads_to_linkedin_page()
