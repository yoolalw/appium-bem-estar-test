import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage

from conftest import driver
from pages.login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestMobPom:
    driver = WebDriver
    wait = WebDriverWait

    def test_login_with_valid_auth(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("fred")
        login_page.enter_password("123")
        login_page.click_button()

        element_in_home_page = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                                  '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View')))

        assert element_in_home_page.is_displayed()
        return

    def test_login_with_invalid_auth(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("fred")
        login_page.enter_password("1234")
        login_page.click_button()

        error_message = self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//android.widget.TextView[@text="Credenciais inválidas!"]')))
        assert error_message.text == 'Credenciais inválidas!'

    def test_verifying_if_home_page_exists(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        homepage = HomePage(self.driver)
        homepage.items_displayeds_in_home_page()

    def test_click_to_see_the_daily_challenge(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        homepage = HomePage(self.driver)
        homepage.click_in_daily_challenge()
        verify_daily_challenge = self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//android.widget.TextView[@text="Beba um copo de água"]')
        ))
        verify_daily_challenge_category = self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//android.widget.TextView[@text="Social"]')
        ))

        assert verify_daily_challenge.text == 'Beba um copo de água' and verify_daily_challenge_category.text == 'Social'

