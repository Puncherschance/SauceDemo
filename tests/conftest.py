import pytest
import time

from playwright.sync_api import Page
from pages.login_page import LoginPage
from env import *


@pytest.fixture()
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    page.set_viewport_size({'height': 768, 'width': 1024})
    yield page
    time.sleep(1)
    browser.close()

@pytest.fixture()
def open_login_page(page):
    login_page = LoginPage(page)
    login_page.open_login_page()

@pytest.fixture()
def auth_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.enter_username_(STANDARD_USER['username'])
    login_page.enter_password_(STANDARD_USER['password'])
    login_page.click_login_button()





