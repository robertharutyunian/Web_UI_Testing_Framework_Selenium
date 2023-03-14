from selenium import webdriver

class WebDriverFactory:
    """This class is responsible for creating webdriver types according to additional argument values provided
    either in the terminal or in the configuration settings for running the code.
    Instances for this class are creating and the methods are called in the 'conftest.py' file for this
    specific POM."""

    def __init__(self, browser_type):
        self.browser_type = browser_type

    def get_driver(self):
        try:
            if self.browser_type.lower() == "firefox":
                driver = webdriver.Firefox()
            elif self.browser_type.lower() == "edge":
                driver = webdriver.Edge()
            elif self.browser_type.lower() == "chrome":
                driver = webdriver.Chrome()
            else:
                print(f"Browser type '{self.browser_type}' is current not supported.")
                return
        except AttributeError as err:
            if str(err) == "'NoneType' object has no attribute 'lower'":
                driver = webdriver.Chrome()
            else:
                raise
        url = "https://opensource-demo.orangehrmlive.com"
        driver.get(url)
        return driver