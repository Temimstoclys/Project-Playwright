import pytest
from playwright.sync_api import sync_playwright, Browser, Page

@pytest.fixture(scope="session")
def playwright_context():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()

@pytest.fixture(scope="session")
def browser(playwright_context) -> Browser: # type: ignore
    browser = playwright_context.chromium.launch()  # Headless por padrão
    yield browser
    browser.close()

@pytest.fixture()
def page(browser: Browser) -> Page: # type: ignore
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
