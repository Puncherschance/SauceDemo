from playwright.sync_api import Page
from methods.base_methods import BaseMethods
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from env import *
from resources.products import *

import pytest


@pytest.fixture(autouse=True)
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    page.set_viewport_size({'height': 768, 'width': 1024})
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
    login_page.enter_username_(STANDARD_USER['username'])
    login_page.enter_password_(STANDARD_USER['password'])
    login_page.click_login_button()
    inventory_page = InventoryPage(page)
    yield inventory_page


@pytest.fixture()
def expand_description_with_random_product(page, inventory_page):
    random_product = INVENTORY_ITEMS[BaseMethods.random_number()]
    inventory_page.expand_product_description_via_clicking_product_name(random_product)
    yield random_product


@pytest.fixture()
def proceed_to_cart_with_random_product(page, inventory_page):
    random_product = INVENTORY_ITEMS[BaseMethods.random_number()]
    inventory_page.add_random_product_to_cart(random_product)
    inventory_page.open_cart()
    yield random_product


@pytest.fixture()
def proceed_to_cart_with_two_random_products(page, inventory_page):
    random_product_1, random_product_2 = BaseMethods.random_numbers()
    inventory_page.add_random_product_to_cart(random_product_1)
    inventory_page.add_random_product_to_cart(random_product_2)
    inventory_page.open_cart()
    yield random_product_1, random_product_2


@pytest.fixture()
def proceed_to_cart_with_all_products(page, inventory_page):
    inventory_page.add_all_products_to_cart()
    inventory_page.open_cart()

# CART_PAGE


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
def checkout_page(page, proceed_to_cart_with_random_product, cart_page):
    cart_page.click_checkout_button()
    checkout_page = CheckoutPage(page)
    yield checkout_page
