import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver

@pytest.fixture(scope="class")
def driver():
    capabilities = dict(  
        platformName = "Android",
        automationName = "uiautomator2",
        deviceName = "RQGL3005S0T",
        app=r"C:\Users\WSC-Convidado\Downloads\BemEstarA2.apk"
    )
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )

    yield driver
    driver.quit()