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

    def test_about_option(self, page: Page, auth_as_standard_user):
        pass

    def test_logout_option(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.open_hamburger_menu()
        inventory_page.check_logout_option_has_text_('Logout')
        inventory_page.check_logout_option_leads_to_login_page()

    def test_reset_option(self, page: Page, auth_as_standard_user):
        pass


class TestBasket:

    def test_basket_presented(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_basket_icon_shown()

    def test_open_empty_basket(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.open_empty_basket()
        inventory_page.check_basket_page_opened()


class TestSortMenu:

    def test_sort_menu_presented(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_sort_menu_shown()
        inventory_page.check_sort_menu_button_shown()

class TestItems:

    @pytest.mark.parametrize('data', INVENTORY_ITEMS)
    def test_all_products_presented(self, page: Page, auth_as_standard_user, data):
        inventory_page = InventoryPage(page)
        inventory_page.check_product_title(data)
        inventory_page.check_product_description(data)
        inventory_page.check_product_price(data)
        inventory_page.check_product_image(data)


class TestFooter:

    def test_twitter_icon_leads_to_twitter_page(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_twitter_icon_redirect()

    def test_terms_of_service_has_text(self, page: Page, auth_as_standard_user):
        inventory_page = InventoryPage(page)
        inventory_page.check_terms_of_service_has_text_('© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')



