from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.relative_locator import locate_with
import time


class OpenWeb:
    """This class is created for automating 3 types of browsers: Chrome, Firefox and Microsoft Edge, using their
    specific web drivers. The class has a few basic methods for homework purposes."""

    def __init__(self, browser_name):
        self.browser_name = browser_name
        if browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.wait = WebDriverWait(self.driver, timeout=15)
        elif browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox()
            self.wait = WebDriverWait(self.driver, timeout=15)
        elif browser_name.lower() == "edge":
            self.driver = webdriver.Edge()
            self.wait = WebDriverWait(self.driver, timeout=15)
        else:
            print(f"'{browser_name}' is not supported. The argument should be either 'Chrome' or 'Firefox' or 'Edge'")

    def screenshot(self):
        self.driver.get("https://www.demoblaze.com/")
        self.wait.until(condition.visibility_of_element_located((By.CSS_SELECTOR, "div.col-lg-9")))
        self.driver.get_screenshot_as_file(f"{self.browser_name.lower()}_screenshot.png")

    def locate_nav_menu_elements(self, element_name):
        self.driver.get("https://www.demoblaze.com/")
        self.wait.until(condition.presence_of_element_located((By.CSS_SELECTOR, "ul.navbar-nav.ml-auto")))
        try:
            if element_name.lower() == "home":
                self.home_button = self.driver.find_element(By.XPATH, "//*[@class = 'nav-link'][@href = 'index.html']")
            elif element_name.lower() == "contact":
                self.contact_button = self.driver.find_element(By.XPATH, "//*[@data-target = '#exampleModal']")
            elif element_name.lower() == "about us":
                self.about_us_button = self.driver.find_element(By.XPATH, "// *[@data-target = '#videoModal']")
            elif element_name.lower() == "cart":
                self.cart_button = self.driver.find_element(By.XPATH, "//*[@id = 'cartur']")
            elif element_name.lower() == "log in" or element_name.lower() == "login":
                self.login_button = self.driver.find_element(By.XPATH, "//*[@id = 'login2']")
            elif element_name.lower() == "sign up":
                self.sign_up_button = self.driver.find_element(By.XPATH, "(//*[text()= 'Sign up'])[3]")
            else:
                raise NoSuchElementException
        except NoSuchElementException:
            print("No Such Element")
            return "No Such Element"
        print("Element is located")

    def locate_category_elements(self, element_name):
        self.driver.get("https://www.demoblaze.com/")
        self.wait.until(condition.presence_of_element_located((By.CSS_SELECTOR, "div.list-group")))
        try:
            if element_name.lower() == "phones":
                self.phone_button = self.driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(2)")
                print("Element is located")
            elif element_name.lower() == "laptops":
                self.laptop_button = self.driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(3)")
                print("Element is located")
            elif element_name.lower() == "monitors":
                self.monitors_button = self.driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(4)")
                print("Element is located")
            else:
                raise NoSuchElementException
        except NoSuchElementException:
            print("No Such Element")

    def highest_price(self):
        self.driver.get("https://demoblaze.com")
        self.wait = WebDriverWait(self.driver, timeout=15)
        self.wait.until(condition.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "div[class='col-lg-4 col-md-6 mb-4']")))
        product_quantity = self.driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4")
        prices = []
        n = 1
        for price in range(len(product_quantity)):
            prices.append(self.driver.find_element(By.CSS_SELECTOR, f"div#tbodyid div:nth-of-type({n}) h5").text)
            n += 1
        time.sleep(5)
        max_price = max(prices)
        max_price_product = self.driver.find_element(
            By.XPATH, f"//div[@class = 'card-block']/h5[text()='{max_price}']")
        product_name = self.driver.find_element(locate_with(By.TAG_NAME, "a").above(max_price_product)).text
        print(f"The most expensive product on this page is {product_name}, which costs {max_price}.")



def test_category(button):
    """The reason that a function was written instead of a class, is that there is nor need of creating any object
    in this case for verifying the category section."""

    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")
    wait = WebDriverWait(driver, timeout=15)
    wait.until(condition.all_of(condition.element_to_be_clickable((By.CSS_SELECTOR, "a#itemc")),
                                condition.visibility_of_element_located(
                                    (By.CSS_SELECTOR, "div#tbodyid div:nth-of-type(9)"))))
    if button.lower() == "phones":
        driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(2)").click()
        time.sleep(1)  # էս մի դեպքում սլիփ եմ օգտագործել, սփեցիֆիկ դեպք է
        actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        expected_amount = 7
        assert actual_amount == expected_amount
    elif button.lower() == "laptops":
        driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(3)").click()
        wait.until(condition.visibility_of_element_located((By.XPATH, "//a[text()='MacBook Pro']")))
        first_page_actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        first_page_expected_amount = 6
        driver.find_element(By.CSS_SELECTOR, "button#next2").click()
        wait.until(condition.visibility_of_element_located((By.XPATH, "//a[text()='ASUS Full HD']")))
        second_page_actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        second_page_expected_amount = 6
        assert first_page_actual_amount == first_page_expected_amount


        assert second_page_actual_amount == second_page_expected_amount
    elif button.lower() == "monitors":
        driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(4)").click()
        wait.until(condition.visibility_of_element_located((By.XPATH, "//a[text()='Apple monitor 24']")))
        actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        expected_amount = 2
        assert actual_amount == expected_amount
    else:
        raise NoSuchElementException("There are only 3 buttons: 'Phones', 'Laptops' and 'Monitors'")

