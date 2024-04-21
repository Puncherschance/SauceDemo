from playwright.sync_api import Page
from env import *


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, endpoint):
        self.page.goto(BASE_PAGE_URL + endpoint)

