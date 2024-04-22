from playwright.sync_api import Page
from pages.inventory_page import InventoryPage


class TestInventoryPage:

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
