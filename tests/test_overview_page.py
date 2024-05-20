import allure
import pytest
from playwright.sync_api import Page

from resources.base_resources import *


@pytest.mark.usefixtures("random_product")
class TestHeader:

    @allure.title('Проверить, что отображается заголовок "Swag Labs".')
    def test_swag_labs_title_shown(self, page: Page, overview_page):
        overview_page.check_swag_labs_title_has_text_("Swag Labs")

    @allure.title('Проверить, что отображается заголовок "Checkout: Overview".')
    def test_swag_labs_title_shown(self, page: Page, overview_page):
        overview_page.check_page_title_has_text_("Checkout: Overview")


@pytest.mark.usefixtures("random_product")
class TestHamburgerMenu:

    @allure.title("Проверить, что отображается гамбургер-меню.")
    def test_hamburger_icon_shown(self, page: Page, overview_page):
        overview_page.check_hamburger_icon_shown()

    @allure.title("Проверить, что отображаются все опции гамбургер-меню.")
    @pytest.mark.parametrize("option", HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(
        self, page: Page, overview_page, option
    ):
        overview_page.open_hamburger_menu()
        overview_page.check_hamburger_option_has_text(option)

    @allure.title(
        'Проверить, что кнопка "All Items" редиректит пользователя на Inventory Page.'
    )
    def test_all_items_option_leads_to_inventory_page(self, page: Page, overview_page):
        overview_page.open_hamburger_menu()
        overview_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason="Баг. Падает ошибка 403 Forbidden при открытии страницы.")
    @allure.title(
        'Проверить, что кнопка "About" редиректит пользователя на About Page.'
    )
    def test_about_option_leads_to_about_page(self, page: Page, overview_page):
        overview_page.open_hamburger_menu()
        overview_page.check_about_option_leads_to_about_page()

    @allure.title(
        'Проверить, что кнопка "Logout" разлогинивает пользователя и редиректит на Login Page.'
    )
    def test_logout_option_leads_to_login_page_and_logout_user(
        self, page: Page, overview_page
    ):
        overview_page.open_hamburger_menu()
        overview_page.check_logout_option_leads_to_login_page()

    @pytest.mark.xfail(
        reason='Баг. После резета страницы состояние кнопки "Remove" не возвращается к исходному.'
    )
    @allure.title(
        'Проверить, что кнопка "Reset App State" удаляет все продукты из корзины.'
    )
    def test_reset_option_remove_products_from_cart(self, page: Page, overview_page):
        overview_page.open_hamburger_menu()
        overview_page.click_reset_app_state_option()
        overview_page.check_cart_badge_value_not_shown()
        overview_page.check_product_data_not_shown()
        overview_page.check_inventory_page_opened()

    @allure.title("Проверить, что гамбургер-меню можно закрыть.")
    def test_close_hamburger_menu(self, page: Page, overview_page):
        overview_page.open_hamburger_menu()
        overview_page.check_close_hamburger_menu_button_shown()
        overview_page.close_hamburger_menu()
        overview_page.check_hamburger_menu_closed()


@pytest.mark.usefixtures("random_product")
class TestCart:

    @allure.title('Проверить, что присутствует иконка "Тележка".')
    def test_cart_icon_shown(self, page: Page, overview_page):
        overview_page.check_cart_icon_shown()

    @allure.title(
        'Проверить, что бейджик на иконке "Тележка" изменяет значение, если у пользователя есть продукт в корзине.'
    )
    def test_cart_badge_shown_when_product_added(self, page: Page, overview_page):
        overview_page.check_cart_badge_value_equal_("1")

    @allure.title("Проверить, что корзина успешно открывается.")
    def test_open_cart(self, page: Page, overview_page):
        overview_page.open_cart()
        overview_page.check_cart_page_opened()


