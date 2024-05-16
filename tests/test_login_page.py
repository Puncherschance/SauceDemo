import allure
import pytest
from playwright.sync_api import Page

from env import *
from resources.login_page_resources import PAGES


class TestHeader:

    @allure.title('Проверить, что отображается заголовок "Swag Labs".')
    def test_swag_labs_title_shown(self, page: Page, login_page):
        login_page.check_swag_labs_title_has_text_("Swag Labs")


class TestAuthForm:

    @allure.title("Проверить, что корректно отображается форма авторизации.")
    def test_auth_form_shown(self, page: Page, login_page):
        login_page.check_login_field_has_placeholder_("Username")
        login_page.check_password_field_has_placeholder_("Password")
        login_page.check_login_button_has_text_("Login")

    @allure.title(
        "Проверить, что удается успешно авторизоваться в систему стандартным пользователем."
    )
    def test_successful_auth_when_login_as_standard_user(self, page: Page, login_page):
        login_page.enter_username_(STANDARD_USER["username"])
        login_page.enter_password_(STANDARD_USER["password"])
        login_page.click_login_button()
        login_page.check_inventory_page_opened()


class TestValidation:

    @allure.title(
        "Проверить, что отображается валидация, если не вводить логин и пароль."
    )
    def test_validation_shown_if_empty_login_and_password(self, page: Page, login_page):
        login_page.click_login_button()
        login_page.check_validation_has_text_("Epic sadface: Username is required")

    @allure.title("Проверить, что отображается валидация, если не ввести пароль.")
    def test_validation_shown_when_password_required(self, page: Page, login_page):
        login_page.enter_username_(STANDARD_USER["username"])
        login_page.click_login_button()
        login_page.check_validation_has_text_("Epic sadface: Password is required")

    @allure.title(
        "Проверить, что отображается валидация, если попытаться авторизоваться в систему заблокированным пользователем."
    )
    def test_validation_shown_when_login_as_locked_user(self, page: Page, login_page):
        login_page.enter_username_(LOCKED_USER["username"])
        login_page.enter_password_(LOCKED_USER["password"])
        login_page.click_login_button()
        login_page.check_validation_has_text_(
            "Epic sadface: Sorry, this user has been locked out."
        )

    @allure.title(
        "Проверить, что отображается валидация, если попытаться авторизоваться в систему с некорректными реквизитами."
    )
    def test_validation_shown_when_login_as_invalid_user(self, page: Page, login_page):
        login_page.enter_username_(INVALID_USER["username"])
        login_page.enter_password_(INVALID_USER["password"])
        login_page.click_login_button()
        login_page.check_validation_has_text_(
            "Epic sadface: Username and password do not match any user in this service"
        )

    @allure.title("Проверить, что валидацию можно закрыть.")
    def test_validation_message_may_be_closed(self, page: Page, login_page):
        login_page.click_login_button()
        login_page.close_validation()
        login_page.check_validation_not_shown()

    @allure.title(
        "Проверить, что остальные страницы доступны только после авторизации."
    )
    @pytest.mark.parametrize("page_endpoint", PAGES)
    def test_page_reached_only_after_authorization(
        self, page, login_page, page_endpoint
    ):
        login_page.open_page_by_direct_url(page_endpoint)
        login_page.check_validation_has_text_(
            f"Epic sadface: You can only access '/{page_endpoint}' when you are logged in."
        )
