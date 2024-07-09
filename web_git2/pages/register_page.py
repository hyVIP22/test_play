"""
注册页面
"""
from playwright.sync_api import Page


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        # 定位元素
        self.locator_username = page.locator("#username")
        self.locator_passwd = page.get_by_label("密     码:")
        self.locator_register_btn = page.locator("#registerBtn")

    # 导航到目标url
    def navigate(self):
        self.page.goto("http://47.116.12.183/register.html")

    # 封装一些操作方法
