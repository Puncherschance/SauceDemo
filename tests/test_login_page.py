import pytest

from playwright.sync_api import Page
from pages.login_page import LoginPage
from env import *


class TestLoginPage:

    def test_all_page_elements_are_presented(self, set_up: Page):
        login_page = LoginPage(set_up)
        login_page.open_login_page()
        login_page.check_tittle_has_text_('Swag Labs')
        login_page.check_login_field_has_placeholder_('Username')
        login_page.check_password_field_has_placeholder_('Password1')
        login_page.check_login_button_is_shown()

    @pytest.mark.parametrize(('username', 'password'), AUTH_DATA)
    def test_successful_login(self, set_up: Page, username, password):
        login_page = LoginPage(set_up)
        login_page.open_login_page()
        login_page.enter_username_(username)
        login_page.enter_password_(password)
        login_page.click_login_button()
        login_page.check_inventory_page_opened()

    def test_validation_is_shown_if_empty_login_and_password(self, set_up: Page):
        login_page = LoginPage(set_up)
        login_page.open_login_page()
        login_page.click_login_button()
        login_page.check_validation_has_text_('Epic sadface: Username is required')

    def test_login_as_locked_user(self, set_up: Page):
        login_page = LoginPage(set_up)
        login_page.open_login_page()
        login_page.enter_username_(LOCKED_USER['username'])
        login_page.enter_password_(LOCKED_USER['password'])
        login_page.click_login_button()
        login_page.check_validation_has_text_('Epic sadface: Sorry, this user has been locked out.')
