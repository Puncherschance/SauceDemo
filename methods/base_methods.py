import datetime
from random import randrange

import allure
from playwright.sync_api import Page, expect

from config import IMAGE_DIR
from env import *
from resources.inventory_page_resources import INVENTORY_ITEMS


class BaseMethods:

    def __init__(self, page: Page):
        self.page = page

    # ACTIONS

    def open_url(self, endpoint):
        self.page.goto(BASE_URL + endpoint)

    def click_element(self, locator):
        self.check_element_shown(locator)
        element = self.page.locator(locator)
        element.click()

    def select_dropdown_option(self, locator, data):
        self.page.select_option(locator, data)

    def enter_data(self, locator, data: str):
        self.check_element_shown(locator)
        element = self.page.locator(locator)
        element.fill(data)

    def get_list_of(self, data: str) -> list[str]:
        elements = self.page.locator(data)
        return elements.all_inner_texts()

    # VALIDATIONS

    def check_url(self, endpoint):
        try:
            url = BASE_URL + endpoint
            expect(
                self.page, f"Ожидался url: {url}. Получен url: {self.page.url}."
            ).to_have_url(url)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_outer_url(self, url):
        try:
            expect(
                self.page, f"Ожидался url: {url}. Получен url: {self.page.url}."
            ).to_have_url(url)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_shown(self, locator):
        try:
            element = self.page.locator(locator)
            expect(
                element, f"Не найден элемент по локатору: {locator}."
            ).to_be_visible()
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_dropdown_option_shown(self, locator, data: str):
        try:
            element = self.page.locator(locator)
            expect(element, f"Не была найдена опция {data}.").to_contain_text(data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_not_shown(self, locator):
        try:
            element = self.page.locator(locator)
            expect(
                element, f"Найден элемент по локатору: {locator}."
            ).not_to_be_visible()
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_has_text(self, locator, data: str):
        self.check_element_shown(locator)
        try:
            element = self.page.locator(locator)
            expect(
                element,
                f"Ожидался текст элемента: {data}. Получен текст элемента: {element.text_content()}.",
            ).to_have_text(data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_qty(self, locator, data: str):
        try:
            element = self.page.locator(locator)
            expect(
                element,
                f"Ожидалось количество элементов {data}. Получено количество элементов {element.count()}.",
            ).to_have_count(data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_placeholder_text(self, locator, data: str):
        self.check_element_shown(locator)
        try:
            element = self.page.locator(locator)
            expect(
                element,
                f"Ожидался текст плейсхолдера: {data}. "
                f'Получен текст плейсхолдера: {element.get_attribute("placeholder")}.',
            ).to_have_attribute("placeholder", data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_asc_sorting(self, data):
        try:
            for i in range(len(data) - 1):
                item_a, item_b = data[i], data[i + 1]
                assert (
                    item_a <= item_b
                ) is True, f"Некорректная сортировка значений: {item_a} и {item_b}."
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_desc_sorting(self, data):
        try:
            for i in range(len(data) - 1):
                item_a, item_b = data[i], data[i + 1]
                assert (
                    item_a >= item_b
                ) is True, f"Некорректная сортировка значений: {item_a} и {item_b}."
        except Exception as err:
            self.attach_screenshot()
            raise err

    # HELPERS

    @staticmethod
    def convert_to_float(data) -> float:
        for i in range(len(data)):
            data[i] = float(data[i][1:])
        return data

    @staticmethod
    def calculate_tax(data: str) -> str:
        tax = float(data.replace("$", "")) / 12.5
        tax_rounded = "{:.2f}".format(round(tax, 2))
        return tax_rounded

    @staticmethod
    def calculate_item_total_for_product(price: str, tax: str) -> str:
        price = price.replace("$", "")
        total = float(price) + float(tax)
        total_rounded = "{:.2f}".format(round(total, 2))
        return total_rounded

    @staticmethod
    def calculate_item_total_for_6_products(products_data: tuple) -> str:
        total_price, count = 0, 0
        for _ in range(6):
            total_price += float(products_data[count]["Price"][0].replace("$", ""))
            count += 1
        total_price_formatted = "$" + str(total_price)
        return total_price_formatted

    @staticmethod
    def random_number() -> int:
        random_number = randrange(start=0, stop=5)
        return random_number

    @staticmethod
    def random_numbers() -> tuple:
        random_number_1 = randrange(start=0, stop=5)
        while True:
            random_number_2 = randrange(start=0, stop=5)
            if random_number_2 == random_number_1:
                continue
            break
        random_product_1 = INVENTORY_ITEMS[random_number_1]
        random_product_2 = INVENTORY_ITEMS[random_number_2]
        return random_product_1, random_product_2

    def attach_screenshot(self):
        current_datetime = (
            str(datetime.datetime.now()).replace(".", " ").replace(":", "-")
        )
        allure.attach(
            self.page.screenshot(
                path=str(IMAGE_DIR) + "/" + current_datetime + ".png", full_page=True
            )
        )
