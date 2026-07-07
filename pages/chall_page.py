import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class ChallengesDonePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.title_displayed = (By.XPATH, '//android.widget.TextView[@text="Desafios concluídos"]')

    def verifying_title_displayed(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.title_displayed))
