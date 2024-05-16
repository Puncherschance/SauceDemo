import allure
import pytest
from playwright.sync_api import Page

from resources.base_resources import *


@pytest.mark.usefixtures("random_product")
class TestHeader:

    @allure.title('Проверить, что отображается заголовок "Swag Labs".')
    def test_swag_labs_title_shown(self, page: Page, complete_page):
        complete_page.check_swag_labs_title_has_text_("Swag Labs")

    @allure.title('Проверить, что отображается заголовок "Checkout: Complete!".')
    def test_page_title_shown(self, page: Page, complete_page):
        complete_page.check_page_title_has_text_("Checkout: Complete!")


@pytest.mark.usefixtures("random_product")
class TestHamburgerMenu:

    @allure.title("Проверить, что отображается гамбургер-меню.")
    def test_hamburger_icon_shown(self, page: Page, complete_page):
        complete_page.check_hamburger_icon_shown()

    @allure.title("Проверить, что отображаются все опции гамбургер-меню.")
    @pytest.mark.parametrize("option", HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(
        self, page: Page, complete_page, option
    ):
        complete_page.open_hamburger_menu()
        complete_page.check_hamburger_option_has_text(option)

    @allure.title(
        'Проверить, что кнопка "All Items" редиректит пользователя на Inventory Page.'
    )
    def test_all_items_option_leads_to_inventory_page(self, page: Page, complete_page):
        complete_page.open_hamburger_menu()
        complete_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason="Баг. Падает ошибка 403 Forbidden при открытии страницы.")
    @allure.title(
        'Проверить, что кнопка "About" редиректит пользователя на About Page.'
    )
    def test_about_option_leads_to_about_page(self, page: Page, complete_page):
        complete_page.open_hamburger_menu()
        complete_page.check_about_option_leads_to_about_page()

    @allure.title(
        'Проверить, что кнопка "Logout" разлогинивает пользователя и редиректит на Login Page.'
    )
    def test_logout_option_leads_to_login_page_and_logout_user(
        self, page: Page, complete_page
    ):
        complete_page.open_hamburger_menu()
        complete_page.check_logout_option_leads_to_login_page()

    @allure.title(
        'Проверить, что кнопка "Reset App State" удаляет все продукты из корзины.'
    )
    def test_reset_option_remove_products_from_cart(self, page: Page, complete_page):
        complete_page.open_hamburger_menu()
        complete_page.click_reset_app_state_option()
        complete_page.check_cart_badge_value_not_shown()

    @allure.title("Проверить, что гамбургер-меню можно закрыть.")
    def test_close_hamburger_menu(self, page: Page, complete_page):
        complete_page.open_hamburger_menu()
        complete_page.check_close_hamburger_menu_button_shown()
        complete_page.close_hamburger_menu()
        complete_page.check_hamburger_menu_closed()


@pytest.mark.usefixtures("random_product")
class TestCart:

    @allure.title('Проверить, что присутствует иконка "Тележка".')
    def test_cart_icon_shown(self, page: Page, complete_page):
        complete_page.check_cart_icon_shown()
        complete_page.check_cart_badge_value_not_shown()


class TestOrderDispatched:

    @allure.title('Проверить, что присутствует изображение "Pony Express".')
    def test_pony_express_image_shown(self, page: Page, complete_page):
        complete_page.check_pony_express_image_shown()

    @allure.title("Проверить, что присутствует текст об успешном заказе.")
    def test_order_dispatched_info_shown(self, page: Page, complete_page):
        complete_page.check_order_dispatched_header_has_text_(
            "Thank you for your order!"
        )
        complete_page.check_order_dispatched_has_text_(
            "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        )

    @allure.title('Проверить, что присутствует кнопка "Back Home".')
    def test_back_home_button_shown(self, page: Page, complete_page):
        complete_page.check_back_home_button_has_text_("Back Home")

    @allure.title(
        'Проверить, что кнопка "Back Home" редиректит пользователя на страницу Inventory Page.'
    )
    def test_back_home_button_leads_to_inventory_page(self, page: Page, complete_page):
        complete_page.click_back_home_button()
        complete_page.check_inventory_page_opened()


class TestFooter:

    @allure.title("Проверить, что присутствует текст условий использования.")
    def test_terms_of_service_has_text(self, page: Page, complete_page):
        complete_page.check_terms_of_service_has_text_(
            "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        )

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Twitter" редиректит пользователя на страницу Twitter.'
    )
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, complete_page):
        complete_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Facebook" редиректит пользователя на страницу Facebook.'
    )
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, complete_page):
        complete_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "LinkedIn" редиректит пользователя на страницу LinkedIn.'
    )
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, complete_page):
        complete_page.check_linkedin_icon_leads_to_linkedin_page()
