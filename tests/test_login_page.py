from playwright.sync_api import Page
from env import *


class TestHeader:

    def test_swag_labs_title_shown(self, page: Page, login_page):
        login_page.check_swag_labs_title_has_text_('Swag Labs')


class TestAuthForm:

    def test_auth_form_shown(self, page: Page, login_page):
        login_page.check_login_field_has_placeholder_('Username')
        login_page.check_password_field_has_placeholder_('Password')
        login_page.check_login_button_has_text_('Login')

    def test_successful_auth_when_login_as_standard_user(self, page: Page, login_page):
        login_page.enter_username_(STANDARD_USER['username'])
        login_page.enter_password_(STANDARD_USER['password'])
        login_page.click_login_button()
        login_page.check_inventory_page_opened()


class TestValidation:

    def test_validation_shown_if_empty_login_and_password(self, page: Page, login_page):
        login_page.click_login_button()
        login_page.check_validation_has_text_('Epic sadface: Username is required')

    def test_validation_shown_when_password_required(self, page: Page, login_page):
        login_page.enter_username_(STANDARD_USER['username'])
        login_page.click_login_button()
        login_page.check_validation_has_text_('Epic sadface: Password is required')

    def test_validation_shown_when_login_as_locked_user(self, page: Page, login_page):
        login_page.enter_username_(LOCKED_USER['username'])
        login_page.enter_password_(LOCKED_USER['password'])
        login_page.click_login_button()
        login_page.check_validation_has_text_('Epic sadface: Sorry, this user has been locked out.')

    def test_validation_shown_when_login_as_invalid_user(self, page: Page, login_page):
        login_page.enter_username_(INVALID_USER['username'])
        login_page.enter_password_(INVALID_USER['password'])
        login_page.click_login_button()
        login_page.check_validation_has_text_('Epic sadface: Username and password do not match any user in this service')

    def test_validation_message_may_be_closed(self, page: Page, login_page):
        login_page.click_login_button()
        login_page.close_validation()
        login_page.check_validation_not_shown()

    def test_inventory_page_reached_only_after_authorization(self, page, login_page):
        login_page.open_inventory_page_by_direct_link()
        login_page.check_validation_has_text_("Epic sadface: You can only access '/inventory.html' when you are logged in.")
