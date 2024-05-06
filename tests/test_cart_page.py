from playwright.sync_api import Page
from resources.hamburger_menu_options import *

import pytest


class TestHeader:

    def test_swag_labs_tittle_shown(self, page: Page, cart_page):
        cart_page.check_swag_labs_title_has_text_('Swag Labs')

    def test_page_tittle_shown(self, page: Page, cart_page):
        cart_page.check_page_title_has_text_('Your Cart')


class TestHamburgerMenu:

    def test_hamburger_icon_shown(self, page: Page, cart_page):
        cart_page.check_hamburger_icon_shown()

    @pytest.mark.parametrize('option', HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(self, page: Page, cart_page, option):
        cart_page.open_hamburger_menu()
        cart_page.check_hamburger_option_has_text(option)

    def test_all_items_option_leads_to_inventory_page(self, page: Page, cart_page):
        cart_page.open_hamburger_menu()
        cart_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason='Баг. Падает ошибка 403 Forbidden при открытии страницы.')
    def test_about_option_leads_to_about_page(self, page: Page, cart_page):
        cart_page.open_hamburger_menu()
        cart_page.check_about_option_leads_to_about_page()

    def test_logout_option_leads_to_login_page_and_logout_user(self, page: Page, cart_page):
        cart_page.open_hamburger_menu()
        cart_page.check_logout_option_leads_to_login_page()

    @pytest.mark.xfail(reason='Баг. После резета страницы состояние кнопки "Remove" не возвращается к исходному.')
    def test_reset_option_remove_products_from_cart(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.open_hamburger_menu()
        cart_page.click_reset_app_state_option()
        cart_page.check_cart_badge_value_not_shown()
        #cart_page.check_add_to_cart_button_has_text_('Add to cart')


class TestCart:

    def test_qty_title_shown(self, page: Page, cart_page):
        cart_page.check_qty_title_has_text_('QTY')

    def test_description_title_shown(self, page: Page, cart_page):
        cart_page.check_description_title_has_text_('Description')

    def test_continue_shopping_button_shown(self, page: Page, cart_page):
        cart_page.check_continue_shopping_button_has_text_('Continue Shopping')

    def test_cart_icon_shown_without_badge_when_empty_cart(self, page: Page, cart_page):
        cart_page.check_cart_icon_shown()
        cart_page.check_cart_badge_value_not_shown()

    def test_continue_shopping_button_leads_to_inventory_page(self, page: Page, cart_page):
        cart_page.check_continue_shopping_button_leads_to_inventory_page()

    def test_user_stays_on_cart_page_when_click_cart_icon(self, page: Page, cart_page):
        cart_page.open_cart()
        cart_page.check_user_stays_on_cart_page()

    def test_checkout_button_shown(self, page: Page, cart_page):
        cart_page.check_checkout_button_has_text_('Checkout')

    @pytest.mark.xfail(reason='Баг. Переход на страницу Checkout с пустой корзиной должен быть запрещен.')
    def test_checkout_with_empty_cart_not_possible(self, page: Page, cart_page):
        cart_page.click_checkout_button()
        cart_page.check_user_stays_on_cart_page()


class TestCartWithProducts:

    def test_cart_icon_shown_with_badge_when_product_in_cart(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.check_cart_icon_shown()
        cart_page.check_cart_badge_value_equal_('1')

    def test_product_name_shown(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.check_product_name_has_correct_text(proceed_to_cart_with_random_product)

    def test_product_description_shown(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.check_product_description_has_correct_text(proceed_to_cart_with_random_product)

    def test_product_price_shown(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.check_product_has_correct_price(proceed_to_cart_with_random_product)

    def test_product_qty_shown(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.check_product_has_qty_('1')

    def test_remove_button_shown(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.check_remove_button_has_text_('Remove')

    def test_click_on_product_name_leads_to_product_page(self, page: Page, proceed_to_cart_with_random_product, cart_page):
        cart_page.click_product_name()
        cart_page.check_product_page_opened_with_correct_product_data(proceed_to_cart_with_random_product)


class TestFooter:

    def test_terms_of_service_has_text(self, page: Page, cart_page):
        cart_page.check_terms_of_service_has_text_('© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, cart_page):
        cart_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, cart_page):
        cart_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, cart_page):
        cart_page.check_linkedin_icon_leads_to_linkedin_page()