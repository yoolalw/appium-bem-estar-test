import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver


@pytest.mark.usefixtures("driver")
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 8)

        self.daily_challenge = (By.XPATH,
                                '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View')
        self.mark_done_challenge = (By.XPATH,
                                    '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.Button')
        self.next_challenge = (By.XPATH,
                               '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.Button')
        self.challenge_text = (By.XPATH, '//android.widget.TextView[@text="Desafio 1 de 30"]')
        self.done_challenges_button = (By.XPATH,
                                       '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[3]')
        self.about_button = (By.XPATH,
                             '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[3]')
        self.logout_button = (By.XPATH,
                              '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[3]')

        self.status_challenges = (By.XPATH, '//android.widget.TextView[@text="Desafio 2 de 30"]')

    def click_daily_challenge_btn(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.daily_challenge)).click()

    def click_mark_done_challenge_btn(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.mark_done_challenge)).click()

    def click_next_challenge_btn(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.next_challenge)).click()

    def click_done_challenges_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.done_challenges_button)).click()

    def click_about_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.about_button)).click()

    def click_logout_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.logout_button)).click()

    def item_displayed_in_home_page(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.daily_challenge)).is_displayed()

    def items_displayeds_in_home_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.daily_challenge)).is_displayed()
        self.wait.until(expected_conditions.visibility_of_element_located(self.mark_done_challenge)).is_displayed()
        self.wait.until(expected_conditions.visibility_of_element_located(self.next_challenge)).is_displayed()
        self.wait.until(expected_conditions.visibility_of_element_located(self.challenge_text)).is_displayed()
        self.wait.until(expected_conditions.visibility_of_element_located(self.done_challenges_button)).is_displayed()
        self.wait.until(expected_conditions.visibility_of_element_located(self.about_button)).is_displayed()
        self.wait.until(expected_conditions.visibility_of_element_located(self.logout_button)).is_displayed()

    def buttonMarkDone(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.mark_done_challenge))

    def text_before_change(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.challenge_text))

    def status_changed(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.status_challenges))
