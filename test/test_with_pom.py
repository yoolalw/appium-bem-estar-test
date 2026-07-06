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

    def test_click_in_done_and_verifying_if_it_has_been_disabled(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        homepage = HomePage(self.driver)
        homepage.click_daily_challenge_btn()
        homepage.click_mark_done_challenge_btn()

        button = homepage.buttonMarkDone()

        assert button.get_attribute("clickable") == 'false'

    def test_click_in_button_next_challenge(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        homepage = HomePage(self.driver)
        status = self.wait.until(expected_conditions.visibility_of_element_located(
            (
                By.XPATH, '//android.widget.TextView[@text="Desafio 1 de 30"]'
            )
        ))
        homepage.click_next_challenge_btn()

        assert status.text == 'Desafio 2 de 30'
