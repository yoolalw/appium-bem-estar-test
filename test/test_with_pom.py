import time
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

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_login_with_valid_auth(self):
        self.login_page.enter_username("fred")
        self.login_page.enter_password("123")
        self.login_page.click_button()

        assert self.home_page.item_displayed_in_home_page()


    def test_login_with_invalid_auth(self):
        self.login_page.enter_username("fred")
        self.login_page.enter_password("1234")
        self.login_page.click_button()

        assert self.login_page.error_message()


    def test_verifying_if_home_page_exists(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login()

        self.home_page.items_displayeds_in_home_page()


    def test_click_to_see_the_daily_challenge(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login()

        self.home_page.click_daily_challenge_btn()
        assert self.home_page.verifying_daily_challenge() and self.home_page.verifying_daily_challenge_category()


    def test_click_in_done_and_verifying_if_it_has_been_disabled(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login()

        self.home_page.click_daily_challenge_btn()
        self.home_page.click_mark_done_challenge_btn()

        button = self.home_page.buttonMarkDone()

        assert button.get_attribute("clickable") == 'false'


    def test_click_in_button_next_challenge(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login()

        self.home_page.text_before_change()
        self.home_page.click_daily_challenge_btn()
        self.home_page.click_next_challenge_btn()
        status = self.home_page.status_changed()

        assert 'Desafio 2 de 30' in status.get_attribute("text")

        # parte q supostamente iria ver a parte de verificação de desafio modificado,
        # mas como ela nao foi feita de forma correta, nao vai ter.


    #    self.home_page.click_daily_challenge_btn()
    #    verify_daily_challenge = self.wait.until(expected_conditions.visibility_of_element_located(
    #        (By.XPATH, '//android.widget.TextView[@text="Envie uma mensagem positiva para alguém"]')
    #    ))
    #    verify_daily_challenge_category = self.wait.until(expected_conditions.visibility_of_element_located(
    #        (By.XPATH, '//android.widget.TextView[@text="Social"]')
    #    ))
    #
    #   assert verify_daily_challenge.text == 'Envie uma mensagem positiva para alguém' and verify_daily_challenge_category.text == 'Social'

    def test_click_to_see_every_challenges_marked_done(self):
        self.login_page.login()

        self.home_page.click_daily_challenge_btn()
        self.home_page.click_mark_done_challenge_btn()

        self.home_page.click_done_challenges_page()

        challpage = ChallengesDonePage(self.driver)
        title = challpage.verifying_title_displayed()
        assert "Desafios concluídos" in title.get_attribute(
            'text') and challpage.verifying_if_the_challenge_has_been_added()


    def test_click_to_see_about_the_app(self):
        self.login_page.login()

        self.home_page.click_about_button()
        aboutpage = AboutPage(self.driver)

        assert aboutpage.verifying_if_about_title_exists(), "Not founded!"
        assert aboutpage.verifying_if_about_text_exists(), "Not founded!"
        assert aboutpage.verifying_if_how_works_title_exists(), "Not founded!"
        assert aboutpage.verifying_if_how_works_text_exists(), "Not founded!"


    def test_click_in_logout(self):
        self.login_page.login()

        self.home_page.click_logout_button()
        assert self.login_page.in_home_page()
