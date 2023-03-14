from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition


class Wait:
    def __init__(self, driver, timeout: float, poll_frequency=0.5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, poll_frequency)


    def for_element(self, locator):
        return self.wait.until(condition.presence_of_element_located(locator))

    def to_be_clickable(self, locator):
        return self.wait.until(condition.element_to_be_clickable(locator))

    def to_be_visible(self, locator):
        return self.wait.until(condition.visibility_of_element_located(locator))

    def to_be_visible_plural(self, locator):
        return self.wait.until(condition.visibility_of_all_elements_located(locator))

    def attribute_text_to_be_present(self, locator, attribute, text):
        self.wait.until(condition.text_to_be_present_in_element_attribute(locator, attribute, text))

    def wait_for_y_scroll(self, y):
        self.wait.until(lambda driver: self.driver.execute_script("return window.pageYOffset") == y)

    def for_page_ready_state(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def till_scrollable(self):
        self.wait.until(lambda driver: self.driver.execute_script(
                "return (document.body.scrollHeight > document.body.clientHeight);"))


