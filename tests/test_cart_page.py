from playwright.sync_api import Page
from pages.cart_page import CartPage


class TestHeader:

    def test_swag_labs_tittle_presented(self, page: Page, auth_as_standard_user, open_basket_page):
        cart_page = CartPage(page)
        cart_page.check_swag_labs_title_has_text_('Swag Labs')

    def test_your_cart_tittle_presented(self, page: Page, auth_as_standard_user, open_basket_page):
        cart_page = CartPage(page)
        cart_page.check_your_cart_title_has_text_('Your Cart')


class TestCart:

    def test_qty_title_presented(self, page: Page, auth_as_standard_user, open_basket_page):
        cart_page = CartPage(page)
        cart_page.check_qty_title_has_text_('QTY')

    def test_description_title_presented(self, page: Page, auth_as_standard_user, open_basket_page):
        cart_page = CartPage(page)
        cart_page.check_description_title_has_text_('Description')

    def test_continue_shopping_button_leads_to_inventory_page(self, page: Page, auth_as_standard_user, open_basket_page):
        cart_page = CartPage(page)
        cart_page.check_continue_shopping_button_has_text_('Continue Shopping')
        cart_page.check_continue_shopping_button_leads_to_inventory_page()


class TestFooter:

    def test_twitter_icon_leads_to_twitter_page(self, page: Page, auth_as_standard_user, open_basket_page):
        cart_page = CartPage(page)
        cart_page.check_twitter_icon_redirect()

    def test_terms_of_service_has_text(self, page: Page, auth_as_standard_user, open_basket_page):
        cart_page = CartPage(page)
        cart_page.check_terms_of_service_has_text_('© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')