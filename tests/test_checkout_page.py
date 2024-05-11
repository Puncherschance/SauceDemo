from playwright.sync_api import Page
from resources.hamburger_menu_options import *

import pytest
import allure


class TestHeader:

    @allure.title('Проверить, что отображается заголовок "Swag Labs".')
    def test_swag_labs_tittle_shown(self, page: Page, checkout_page):
        checkout_page.check_swag_labs_title_has_text_('Swag Labs')

    @allure.title('Проверить, что отображается заголовок "Checkout: Your Information".')
    def test_page_tittle_shown(self, page: Page, checkout_page):
        checkout_page.check_page_title_has_text_('Checkout: Your Information')


class TestHamburgerMenu:

    @allure.title('Проверить, что отображается гамбургер-меню.')
    def test_hamburger_icon_shown(self, page: Page, checkout_page):
        checkout_page.check_hamburger_icon_shown()

    @allure.title('Проверить, что отображаются все опции гамбургер-меню.')
    @pytest.mark.parametrize('option', HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(self, page: Page, checkout_page, option):
        checkout_page.open_hamburger_menu()
        checkout_page.check_hamburger_option_has_text(option)

    @allure.title('Проверить, что кнопка "All Items" редиректит пользователя на Inventory Page.')
    def test_all_items_option_leads_to_inventory_page(self, page: Page, checkout_page):
        checkout_page.open_hamburger_menu()
        checkout_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason='Баг. Падает ошибка 403 Forbidden при открытии страницы.')
    @allure.title('Проверить, что кнопка "About" редиректит пользователя на About Page.')
    def test_about_option_leads_to_about_page(self, page: Page, checkout_page):
        checkout_page.open_hamburger_menu()
        checkout_page.check_about_option_leads_to_about_page()

    @allure.title('Проверить, что кнопка "Logout" разлогинивает пользователя и редиректит на Login Page.')
    def test_logout_option_leads_to_login_page_and_logout_user(self, page: Page, checkout_page):
        checkout_page.open_hamburger_menu()
        checkout_page.check_logout_option_leads_to_login_page()

    @allure.title('Проверить, что кнопка "Reset App State" удаляет все продукты из корзины.')
    def test_reset_option_remove_products_from_cart(self, page: Page, checkout_page):
        checkout_page.open_hamburger_menu()
        checkout_page.click_reset_app_state_option()
        checkout_page.check_cart_badge_value_not_shown()


class TestCart:

    @allure.title('Проверить, что присутствует иконка "Тележка".')
    def test_cart_icon_shown(self, page: Page, checkout_page):
        checkout_page.check_cart_icon_shown()

    @allure.title('Проверить, что бейджик на иконке "Тележка" изменяет значение, если у пользователя есть продукт в корзине.')
    def test_cart_badge_shown_when_product_added(self, page: Page, checkout_page):
        checkout_page.check_cart_badge_value_equal_('1')


class TestRequisites:

    @allure.title('Проверить, что присутствует форма ввода реквизитов.')
    def test_requisites_form_shown(self, page: Page, checkout_page):
        checkout_page.check_first_name_field_has_placeholder_('First Name')
        checkout_page.check_last_name_field_has_placeholder_('Last Name')
        checkout_page.check_postal_field_has_placeholder_('Zip/Postal Code')

    @allure.title('Проверить, что присутствует кнопка "Continue".')
    def test_continue_button_shown(self, page: Page, checkout_page):
        checkout_page.check_continue_button_has_text_('Continue')

    @allure.title('Проверить, что присутствует кнопка "Cancel".')
    def test_cancel_button_shown(self, page: Page, checkout_page):
        checkout_page.check_cancel_button_has_text_('Cancel')

    @allure.title('Проверить, что кнопка "Cancel" редиректит пользователя на страницу Cart Page.')
    def test_cancel_button_leads_to_cart_page(self, page: Page, checkout_page):
        checkout_page.click_cancel_button()
        checkout_page.check_cart_page_opened()


class TestValidation:

    @allure.title('Проверить, что появляется валидация, если попытаться перейти к покупке, оставив все поля пустыми на форме ввода реквизитов.')
    def test_validation_shown_if_proceed_checkout_with_empty_data(self, page: Page, checkout_page):
        checkout_page.click_continue_button()
        checkout_page.check_validation_has_text_('Error: First Name is required')

    @allure.title('Проверить, что появляется валидация, если попытаться перейти к покупке, оставив поле "First Name" пустым на форме ввода реквизитов.')
    def test_validation_shown_if_proceed_checkout_with_empty_first_name(self, page: Page, checkout_page):
        checkout_page.enter_last_name_('User')
        checkout_page.enter_postal_code_('41000')
        checkout_page.click_continue_button()
        checkout_page.check_validation_has_text_('Error: First Name is required')

    @allure.title('Проверить, что появляется валидация, если попытаться перейти к покупке, оставив поле "Last Name" пустым на форме ввода реквизитов.')
    def test_validation_shown_if_proceed_checkout_with_empty_last_name(self, page: Page, checkout_page):
        checkout_page.enter_first_name_('User')
        checkout_page.enter_postal_code_('41000')
        checkout_page.click_continue_button()
        checkout_page.check_validation_has_text_('Error: Last Name is required')

    @allure.title('Проверить, что появляется валидация, если попытаться перейти к покупке, оставив поле "Zip/Postal Code" пустым на форме ввода реквизитов.')
    def test_validation_shown_if_proceed_checkout_with_empty_postal_code(self, page: Page, checkout_page):
        checkout_page.enter_first_name_('User')
        checkout_page.enter_last_name_('User')
        checkout_page.click_continue_button()
        checkout_page.check_validation_has_text_('Error: Postal Code is required')

    @allure.title('Проверить, что валидацию можно закрыть.')
    def test_validation_message_may_be_closed(self, page: Page, checkout_page):
        checkout_page.click_continue_button()
        checkout_page.close_validation()
        checkout_page.check_validation_not_shown()


class TestFooter:

    @allure.title('Проверить, что присутствует текст условий использования.')
    def test_terms_of_service_has_text(self, page: Page, checkout_page):
        checkout_page.check_terms_of_service_has_text_('© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    @allure.title('Проверить, иконка "Twitter" редиректит пользователя на страницу Twitter.')
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, checkout_page):
        checkout_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    @allure.title('Проверить, иконка "Facebook" редиректит пользователя на страницу Facebook.')
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, checkout_page):
        checkout_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip('Проверка недоступна без ВПН!')
    @allure.title('Проверить, иконка "LinkedIn" редиректит пользователя на страницу LinkedIn.')
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, checkout_page):
        checkout_page.check_linkedin_icon_leads_to_linkedin_page()
