from playwright.sync_api import sync_playwright


# with sync_playwright() as p:
#     browser = p.chromium.launch(channel='chrome', headless=False)
#     page = browser.new_page()
#     page.goto('https://www.baidu.com/')
#     print(page.title())
#     page.pause()


p = sync_playwright().start()
browser = p.chromium.launch(channel='chrome', headless=False)
page = browser.new_page()
page.goto("https://www.baidu.com/")
print(page.title())
p.stop()