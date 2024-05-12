from pages.base_page import BasePage
from locators.overview_page_locators import *
from env import *

import allure


class OverviewPage(BasePage):

    # PRODUCTS

    @allure.step('Проверить, что отображается корректное название продукта.')
    def check_product_name_has_correct_text(self, product_data: dict[str, str]):
        name = product_data['Name'][0]
        self.check_element_has_text(locator=PRODUCT_1_NAME, data=name)

    @allure.step('Проверить, что отображаются корректные названия продуктов.')
    def check_product_names_has_correct_text(self, products_data):
        name_1 = products_data[0]['Name'][0]
        name_2 = products_data[1]['Name'][0]
        self.check_element_has_text(locator=PRODUCT_1_NAME, data=name_1)
        self.check_element_has_text(locator=PRODUCT_2_NAME, data=name_2)

    @allure.step('Проверить, что отображается корректное описание продукта.')
    def check_product_description_has_correct_text(self, product_data: dict[str, str]):
        description = product_data['Description'][0]
        self.check_element_has_text(locator=PRODUCT_1_DESC, data=description)

    @allure.step('Проверить, что отображаются корректные описания продуктов.')
    def check_product_descriptions_has_correct_text(self, products_data):
        description_1 = products_data[0]['Description'][0]
        description_2 = products_data[1]['Description'][0]
        self.check_element_has_text(locator=PRODUCT_1_DESC, data=description_1)
        self.check_element_has_text(locator=PRODUCT_2_DESC, data=description_2)

    @allure.step('Проверить, что отображается корректная цена продукта.')
    def check_product_has_correct_price(self, product_data: dict[str, str]):
        price = product_data['Price'][0]
        self.check_element_has_text(locator=PRODUCT_1_PRICE, data=price)

    @allure.step('Проверить, что отображаются корректные цены продуктов.')
    def check_products_has_correct_prices(self, products_data):
        price_1 = products_data[0]['Price'][0]
        price_2 = products_data[1]['Price'][0]
        self.check_element_has_text(locator=PRODUCT_1_PRICE, data=price_1)
        self.check_element_has_text(locator=PRODUCT_2_PRICE, data=price_2)

    @allure.step('Проверить, что отображается количество продукта {value}.')
    def check_product_has_qty_(self, value: str):
        self.check_element_has_text(locator=PRODUCT_1_QTY, data=value)

    @allure.step('Проверить, что отображается количество продукта {value} для каждого продукта.')
    def check_products_has_qty_(self, value: str):
        self.check_element_has_text(locator=PRODUCT_1_QTY, data=value)
        self.check_element_has_text(locator=PRODUCT_2_QTY, data=value)

    @allure.step('Проверить, что присутствует кнопка "Cancel".')
    def check_cancel_button_has_text_(self, text):
        self.check_element_has_text(locator=CANCEL, data=text)

    @allure.step('Кликнуть по кнопке "Cancel".')
    def click_cancel_button(self):
        self.click_element(locator=CANCEL)

    @allure.step('Проверить, что присутствует кнопка "Finish".')
    def check_finish_button_has_text_(self, text):
        self.check_element_has_text(locator=FINISH, data=text)

    @allure.step('Кликнуть по кнопке "Finish".')
    def click_finish_button(self):
        self.click_element(locator=FINISH)

    @allure.step('Проверить, что не отображается информация о продукте.')
    def check_product_data_not_shown(self):
        self.check_element_not_shown(locator=PRODUCT_1_NAME)
        self.check_element_not_shown(locator=PRODUCT_1_DESC)
        self.check_element_not_shown(locator=PRODUCT_1_PRICE)
        self.check_element_not_shown(locator=PRODUCT_1_QTY)

    # PAYMENT INFORMATION

    @allure.step('Проверить, что присутствует текст заголовка: {text}.')
    def check_payment_information_header_has_text_(self, text):
        self.check_element_has_text(locator=PAYMENT_INFO, data=text)

    @allure.step('Проверить, что присутствует номер карты пользователя: {card_number}.')
    def check_card_number_has_text_(self, card_number):
        self.check_element_has_text(locator=CARD_NUMBER, data=card_number)

    @allure.step('Проверить, что присутствует текст заголовка: {text}.')
    def check_shipping_information_header_has_text_(self, text):
        self.check_element_has_text(locator=SHIPPING_INFO, data=text)

    @allure.step('Проверить, что присутствует цена доставки: {price}.')
    def check_shipping_price_has_text_(self, price):
        self.check_element_has_text(locator=SHIPPING_PRICE, data=price)

    @allure.step('Проверить, что присутствует цена доставки: {text}.')
    def check_price_total_header_has_text_(self, text):
        self.check_element_has_text(locator=PRICE_TOTAL, data=text)

    @allure.step('Проверить, что присутствует корректный подитог стоимости заказа.')
    def check_item_total_correct(self, product_data):
        price = product_data['Price'][0]
        subtotal = 'Item total: ' + price
        self.check_element_has_text(locator=SUBTOTAL, data=subtotal)

    @allure.step('Проверить, что присутствует корректный расчет налога.')
    def check_tax_correct(self, product_data):
        price = product_data['Price'][0]
        tax = 'Tax: $' + self.calculate_tax(data=price)
        self.check_element_has_text(locator=TAX, data=tax)

    @allure.step('Проверить, что присутствует корректный расчет итога.')
    def check_total_correct(self, product_data):
        price = product_data['Price'][0]
        tax = self.calculate_tax(data=price)
        total = 'Total: $' + self.calculate_total(price=price, tax=tax)
        self.check_element_has_text(locator=TOTAL, data=total)

    # NAVIGATION

    @allure.step('Проверить, что пользователя редиректит на страницу Complete Page.')
    def check_complete_page_opened(self):
        self.check_url(endpoint=COMPLETE_ENDPOINT)
