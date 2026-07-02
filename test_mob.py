import time

import pytest
from cffi.model import BaseType
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from conftest import driver


class TestMob:
    def test_displayed_items_in_login_page(self, driver):
        time.sleep(5)
        email = driver.find_element(By.XPATH, value='//android.widget.TextView[@text="Email"]')
        email.is_displayed()

        password = driver.find_element(By.XPATH, value='//android.widget.TextView[@text="Senha"]')
        password.is_displayed()

    def test_inserting_itens_in_login_page(self, driver):
        time.sleep(4)
        email = driver.find_element(By.XPATH,
                                    value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
        email.send_keys('fred')
        password = driver.find_element(By.XPATH,
                                       value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
        password.send_keys('123')
        submit = driver.find_element(By.XPATH, value='//android.widget.Button')
        submit.click()

    def test_verifying_itens_in_homepage(self, driver):
        wait = WebDriverWait(driver, 10)

        verDesafio = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                   '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button')))
        concluirDesafio = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                        '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]')))
        proxDesafio = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                    '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.Button')))

    def test_clicking_in_show_challenge(self, driver):
        wait = WebDriverWait(driver, 10)
        verDesafio = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                   '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button')))
        verDesafio.click()

    def test_clicking_in_mark_done(self, driver):
        wait = WebDriverWait(driver, 10)
        concluirDesafio = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                        '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.Button')))
        concluirDesafio.click()

    def test_clicking_in_new_challenge(self, driver):
        print('verificandoProxDesafio')
        wait = WebDriverWait(driver, 10)
        proxDesafio = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                    '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.Button')))
        proxDesafio.click()

        verDesafio = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                   '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button')))
        verDesafio.click()

        text = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="Envie uma mensagem positiva para alguém"]')))

    def test_redirect_to_page_to_see_the_done_challenges(self, driver):
        wait = WebDriverWait(driver, 10)
        pagConcluido = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[4]')))
        pagConcluido.click()

    def test_verifying_if_challenges_have_been_present(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="Beba um copo de água"]')))