from playwright.sync_api import Page
from pages.product_page import ProductPage
from resources.products import *

import pytest


class TestHeader:

    def test_swag_labs_tittle_presented(self, page: Page, auth_as_standard_user, open_product_page):
        product_page = ProductPage(page)
        product_page.check_swag_labs_title_has_text_('Swag Labs')

    def test_back_to_products_tittle_presented(self, page: Page, auth_as_standard_user, open_product_page):
        product_page = ProductPage(page)
        product_page.check_back_to_products_title_has_text_('Back to products')

    def test_back_to_products_tittle_leads_to_inventory_page(self, page: Page, auth_as_standard_user, open_product_page):
        product_page = ProductPage(page)
        product_page.check_back_to_products_tittle_leads_to_iventory_page()
