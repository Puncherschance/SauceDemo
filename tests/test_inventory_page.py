from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from resources.products import *

import pytest


class TestHeader:

    def test_swag_labs_tittle_presented(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_swag_labs_title_has_text_('Swag Labs')

    def test_products_tittle_presented(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_products_title_has_text_('Products')


class TestHamburgerMenu:

    def test_hamburger_icon_shown(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_hamburger_icon_shown()

    def test_all_items_option(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.open_hamburger_menu()
        inventory_page.check_all_items_option_has_text_('All Items')
        inventory_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason='Обнаружен баг на сайте!')
    def test_about_option(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.open_hamburger_menu()
        inventory_page.check_about_option_has_text_('About')
        inventory_page.check_about_option_leads_to_about_page()

    def test_logout_option(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.open_hamburger_menu()
        inventory_page.check_logout_option_has_text_('Logout')
        inventory_page.check_logout_option_leads_to_login_page()

    def test_reset_option(self, page: Page, auth_as_standard_user):
        pass


class TestSortMenu:

    def test_sort_menu_presented(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_sort_menu_shown()
        inventory_page.check_sort_menu_button_shown()

    def test_all_sorting_options_shown(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_all_sorting_options_shown()

    def test_alphabet_asc_sorting_correct(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.sort_products_('Name (A to Z)')
        inventory_page.check_products_sorted_by_alphabet_asc()

    def test_alphabet_desc_sorting_correct(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.sort_products_('Name (Z to A)')
        inventory_page.check_products_sorted_by_alphabet_desc()

    def test_price_asc_sorting_correct(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.sort_products_('Price (low to high)')
        inventory_page.check_products_sorted_by_price_asc()

    def test_price_desc_sorting_correct(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.sort_products_('Price (high to low)')
        inventory_page.check_products_sorted_by_price_desc()


class TestCart:

    def test_cart_presented(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_cart_icon_shown()

    def test_open_empty_cart(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.open_empty_cart()
        inventory_page.check_cart_page_opened()

    def test_cart_badge_appeared_when_add_product(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_cart_badge_value_not_shown()
        inventory_page.add_product_to_cart()
        inventory_page.check_cart_badge_value_equal_('1')
        inventory_page.remove_product_from_cart()
        inventory_page.check_cart_badge_value_not_shown()

    def test_cart_badge_appeared_when_add_all_products(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_cart_badge_value_not_shown()
        inventory_page.add_all_products_to_cart()
        inventory_page.check_cart_badge_value_equal_('6')
        inventory_page.remove_all_products_from_cart()
        inventory_page.check_cart_badge_value_not_shown()


class TestProducts:

    @pytest.mark.parametrize('data', INVENTORY_ITEMS)
    def test_all_products_presented(self, page: Page, auth_as_standard_user, data):
        inventory_page = InventoryPage(page)
        inventory_page.check_product_name(data)
        inventory_page.check_product_description(data)
        inventory_page.check_product_price(data)
        inventory_page.check_product_image(data)

    @pytest.mark.parametrize('data', INVENTORY_ITEMS)
    def test_product_description_expanded_when_click_product_name(self, page: Page, auth_as_standard_user, data):
        inventory_page = InventoryPage(page)
        inventory_page.expand_product_description_via_clicking_product_name(data)
        inventory_page.check_product_page_opened(data)

    @pytest.mark.parametrize('data', INVENTORY_ITEMS)
    def test_product_description_expanded_when_click_product_image(self, page: Page, auth_as_standard_user, data):
        inventory_page = InventoryPage(page)
        inventory_page.expand_product_description_via_clicking_product_image(data)
        inventory_page.check_product_page_opened(data)


class TestFooter:

    def test_terms_of_service_has_text(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_terms_of_service_has_text_('© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_linkedin_icon_leads_to_linkedin_page()
