import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def page_start(request):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://courses.letskodeit.com/practice")
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    request.cls.driver = driver
    request.cls.wait = wait