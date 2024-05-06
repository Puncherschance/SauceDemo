from playwright.sync_api import Page
from resources.hamburger_menu_options import *

import pytest

@pytest.mark.usefixtures('expand_description_with_random_product')
class TestHeader:

    def test_swag_labs_tittle_shown(self, page: Page, product_page):
        product_page.check_swag_labs_title_has_text_('Swag Labs')

    def test_back_to_products_button_shown(self, page: Page, product_page):
        product_page.check_back_to_products_button_has_text_('Back to products')

    def test_back_to_products_button_leads_to_inventory_page(self, page: Page, product_page):
        product_page.check_back_to_products_button_leads_to_iventory_page()


@pytest.mark.usefixtures('expand_description_with_random_product')
class TestHamburgerMenu:

    def test_hamburger_icon_shown(self, page: Page, product_page):
        product_page.check_hamburger_icon_shown()

    @pytest.mark.parametrize('option', HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(self, page: Page, product_page, option):
        product_page.open_hamburger_menu()
        product_page.check_hamburger_option_has_text(option)

    def test_all_items_option_leads_to_inventory_page(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason='Баг. Падает ошибка 403 Forbidden при открытии страницы.')
    def test_about_option_leads_to_about_page(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.check_about_option_leads_to_about_page()

    def test_logout_option_leads_to_logout_page_and_logout_user(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.check_logout_option_leads_to_login_page()

    @pytest.mark.xfail(reason='Баг. После резета страницы состояние кнопки "Remove" не возвращается к исходному.')
    def test_reset_app_state_option_remove_products_from_cart(self, page: Page, product_page):
        product_page.open_hamburger_menu()
        product_page.add_product_to_cart()
        product_page.click_reset_app_state_option()
        product_page.check_cart_badge_value_not_shown()
        product_page.check_remove_button_not_shown()
        product_page.check_add_to_cart_button_has_text_('Add to cart')


@pytest.mark.usefixtures('expand_description_with_random_product')
class TestCart:

    def test_cart_icon_shown(self, page: Page, product_page):
        product_page.check_cart_icon_shown()

    def test_open_empty_cart(self, page: Page, product_page):
        product_page.open_empty_cart()
        product_page.check_cart_page_opened()

    def test_cart_badge_appeared_when_add_product(self, page: Page, product_page):
        product_page.check_cart_badge_value_not_shown()
        product_page.add_product_to_cart()
        product_page.check_cart_badge_value_equal_('1')
        product_page.remove_product_from_cart()
        product_page.check_cart_badge_value_not_shown()


@pytest.mark.usefixtures('expand_description_with_random_product')
class TestProduct:

    def test_product_name_shown(self, page: Page, product_page, expand_description_with_random_product):
        product_page.check_correct_product_name_shown(expand_description_with_random_product)

    def test_product_description_shown(self, page: Page, product_page, expand_description_with_random_product):
        product_page.check_correct_product_description_shown(expand_description_with_random_product)

    def test_product_price_shown(self, page: Page, product_page, expand_description_with_random_product):
        product_page.check_correct_product_price_shown(expand_description_with_random_product)

    def test_product_image_shown(self, page: Page, product_page):
        product_page.check_product_image_shown()

    def test_add_to_cart_button_shown(self, page: Page, product_page):
        product_page.check_add_to_cart_button_has_text_('Add to cart')

    def test_remove_button_shown(self, page: Page, product_page):
        product_page.add_product_to_cart()
        product_page.check_remove_button_has_text_('Remove')



@pytest.mark.usefixtures('expand_description_with_random_product')
class TestFooter:

    def test_terms_of_service_has_text(self, page: Page, product_page):
        product_page.check_terms_of_service_has_text_('© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, product_page):
        product_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, product_page):
        product_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, product_page):
        product_page.check_linkedin_icon_leads_to_linkedin_page()
