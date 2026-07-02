import pytest
from selenium.webdriver.common.by import By

from conftest import driver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.usernameInput = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
        self.passwordInput = (By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
        self.loginButton = (By.XPATH, '//android.widget.Button')

        ex = (1, 2, 3)

    def enterUsername(self, username):
        self.driver.find_element(*self.usernameInput).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*self.passwordInput).send_keys(password)

    def clickButton(self):
        self.driver.find_element(*self.loginButton).click()