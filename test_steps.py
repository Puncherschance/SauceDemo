from playwright.sync_api import Page, Playwright, sync_playwright, expect


def test_empty_login_and_password(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.saucedemo.com/')
    page.get_by_role('button', name='Login').click()
    expect(page.get_by_text('Epic sadface: Username is required')).to_be_visible()

def test_login_as_standart_user(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.saucedemo.com/')
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_role('button', name='Login').click()



