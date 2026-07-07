from asyncio import wait

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver

@pytest.mark.usefixtures("driver")
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)
        self.username_input = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
        self.password_input = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
        self.login_button = (By.XPATH, '//android.widget.Button')
        self.logout_button = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[3]')
        self.title_login_page = (By.XPATH, '//android.widget.TextView[@text="Bem vindo de volta"]')

    def enter_username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.login_button)).click()

    def logout_returns(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.logout_button)).click()

    def in_home_page(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.title_login_page)).is_displayed()

    def login(self):
        self.enter_username("fred")
        self.enter_password("123")
        self.click_button()
