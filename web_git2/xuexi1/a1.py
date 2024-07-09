from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=False)
    page = browser.new_page()
    page.goto('https://www.baidu.com/')
    print(page.title())
    page.pause()

    time.sleep(2)
