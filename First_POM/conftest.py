from base.webdriver_factory import WebDriverFactory
import pytest



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def start(request):
    webdriver = WebDriverFactory(request.config.getoption("--browser"))
    driver = webdriver.get_driver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    if request.config.getoption("--browser") != None:
        if request.config.getoption("--browser").lower == "firefox":
            driver.quit()
