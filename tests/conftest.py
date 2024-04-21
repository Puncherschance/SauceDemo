import pytest
import time

from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture()
def set_up(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    page.set_viewport_size({'height': 768, 'width': 1024})
    yield page
    time.sleep(1)
    browser.close()

@pytest.fixture()
def xz(page, set_up):
    print('LOL')
    login_page = LoginPage(page)
    login_page.open_login_page()
    print('LOL2')
    yield login_page
