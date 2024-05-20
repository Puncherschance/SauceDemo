import allure
import pytest
from playwright.sync_api import Page

from resources.base_resources import *


class TestHeader:

    @allure.title('Проверить, что отображается заголовок "Swag Labs".')
    def test_swag_labs_title_shown(self, page: Page, cart_page):
        cart_page.check_swag_labs_title_has_text_("Swag Labs")

    @allure.title('Проверить, что отображается заголовок "Your Cart".')
    def test_page_title_shown(self, page: Page, cart_page):
        cart_page.check_page_title_has_text_("Your Cart")


class TestHamburgerMenu:

    @allure.title("Проверить, что отображается гамбургер-меню.")
    def test_hamburger_icon_shown(self, page: Page, cart_page):
        cart_page.check_hamburger_icon_shown()

    @allure.title("Проверить, что отображаются все опции гамбургер-меню.")
    @pytest.mark.parametrize("option", HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(
        self, page: Page, cart_page, option
    ):
        cart_page.open_hamburger_menu()
        cart_page.check_hamburger_option_has_text(option)

    @allure.title(
        'Проверить, что кнопка "All Items" редиректит пользователя на Inventory Page.'
    )
    def test_all_items_option_leads_to_inventory_page(self, page: Page, cart_page):
        cart_page.open_hamburger_menu()
        cart_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason="Баг. Падает ошибка 403 Forbidden при открытии страницы.")
    @allure.title(
        'Проверить, что кнопка "About" редиректит пользователя на About Page.'
    )
    def test_about_option_leads_to_about_page(self, page: Page, cart_page):
        cart_page.open_hamburger_menu()
        cart_page.check_about_option_leads_to_about_page()

    @allure.title(
        'Проверить, что кнопка "Logout" разлогинивает пользователя и редиректит на Login Page.'
    )
    def test_logout_option_leads_to_login_page_and_logout_user(
        self, page: Page, cart_page
    ):
        cart_page.open_hamburger_menu()
        cart_page.check_logout_option_leads_to_login_page()

    @pytest.mark.xfail(
        reason="Баг. После резета страницы информация по продукту продолжает отображаться."
    )
    @allure.title(
        'Проверить, что кнопка "Reset App State" удаляет все продукты из корзины.'
    )
    def test_reset_option_remove_products_from_cart(
        self, page: Page, random_product, cart_page
    ):
        cart_page.open_hamburger_menu()
        cart_page.click_reset_app_state_option()
        cart_page.check_cart_badge_value_not_shown()
        cart_page.check_product_data_not_shown()

    @allure.title("Проверить, что гамбургер-меню можно закрыть.")
    def test_close_hamburger_menu(self, page: Page, random_product, cart_page):
        cart_page.open_hamburger_menu()
        cart_page.check_close_hamburger_menu_button_shown()
        cart_page.close_hamburger_menu()
        cart_page.check_hamburger_menu_closed()


class TestCart:

    @allure.title('Проверить, что присутствует иконка "Тележка".')
    def test_cart_icon_shown(self, page: Page, cart_page):
        cart_page.check_cart_icon_shown()

    @allure.title('Проверить, что присутствует текст "QTY".')
    def test_qty_title_shown(self, page: Page, cart_page):
        cart_page.check_qty_title_has_text_("QTY")

    @allure.title('Проверить, что присутствует текст "Description".')
    def test_description_title_shown(self, page: Page, cart_page):
        cart_page.check_description_title_has_text_("Description")

    @allure.title('Проверить, что присутствует кнопка "Continue Shopping".')
    def test_continue_shopping_button_shown(self, page: Page, cart_page):
        cart_page.check_continue_shopping_button_has_text_("Continue Shopping")

    @allure.title(
        'Проверить, что бейджик на иконке "Тележка" не отображается, если у пользователя пустая корзина.'
    )
    def test_cart_icon_shown_without_badge_when_empty_cart(self, page: Page, cart_page):
        cart_page.check_cart_badge_value_not_shown()

    @allure.title(
        'Проверить, что кнопка "Continue Shopping" редиректит пользователя на страницу Inventory page.'
    )
    def test_continue_shopping_button_leads_to_inventory_page(
        self, page: Page, cart_page
    ):
        cart_page.check_continue_shopping_button_leads_to_inventory_page()

    @allure.title(
        'Проверить, что пользователь остается на странице Cart page, если кликнуть на иконку "Тележка".'
    )
    def test_user_stays_on_cart_page_when_click_cart_icon(self, page: Page, cart_page):
        cart_page.open_cart()
        cart_page.check_user_stays_on_cart_page()

    @allure.title('Проверить, что присутствует кнопка "Checkout".')
    def test_checkout_button_shown(self, page: Page, cart_page):
        cart_page.check_checkout_button_has_text_("Checkout")

    @pytest.mark.xfail(
        reason="Баг. Переход на страницу Checkout с пустой корзиной должен быть запрещен."
    )
    @allure.title(
        "Проверить, что пользователь не переходит к покупке с пустой корзиной."
    )
    def test_proceed_checkout_with_empty_cart_not_possible(self, page: Page, cart_page):
        cart_page.click_checkout_button()
        cart_page.check_user_stays_on_cart_page()


