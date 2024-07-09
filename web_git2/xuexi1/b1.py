from playwright.async_api import async_playwright
import asyncio


def fun():
    print("1111")


def fun_1():
    print("2222")


# fun()
# fun_1()


async def main():
    # print("异步函数")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.baidu.com/")
        print(await page.title())
        await browser.close()
asyncio.run(main())
