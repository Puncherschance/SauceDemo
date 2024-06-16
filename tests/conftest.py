import pytest
from playwright.sync_api import Page

from env import *
from methods.base_methods import BaseMethods
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.overview_page import OverviewPage
from pages.product_page import ProductPage
from resources.inventory_page_resources import INVENTORY_ITEMS


@pytest.fixture(autouse=True)
def page(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page: Page = context.new_page()
    page.set_viewport_size({"height": 768, "width": 1024})
    yield page
    browser.close()


# LOGIN_PAGE


@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    yield login_page


# INVENTORY_PAGE


@pytest.fixture()
def inventory_page(page, login_page):
    login_page.enter_username_(STANDARD_USER["username"])
    login_page.enter_password_(STANDARD_USER["password"])
    login_page.click_login_button()
    inventory_page = InventoryPage(page)
    yield inventory_page


@pytest.fixture()
def expand_description(page, inventory_page):
    random_product = INVENTORY_ITEMS[BaseMethods.random_number()]
    inventory_page.expand_product_description_via_clicking_product_name(random_product)
    yield random_product


@pytest.fixture()
def random_product(page, inventory_page):
    random_product = INVENTORY_ITEMS[BaseMethods.random_number()]
    inventory_page.add_product_to_cart(random_product)
    inventory_page.open_cart()
    yield random_product


@pytest.fixture()
def two_random_products(page, inventory_page):
    random_product_1, random_product_2 = BaseMethods.random_numbers()
    inventory_page.add_product_to_cart(random_product_1)
    inventory_page.add_product_to_cart(random_product_2)
    yield random_product_1, random_product_2


@pytest.fixture()
def all_products(page, inventory_page):
    all_products = INVENTORY_ITEMS
    inventory_page.add_all_products_to_cart()
    yield all_products


# CART_PAGE


@pytest.fixture()
def product_from_product_page(page, product_page, expand_description):
    product_page.add_product_to_cart()
    product_page.open_cart()
    yield expand_description


@pytest.fixture()
def cart_page(page, inventory_page):
    inventory_page.open_cart()
    cart_page = CartPage(page)
    yield cart_page


# PRODUCT_PAGE


@pytest.fixture()
def product_page(page):
    product_page = ProductPage(page)
    yield product_page


# CHECKOUT_PAGE


@pytest.fixture()
def checkout_page(page, cart_page):
    cart_page.click_checkout_button()
    checkout_page = CheckoutPage(page)
    yield checkout_page


# OVERVIEW_PAGE


@pytest.fixture()
def overview_page(page, checkout_page):
    checkout_page.enter_first_name_("Test")
    checkout_page.enter_last_name_("User")
    checkout_page.enter_postal_code_("41000")
    checkout_page.click_continue_button()
    overview_page = OverviewPage(page)
    yield overview_page


# COMPLETE_PAGE


@pytest.fixture()
def complete_page(page, overview_page):
    overview_page.click_finish_button()
    complete_page = CompletePage(page)
    yield complete_page
