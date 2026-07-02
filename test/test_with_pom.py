import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from conftest import driver
from pages.loginpage import LoginPage

@pytest.mark.usefixtures("driver")
class TestMobPom:
    driver: WebDriver
    def test_login_page(self):
        time.sleep(7)
        loginPage = LoginPage(self.driver)
        loginPage.enterUsername("fred")
        loginPage.enterPassword("123")
        loginPage.clickButton()
