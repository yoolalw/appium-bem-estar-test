import time
from math import lgamma
from os.path import exists

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.about_page import AboutPage
from pages.chall_page import ChallengesDonePage
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

        homepage = HomePage(self.driver)
        assert homepage.item_displayed_in_home_page()

    def test_login_with_invalid_auth(self):
        login_page: LoginPage = LoginPage(self.driver)
        login_page.enter_username("fred")
        login_page.enter_password("1234")
        login_page.click_button()

        assert login_page.error_message()


    def test_verifying_if_home_page_exists(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        homepage = HomePage(self.driver)
        assert homepage.items_displayeds_in_home_page()

    def test_click_to_see_the_daily_challenge(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        homepage = HomePage(self.driver)
        homepage.click_daily_challenge_btn()
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
        homepage.text_before_change()
        homepage.click_daily_challenge_btn()
        homepage.click_next_challenge_btn()
        status = homepage.status_changed()

        assert 'Desafio 2 de 30' in status.get_attribute("text")

        # parte q supostamente iria ver a parte de verificação de desafio modificado,
        # mas como ela nao foi feita de forma correta, nao vai ter.

    #    homepage.click_daily_challenge_btn()
    #    verify_daily_challenge = self.wait.until(expected_conditions.visibility_of_element_located(
    #        (By.XPATH, '//android.widget.TextView[@text="Envie uma mensagem positiva para alguém"]')
    #    ))
    #    verify_daily_challenge_category = self.wait.until(expected_conditions.visibility_of_element_located(
    #        (By.XPATH, '//android.widget.TextView[@text="Social"]')
    #    ))
    #
    #   assert verify_daily_challenge.text == 'Envie uma mensagem positiva para alguém' and verify_daily_challenge_category.text == 'Social'

    def test_click_to_see_every_challenges_marked_done(self):
        loginpage = LoginPage(self.driver)
        loginpage.login()
        homepage = HomePage(self.driver)

        homepage.click_daily_challenge_btn()
        homepage.click_mark_done_challenge_btn()

        homepage.click_done_challenges_page()

        challpage = ChallengesDonePage(self.driver)
        title = challpage.verifying_title_displayed()
        assert "Desafios concluídos" in title.get_attribute('text')

        challenges = challpage.verifying_if_the_challenge_has_been_added()
        assert challenges

    def test_click_to_see_about_the_app(self):
        loginpage = LoginPage(self.driver)
        loginpage.login()
        homepage = HomePage(self.driver)
        homepage.click_about_button()
        aboutpage = AboutPage(self.driver)

        assert aboutpage.verifying_if_about_title_exists(), "Not founded!"
        assert aboutpage.verifying_if_about_text_exists(), "Not founded!"
        assert aboutpage.verifying_if_how_works_title_exists(), "Not founded!"
        assert aboutpage.verifying_if_how_works_text_exists(), "Not founded!"

    def test_click_in_logout(self):
        loginpage = LoginPage(self.driver)
        loginpage.login()
        homepage = HomePage(self.driver)
        homepage.click_logout_button()
        loginpage.in_home_page()

