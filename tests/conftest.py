from playwright.sync_api import Page
from methods.base_methods import BaseMethods
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
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


@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    yield login_page


@pytest.fixture()
def inventory_page(page, login_page):
    login_page.enter_username_(STANDARD_USER['username'])
    login_page.enter_password_(STANDARD_USER['password'])
    login_page.click_login_button()
    inventory_page = InventoryPage(page)
    yield inventory_page


@pytest.fixture()
def cart_page(page, inventory_page):
    inventory_page.open_cart()
    cart_page = CartPage(page)
    yield cart_page


@pytest.fixture()
def product_page(page):
    product_page = ProductPage(page)
    yield product_page


@pytest.fixture()
def expand_description_with_random_product(page, inventory_page):
    random_product = INVENTORY_ITEMS[BaseMethods.random_product()]
    inventory_page.expand_product_description_via_clicking_product_name(random_product)
    yield random_product

@pytest.fixture()
def proceed_to_cart_with_random_product(page, inventory_page):
    random_product = INVENTORY_ITEMS[BaseMethods.random_product()]
    inventory_page.add_random_product_to_cart(random_product)
    inventory_page.open_cart()
    yield random_product
