from playwright.sync_api import Page, expect
from env import *


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, endpoint):
        self.page.goto(BASE_URL + endpoint)

    def check_url(self, endpoint):
        expect(self.page).to_have_url(BASE_URL+endpoint)

    def check_outer_url(self, url):
        self.page.wait_for_url(url)
        expect(self.page, 'Ошибка!').to_have_url(url)

    def check_element_shown(self, locator):
        element = self.page.locator(locator)
        expect(element, f'Не найден элемент по локатору {locator}.').to_be_visible()

    def check_element_not_shown(self, locator):
        element = self.page.locator(locator)
        expect(element, f'Найден элемент по локатору {locator}.').not_to_be_visible()

    def check_element_has_text(self, locator, data):
        element = self.page.locator(locator)
        expect(element, f'Ожидался текст элемента: {data}. Получен текст элемента {element.text_content()}.').to_have_text(data)

    def check_placeholder_text(self, locator, data):
        element = self.page.locator(locator)
        expect(element, f'Ожидался текст плейсхолдера: {data}. Получен текст плейсхолдера {element.get_attribute("placeholder")}.').to_have_attribute('placeholder', data)

    def click_element(self, locator):
        element = self.page.locator(locator)
        element.click()

    def enter_data(self, locator, data):
        element = self.page.locator(locator)
        element.fill(data)
