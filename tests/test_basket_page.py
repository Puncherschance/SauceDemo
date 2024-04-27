from playwright.sync_api import Page
from pages.basket_page import BasketPage



class TestHeader:

    def test_swag_labs_tittle_presented(self, page: Page, auth_as_standard_user, open_basket_page):
        basket_page = BasketPage(page)
        basket_page.check_swag_labs_title_has_text_('Swag Labs')

    def test_your_cart_tittle_presented(self, page: Page, auth_as_standard_user, open_basket_page):
        basket_page = BasketPage(page)
        basket_page.check_your_cart_title_has_text_('Your Cart')


class TestCart:

    def test_qty_title_presented(self, page: Page, auth_as_standard_user, open_basket_page,):
        basket_page = BasketPage(page)
        basket_page.check_qty_title_has_text_('QTY')

    def test_description_title_presented(self, page: Page, auth_as_standard_user, open_basket_page):
        basket_page = BasketPage(page)
        basket_page.check_description_title_has_text_('Description')