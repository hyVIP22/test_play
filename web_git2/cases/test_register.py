from pages.register_page import RegisterPage
import pytest
from playwright.sync_api import sync_playwright, Page, expect
from utils.fun import rand_str, rand_str1
import re


class TestRegister:

    @pytest.fixture(scope="function", autouse=True)
    def for_each(self, page_fixture: Page):
        """for_each 里边写每个用例的前置条件"""
        # self.page = page
        self.register = RegisterPage(page_fixture)
        self.register.navigate()
        yield
        print("-----")

    def test_register_01(self):
        # with allure.step("注册")；
        self.register.locator_username.fill(rand_str())
        self.register.locator_passwd.fill("123456")
        self.register.locator_register_btn.click()
        # 断言
        # self.register.page.pause()
        expect(self.register.page).to_have_title("首页")
        expect(self.register.page).to_have_url("http://47.116.12.183/index.html")
        expect(self.register.page).not_to_have_url(re.compile(r".*login.html"))

    def test_register_02(self):
        # with allure.step("注册")；

        # register = RegisterPage(page_fixture)
        self.register.locator_register_btn.click()

    def test_register_03(self):
        # with allure.step("注册")；

        # register = RegisterPage(page_fixture)
        self.register.locator_username.fill("@1234")
        expect(self.register.page).t

