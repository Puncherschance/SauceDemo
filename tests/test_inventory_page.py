import allure
import pytest
from playwright.sync_api import Page

from resources.base_resources import HAMBURGER_OPTIONS
from resources.inventory_page_resources import INVENTORY_ITEMS


class TestHeader:

    @allure.title('Проверить, что отображается заголовок "Swag Labs".')
    def test_swag_labs_title_shown(self, page: Page, inventory_page):
        inventory_page.check_swag_labs_title_has_text_("Swag Labs")

    @allure.title('Проверить, что отображается заголовок "Products".')
    def test_products_title_shown(self, page: Page, inventory_page):
        inventory_page.check_page_title_has_text_("Products")


class TestHamburgerMenu:

    @allure.title("Проверить, что отображается гамбургер-меню.")
    def test_hamburger_icon_shown(self, page: Page, inventory_page):
        inventory_page.check_hamburger_icon_shown()

    @allure.title("Проверить, что отображаются все опции гамбургер-меню.")
    @pytest.mark.parametrize("option", HAMBURGER_OPTIONS)
    def test_check_hamburger_option_has_correct_text(
        self, page: Page, inventory_page, option
    ):
        inventory_page.open_hamburger_menu()
        inventory_page.check_hamburger_option_has_text(option)

    @allure.title(
        'Проверить, что кнопка "All Items" редиректит пользователя на страницу Inventory Page.'
    )
    def test_all_items_option_leads_to_inventory_page(self, page: Page, inventory_page):
        inventory_page.open_hamburger_menu()
        inventory_page.check_all_items_option_leads_to_iventory_page()

    @pytest.mark.xfail(reason="Баг. Падает ошибка 403 Forbidden при открытии страницы.")
    @allure.title(
        'Проверить, что кнопка "About" редиректит пользователя на страницу About Page.'
    )
    def test_about_option_leads_to_about_page(self, page: Page, inventory_page):
        inventory_page.open_hamburger_menu()
        inventory_page.check_about_option_leads_to_about_page()

    @allure.title(
        'Проверить, что кнопка "Logout" разлогинивает пользователя и редиректит на страницу Login Page.'
    )
    def test_logout_option_leads_to_login_page_and_logout_user(
        self, page: Page, inventory_page
    ):
        inventory_page.open_hamburger_menu()
        inventory_page.check_logout_option_leads_to_login_page()

    @pytest.mark.xfail(
        reason='Баг. После резета страницы состояние кнопки "Remove" не возвращается к исходному.'
    )
    @allure.title(
        'Проверить, что кнопка "Reset App State" удаляет все продукты из корзины.'
    )
    def test_reset_option_remove_products_from_cart(self, page: Page, inventory_page):
        inventory_page.open_hamburger_menu()
        inventory_page.add_all_products_to_cart()
        inventory_page.click_reset_app_state_option()
        inventory_page.check_cart_badge_value_not_shown()
        inventory_page.check_remove_buttons_return_to_initial_state()

    @allure.title("Проверить, что гамбургер-меню можно закрыть.")
    def test_close_hamburger_menu(self, page: Page, inventory_page):
        inventory_page.open_hamburger_menu()
        inventory_page.check_close_hamburger_menu_button_shown()
        inventory_page.close_hamburger_menu()
        inventory_page.check_hamburger_menu_closed()


class TestCart:

    @allure.title('Проверить, что отображается иконка "Тележка".')
    def test_cart_icon_shown(self, page: Page, inventory_page):
        inventory_page.check_cart_icon_shown()

    @allure.title("Проверить, что пустая корзина успешно открывается.")
    def test_open_empty_cart(self, page: Page, inventory_page):
        inventory_page.open_cart()
        inventory_page.check_cart_page_opened()

    @allure.title(
        'Проверить, что при добавлении продукта в корзину, бейджик на иконке "Тележка" изменяет значение.'
    )
    def test_cart_badge_appeared_when_add_product(self, page: Page, inventory_page):
        inventory_page.check_cart_badge_value_not_shown()
        inventory_page.add_specific_product_to_cart()
        inventory_page.check_cart_badge_value_equal_("1")
        inventory_page.remove_product_from_cart()
        inventory_page.check_cart_badge_value_not_shown()

    @allure.title(
        'Проверить, что при добавлении всех продуктов в корзину, бейджик на иконке "Тележка" изменяет значение.'
    )
    def test_cart_badge_appeared_when_add_all_products(
        self, page: Page, inventory_page
    ):
        inventory_page.check_cart_badge_value_not_shown()
        inventory_page.add_all_products_to_cart()
        inventory_page.check_cart_badge_value_equal_("6")
        inventory_page.remove_all_products_from_cart()
        inventory_page.check_cart_badge_value_not_shown()