@pytest.mark.usefixtures("random_product")
class TestCheckoutSingleProduct:

    @allure.title('Проверить, что присутствует заголовок "QTY".')
    def test_qty_title_shown(self, page: Page, overview_page):
        overview_page.check_qty_title_has_text_("QTY")

    @allure.title('Проверить, что присутствует заголовок "Description".')
    def test_description_title_shown(self, page: Page, overview_page):
        overview_page.check_description_title_has_text_("Description")

    @allure.title("Проверить, что отображается корректное название продукта.")
    def test_product_name_shown(self, page: Page, random_product, overview_page):
        overview_page.check_product_name_has_correct_text(random_product)

    @allure.title("Проверить, что отображается корректное описание продукта.")
    def test_product_description_shown(self, page: Page, random_product, overview_page):
        overview_page.check_product_description_has_correct_text(random_product)

    @allure.title("Проверить, что отображается корректная цена продукта.")
    def test_product_price_shown(self, page: Page, random_product, overview_page):
        overview_page.check_product_has_correct_price(random_product)

    @allure.title("Проверить, что отображается корректное количество продукта.")
    def test_product_qty_shown(self, page: Page, random_product, overview_page):
        overview_page.check_product_has_qty_("1")

    @allure.title('Проверить, что присутствует кнопка "Cancel".')
    def test_cancel_button_shown(self, page: Page, overview_page):
        overview_page.check_cancel_button_has_text_("Cancel")

    @allure.title('Проверить, что присутствует кнопка "Finish".')
    def test_finish_button_shown(self, page: Page, overview_page):
        overview_page.check_finish_button_has_text_("Finish")

    @allure.title(
        'Проверить, что кнопка "Cancel" редиректит пользователя на страницу Inventory Page.'
    )
    def test_cancel_button_leads_to_inventory_page(self, page: Page, overview_page):
        overview_page.click_cancel_button()
        overview_page.check_inventory_page_opened()

    @allure.title(
        'Проверить, что кнопка "Finish" редиректит пользователя на страницу Complete Page.'
    )
    def test_finish_button_leads_to_complete_page(self, page: Page, overview_page):
        overview_page.click_finish_button()
        overview_page.check_complete_page_opened()

    @allure.title(
        "Проверить, что при клике по названию продукта, пользователя редиректит на страницу Product Page."
    )
    def test_click_on_product_name_leads_to_product_page(
        self, page: Page, random_product, overview_page
    ):
        overview_page.click_product_name()
        overview_page.check_product_page_opened(random_product)


@pytest.mark.usefixtures("two_random_products")
class TestCheckoutMultipleProducts:

    @allure.title("Проверить, что отображаются корректные названия продуктов.")
    def test_product_names_shown(self, page: Page, two_random_products, overview_page):
        overview_page.check_product_names_has_correct_text(two_random_products)

    @allure.title("Проверить, что отображаются корректные описания продуктов.")
    def test_product_descriptions_shown(
        self, page: Page, two_random_products, overview_page
    ):
        overview_page.check_product_descriptions_has_correct_text(two_random_products)

    @allure.title("Проверить, что отображаются корректные цены продуктов.")
    def test_product_prices_shown(self, page: Page, two_random_products, overview_page):
        overview_page.check_products_has_correct_prices(two_random_products)

    @allure.title("Проверить, что отображаются корректное количество продуктов.")
    def test_products_qty_shown(self, page: Page, two_random_products, overview_page):
        overview_page.check_products_has_qty_("1")


class TestPaymentData:

    @allure.title(
        'Проверить, что присутствует колонка "Payment Information" с корректной информацией.'
    )
    def test_payment_information_shown(self, page: Page, overview_page):
        overview_page.check_payment_information_header_has_text_("Payment Information:")
        overview_page.check_card_number_has_text_("SauceCard #31337")

    @allure.title(
        'Проверить, что присутствует колонка "Shipping Information" с корректной информацией.'
    )
    def test_shipping_information_shown(self, page: Page, overview_page):
        overview_page.check_shipping_information_header_has_text_(
            "Shipping Information:"
        )
        overview_page.check_shipping_price_has_text_("Free Pony Express Delivery!")

    @allure.title(
        'Проверить, что присутствует колонка "Price Total" с корректной информацией, если добавлен один продукт.'
    )
    def test_price_total_shown(self, page: Page, random_product, overview_page):
        overview_page.check_price_total_header_has_text_("Price Total")
        overview_page.check_item_total_correct(random_product)
        overview_page.check_tax_correct(random_product)
        overview_page.check_total_correct(random_product)

    @allure.title(
        'Проверить, что присутствует колонка "Price Total" с корректной информацией, если добавлен максимум продуктов.'
    )
    def test_price_total_shown_multiple_products(
        self, page: Page, all_products, overview_page
    ):
        overview_page.check_price_total_header_has_text_("Price Total")
        overview_page.check_item_total_correct_multiple_products(all_products)
        overview_page.check_tax_correct_multiple_products(all_products)
        overview_page.check_total_correct_multiple_products(all_products)


class TestFooter:

    @allure.title("Проверить, что присутствует текст условий использования.")
    def test_terms_of_service_has_text(self, page: Page, overview_page):
        overview_page.check_terms_of_service_has_text_(
            "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        )

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Twitter" редиректит пользователя на страницу Twitter.'
    )
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, overview_page):
        overview_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Facebook" редиректит пользователя на страницу Facebook.'
    )
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, overview_page):
        overview_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "LinkedIn" редиректит пользователя на страницу LinkedIn.'
    )
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, overview_page):
        overview_page.check_linkedin_icon_leads_to_linkedin_page()
