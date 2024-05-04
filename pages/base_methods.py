from playwright.sync_api import Page, expect
from env import *


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

    def select_option(self, locator, option):
        self.page.select_option(locator, option)

    def enter_data(self, locator, data):
        self.check_element_shown(locator)
        element = self.page.locator(locator)
        element.fill(data)

    def get_list_of(self, data):
        elements = self.page.locator(data)
        return elements.all_inner_texts()

    # VALIDATIONS

    def check_url(self, endpoint):
        expect(self.page, f'Ожидался url: {BASE_URL+endpoint}. Получен url: {self.page.url}.').to_have_url(BASE_URL+endpoint)

    def check_outer_url(self, url):
        self.page.wait_for_url(url)
        expect(self.page, f'Ожидался url: {url}. Получен url: {self.page.url}.').to_have_url(url)

    def check_element_shown(self, locator):
        element = self.page.locator(locator)
        expect(element, f'Не найден элемент по локатору: {locator}.').to_be_visible()

    def check_element_not_shown(self, locator):
        element = self.page.locator(locator)
        expect(element, f'Найден элемент по локатору: {locator}.').not_to_be_visible()

    def check_element_has_text(self, locator, data):
        self.check_element_shown(locator)
        element = self.page.locator(locator)
        expect(element, f'Ожидался текст элемента: {data}. Получен текст элемента: {element.text_content()}.').to_have_text(data)

    def check_placeholder_text(self, locator, data):
        self.check_element_shown(locator)
        element = self.page.locator(locator)
        expect(element, f'Ожидался текст плейсхолдера: {data}. Получен текст плейсхолдера: {element.get_attribute("placeholder")}.').to_have_attribute('placeholder', data)

    @staticmethod
    def check_asc_sorting(data):
        for i in range(len(data)-1):
            item_a, item_b = data[i], data[i + 1]
            assert (item_a <= item_b) is True, f'Некорректная сортировка значений: {item_a} и {item_b}.'

    @staticmethod
    def check_desc_sorting(data):
        for i in range(len(data)-1):
            item_a, item_b = data[i], data[i + 1]
            assert (item_a >= item_b) is True, f'Некорректная сортировка значений: {item_a} и {item_b}.'

    # FORMATTING

    @staticmethod
    def convert_to_float(data):
        for i in range(len(data)):
            data[i] = float(data[i][1:])
        return data
