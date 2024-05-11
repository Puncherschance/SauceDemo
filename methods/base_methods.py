from playwright.sync_api import Page, expect
from env import *
from config import *
from random import randrange
from resources.products import *

import allure


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

    def enter_data(self, locator, data):
        self.check_element_shown(locator)
        element = self.page.locator(locator)
        element.fill(data)

    def get_list_of(self, data):
        elements = self.page.locator(data)
        return elements.all_inner_texts()

    # VALIDATIONS

    def check_url(self, endpoint):
        try:
            url = BASE_URL + endpoint
            expect(self.page, f'Ожидался url: {url}. Получен url: {self.page.url}.').to_have_url(url)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_outer_url(self, url):
        try:
            expect(self.page, f'Ожидался url: {url}. Получен url: {self.page.url}.').to_have_url(url)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_shown(self, locator):
        try:
            element = self.page.locator(locator)
            expect(element, f'Не найден элемент по локатору: {locator}.').to_be_visible()
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_dropdown_option_shown(self, locator, data):
        try:
            element = self.page.locator(locator)
            expect(element, f'Не была найдена опция {data}.').to_contain_text(data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_not_shown(self, locator):
        try:
            element = self.page.locator(locator)
            expect(element, f'Найден элемент по локатору: {locator}.').not_to_be_visible()
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_has_text(self, locator, data):
        self.check_element_shown(locator)
        try:
            element = self.page.locator(locator)
            expect(element, f'Ожидался текст элемента: {data}. Получен текст элемента: {element.text_content()}.').to_have_text(data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_element_qty(self, locator, data):
        try:
            element = self.page.locator(locator)
            expect(element, f'Ожидалось количество элементов {data}. Получено количество элементов {element.count()}.').to_have_count(data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_placeholder_text(self, locator, data):
        self.check_element_shown(locator)
        try:
            element = self.page.locator(locator)
            expect(element, f'Ожидался текст плейсхолдера: {data}. Получен текст плейсхолдера: {element.get_attribute("placeholder")}.').to_have_attribute('placeholder', data)
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_asc_sorting(self, data):
        try:
            for i in range(len(data)-1):
                item_a, item_b = data[i], data[i + 1]
                assert (item_a <= item_b) is True, f'Некорректная сортировка значений: {item_a} и {item_b}.'
        except Exception as err:
            self.attach_screenshot()
            raise err

    def check_desc_sorting(self, data):
        try:
            for i in range(len(data)-1):
                item_a, item_b = data[i], data[i + 1]
                assert (item_a >= item_b) is True, f'Некорректная сортировка значений: {item_a} и {item_b}.'
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
        allure.attach(
            self.page.screenshot(
                path=str(IMAGE_DIR) + '/image.png',
                full_page=True)
        )