class TestCartWithSingleProduct:

    @allure.title(
        'Проверить, что бейджик на иконке "Тележка" присутствует со значением "1", если у пользователя есть продукт в '
        'корзине.'
    )
    def test_cart_icon_shown_with_badge_when_product_in_cart(
        self, page: Page, random_product, cart_page
    ):
        cart_page.check_cart_badge_value_equal_("1")

    @allure.title("Проверить, что отображается корректное название продукта.")
    def test_product_name_shown(self, page: Page, random_product, cart_page):
        cart_page.check_product_name_has_correct_text(random_product)

    @allure.title("Проверить, что отображается корректное описание продукта.")
    def test_product_description_shown(self, page: Page, random_product, cart_page):
        cart_page.check_product_description_has_correct_text(random_product)

    @allure.title("Проверить, что отображается корректная цена продукта.")
    def test_product_price_shown(self, page: Page, random_product, cart_page):
        cart_page.check_product_has_correct_price(random_product)

    @allure.title("Проверить, что отображается корректное количество продукта.")
    def test_product_qty_shown(self, page: Page, random_product, cart_page):
        cart_page.check_product_has_qty_("1")

    @allure.title(
        'Проверить, что присутствует кнопка "Remove", если у пользователя есть продукты в корзине.'
    )
    def test_remove_button_shown(self, page: Page, random_product, cart_page):
        cart_page.check_remove_button_has_text_("Remove")

    @allure.title(
        "Проверить, что клик по названию продукта редиректит пользователя на страницу Product Page."
    )
    def test_click_on_product_name_leads_to_product_page(
        self, page: Page, random_product, cart_page
    ):
        cart_page.click_product_name()
        cart_page.check_product_page_opened(random_product)

    @allure.title(
        'Проверить, что кнопка "Checkout" редиректит пользователя на страницу Checkout Page.'
    )
    def test_proceed_checkout_with_product(self, page: Page, random_product, cart_page):
        cart_page.click_checkout_button()
        cart_page.check_checkout_page_opened()

    @allure.title(
        'Проверить, что продукт добавляется в корзину, будучи добавленным на странице Product Page.'
    )
    def test_add_product_from_product_page(self, page: Page, product_from_product_page, cart_page):
        print(product_from_product_page)
        cart_page.check_product_name_has_correct_text(product_from_product_page)
        cart_page.check_product_description_has_correct_text(product_from_product_page)
        cart_page.check_product_has_correct_price(product_from_product_page)
        cart_page.check_product_has_qty_("1")


class TestCartWithMultipleProducts:

    @allure.title(
        'Проверить, что бейджик на иконке "Тележка" присутствует со значением "2", если у пользователя есть два '
        'продукта в корзине.'
    )
    def test_cart_icon_shown_with_badge_when_product_in_cart(
        self, page: Page, two_random_products, cart_page
    ):
        cart_page.check_cart_badge_value_equal_("2")

    @allure.title("Проверить, что отображаются корректные названия продуктов.")
    def test_product_names_shown(self, page: Page, two_random_products, cart_page):
        cart_page.check_product_names_has_correct_text(two_random_products)

    @allure.title("Проверить, что отображаются корректные описания продуктов.")
    def test_product_descriptions_shown(
        self, page: Page, two_random_products, cart_page
    ):
        cart_page.check_product_descriptions_has_correct_text(two_random_products)

    @allure.title("Проверить, что отображаются корректные цены продуктов.")
    def test_product_prices_shown(self, page: Page, two_random_products, cart_page):
        cart_page.check_products_has_correct_prices(two_random_products)

    @allure.title("Проверить, что отображается корректное количество продуктов.")
    def test_products_qty_shown(self, page: Page, two_random_products, cart_page):
        cart_page.check_products_has_qty_("1")

    @allure.title("Проверить, что в корзине умещается максимум продуктов.")
    def test_all_products_fit_on_page(self, page: Page, all_products, cart_page):
        cart_page.check_cart_badge_value_equal_("6")
        cart_page.check_remove_buttons_qty_(6)


class TestFooter:

    @allure.title("Проверить, что присутствует текст условий использования.")
    def test_terms_of_service_has_text(self, page: Page, cart_page):
        cart_page.check_terms_of_service_has_text_(
            "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        )

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Twitter" редиректит пользователя на страницу Twitter.'
    )
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, cart_page):
        cart_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Facebook" редиректит пользователя на страницу Facebook.'
    )
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, cart_page):
        cart_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "LinkedIn" редиректит пользователя на страницу LinkedIn.'
    )
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, cart_page):
        cart_page.check_linkedin_icon_leads_to_linkedin_page()
