from playwright.sync_api import Page

import pytest


class TestHeader:

    def test_swag_labs_tittle_presented(self, page: Page, cart_page):
        cart_page.check_swag_labs_title_has_text_('Swag Labs')

    def test_page_tittle_presented(self, page: Page, cart_page):
        cart_page.check_page_title_has_text_('Your Cart')


class TestCart:

    def test_qty_title_presented(self, page: Page, cart_page):
        cart_page.check_qty_title_has_text_('QTY')

    def test_description_title_presented(self, page: Page, cart_page):
        cart_page.check_description_title_has_text_('Description')

    def test_continue_shopping_button_leads_to_inventory_page(self, page: Page, cart_page):
        cart_page.check_continue_shopping_button_has_text_('Continue Shopping')
        cart_page.check_continue_shopping_button_leads_to_inventory_page()

    def test_checkout_button_presented(self, page: Page, cart_page):
        cart_page.check_checkout_button_has_text_('Checkout')

    def test_checkout_with_empty_basket(self, page: Page, cart_page):
        cart_page.click_checkout_button()
        #cart_page.check_checkout_page_not_opened()


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