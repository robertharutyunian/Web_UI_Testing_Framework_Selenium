from selenium.webdriver.common.by import By
from base.base_page import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.my_info_button = self.wait.until(condtion.presence_of_element_located(
        #     (By.XPATH, "//span[text()='My Info']")))
        self.my_info_button = self.wait.for_element((By.XPATH, "//span[text()='My Info']"))

    def enter_my_info(self):
        self.my_info_button.click()
        self.wait.for_page_ready_state()
