import allure

from locators.complete_page_locators import *
from pages.base_page import BasePage


class CompletePage(BasePage):

    # ORDER_DISPATCHED

    @allure.step('Проверить, что присутствует изображение "Pony Express".')
    def check_pony_express_image_shown(self):
        self.check_element_shown(locator=PONY_IMAGE)

    @allure.step("Проверить, что на странице присутствует текст: {text}.")
    def check_order_dispatched_header_has_text_(self, text: str):
        self.check_element_has_text(locator=COMPLETE_HEADER, data=text)

    @allure.step("Проверить, что на странице присутствует текст: {text}.")
    def check_order_dispatched_has_text_(self, text: str):
        self.check_element_has_text(locator=COMPLETE_TEXT, data=text)

    @allure.step('Проверить, что отображается кнопка "Back Home".')
    def check_back_home_button_has_text_(self, text: str):
        self.check_element_has_text(locator=BACK_HOME, data=text)

    @allure.step('Кликнуть по кнопке "Back Home".')
    def click_back_home_button(self):
        self.click_element(locator=BACK_HOME)
