import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver


class AboutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.about_title = (By.XPATH, '//android.widget.TextView[@text="Sobre o app"]')
        self.about_text = (By.XPATH,
                           '//android.widget.TextView[@text="Este aplicativo foi criado para ajudar você a desenvolver hábitos mais saudáveis, melhorar seu bem-estar emocional e estimular o aprendizado diário por meio de pequenos desafios. Cada ação proposta foi pensada para trazer mais equilíbrio, foco e leveza para a sua rotina. Cuide de você um passo de cada vez."]')
        self.how_works_title = (By.XPATH, '//android.widget.TextView[@text="Como funciona"]')
        self.how_works_text = (By.XPATH,
                               '//android.widget.TextView[@text="O aplicativo possui 5 desafios rotativos que são disponibilizados progressivamente para você"]')

    def verifying_if_about_title_exists(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.about_title)).is_displayed()

    def verifying_if_about_text_exists(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.about_text)).is_displayed()

    def verifying_if_how_works_title_exists(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.how_works_title)).is_displayed()

    def verifying_if_how_works_text_exists(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.how_works_text)).is_displayed()
