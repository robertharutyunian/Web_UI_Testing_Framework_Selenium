from selenium.webdriver.common.by import By
from base.base_page import BasePage



class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.username_field = self.wait.until(condition.presence_of_element_located(
        #     (By.CSS_SELECTOR, "input[name='username']")))
        self.username_field = self.wait.for_element((By.CSS_SELECTOR, "input[name='username']"))
        self.password_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        self.login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")


    def valid_login(self):
        self.username_field.send_keys("Admin")
        self.password_field.click()
        self.password_field.send_keys("admin123")
        self.login_button.click()
        self.wait.for_page_ready_state()