class TestSortMenu:

    @allure.title("Проверить, что отображается меню сортировки.")
    def test_sort_menu_with_sort_button_shown(self, page: Page, inventory_page):
        inventory_page.check_sort_menu_shown()

    @allure.title("Проверить, что отображаются все опции сортировки.")
    def test_all_sorting_options_shown_when_click_sort_menu(
        self, page: Page, inventory_page
    ):
        inventory_page.click_sort_menu()
        inventory_page.check_all_sorting_options_shown()

    @allure.title(
        "Проверить, что продукты корректно сортируются по алфавиту в возрастающем порядке."
    )
    def test_alphabet_asc_sorting_correct(self, page: Page, inventory_page):
        inventory_page.sort_products_("Name (A to Z)")
        inventory_page.check_products_sorted_by_alphabet_asc()

    @allure.title(
        "Проверить, что продукты корректно сортируются по алфавиту в убывающем порядке."
    )
    def test_alphabet_desc_sorting_correct(self, page: Page, inventory_page):
        inventory_page.sort_products_("Name (Z to A)")
        inventory_page.check_products_sorted_by_alphabet_desc()

    @allure.title(
        "Проверить, что продукты корректно сортируются по цене в возрастающем порядке."
    )
    def test_price_asc_sorting_correct(self, page: Page, inventory_page):
        inventory_page.sort_products_("Price (low to high)")
        inventory_page.check_products_sorted_by_price_asc()

    @allure.title(
        "Проверить, что продукты корректно сортируются по цене в убывающем порядке."
    )
    def test_price_desc_sorting_correct(self, page: Page, inventory_page):
        inventory_page.sort_products_("Price (high to low)")
        inventory_page.check_products_sorted_by_price_desc()


class TestProducts:

    @allure.title("Проверить, что отображается корректное название продукта.")
    @pytest.mark.parametrize("product_data", INVENTORY_ITEMS)
    def test_correct_product_name_shown(self, page: Page, inventory_page, product_data):
        inventory_page.check_product_name_shown(product_data)

    @allure.title("Проверить, что отображается корректное описание продукта.")
    @pytest.mark.parametrize("product_data", INVENTORY_ITEMS)
    def test_correct_product_description_shown(
        self, page: Page, inventory_page, product_data
    ):
        inventory_page.check_product_description_shown(product_data)

    @allure.title("Проверить, что отображается корректная цена продукта.")
    @pytest.mark.parametrize("product_data", INVENTORY_ITEMS)
    def test_correct_product_price_shown(
        self, page: Page, inventory_page, product_data
    ):
        inventory_page.check_product_price_shown(product_data)

    @allure.title("Проверить, что отображается изображение продукта.")
    @pytest.mark.parametrize("product_data", INVENTORY_ITEMS)
    def test_product_image_shown(self, page: Page, inventory_page, product_data):
        inventory_page.check_product_image_shown(product_data)

    @allure.title('Проверить, что отображается кнопка "Add to cart".')
    @pytest.mark.parametrize("product_data", INVENTORY_ITEMS)
    def test_add_to_cart_button_shown(self, page: Page, inventory_page, product_data):
        inventory_page.check_add_to_cart_button_shown(product_data)

    @allure.title(
        "Проверить, что при клике по названию продукта открывается страница Product page."
    )
    @pytest.mark.parametrize("product_data", INVENTORY_ITEMS)
    def test_product_description_expanded_when_click_product_name(
        self, page: Page, inventory_page, product_data
    ):
        inventory_page.expand_product_description_via_clicking_product_name(
            product_data
        )
        inventory_page.check_product_page_opened(product_data)

    @allure.title(
        "Проверить, что при клике по изображению продукта открывается страница Product page."
    )
    @pytest.mark.parametrize("product_data", INVENTORY_ITEMS)
    def test_product_description_expanded_when_click_product_image(
        self, page: Page, inventory_page, product_data
    ):
        inventory_page.expand_product_description_via_clicking_product_image(
            product_data
        )
        inventory_page.check_product_page_opened(product_data)

    @allure.title(
        'Проверить, что отображается кнопка "Remove", если продукт в корзине.'
    )
    def test_remove_buttons_shown(self, page: Page, inventory_page):
        inventory_page.add_all_products_to_cart()
        inventory_page.check_remove_buttons_shown()

    @allure.title(
        'Проверить, что вновь отображается кнопка "Add to cart", если убрать продукт из корзины.'
    )
    def test_add_to_cart_buttons_appear(self, page: Page, inventory_page):
        inventory_page.add_all_products_to_cart()
        inventory_page.check_remove_buttons_shown()
        inventory_page.remove_all_products_from_cart()
        inventory_page.check_remove_buttons_return_to_initial_state()


class TestFooter:

    @allure.title("Проверить, что присутствует текст условий использования.")
    def test_terms_of_service_has_text(self, page: Page, inventory_page):
        inventory_page.check_terms_of_service_has_text_(
            "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        )

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Twitter" редиректит пользователя на страницу Twitter.'
    )
    def test_twitter_icon_leads_to_twitter_page(self, page: Page, inventory_page):
        inventory_page.check_twitter_icon_leads_to_twitter_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "Facebook" редиректит пользователя на страницу Facebook.'
    )
    def test_facebook_icon_leads_to_facebook_page(self, page: Page, inventory_page):
        inventory_page.check_facebook_icon_leads_to_facebook_page()

    @pytest.mark.skip("Проверка недоступна без ВПН!")
    @allure.title(
        'Проверить, иконка "LinkedIn" редиректит пользователя на страницу LinkedIn.'
    )
    def test_linkedin_icon_leads_to_linkedin_page(self, page: Page, inventory_page):
        inventory_page.check_linkedin_icon_leads_to_linkedin_page()
