"""
整个项目插件,用于全局控制
"""
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def page_fixture():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page