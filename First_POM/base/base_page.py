from selenium import webdriver
from waits import Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver: webdriver.Chrome = driver
        self.wait = Wait(driver, timeout=15)
        self.actions = ActionChains(self.driver)


    def action_clear(self):
        self.actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        self.actions.send_keys(Keys.BACKSPACE).perform()

    def action_click(self, element):
        self.actions.click(element).perform()

    def page_scroll(self, x=0, y=0):
        self.driver.execute_script(f"window.scrollBy({x},{y});")
