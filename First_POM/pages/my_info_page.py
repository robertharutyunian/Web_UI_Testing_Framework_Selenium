from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class PersonalDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver: webdriver.Chrome = driver


    def fill_employee_full_name(self, firstname, middlename, lastname):
        first_name_field = self.wait.to_be_clickable((By.CSS_SELECTOR, "input[name='firstName']"))
        middle_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='middleName']")
        last_name_field = self.wait.to_be_clickable((By.CSS_SELECTOR, "input[name='lastName']"))

        last_name_field.click()
        self.action_clear()
        last_name_field.send_keys(lastname)
        first_name_field.click()
        self.action_clear()
        first_name_field.send_keys(firstname)
        middle_name_field.click()
        self.action_clear()
        middle_name_field.send_keys(middlename)

    def is_first_name_correct(self, firstname):
        first_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
        return first_name_field.get_attribute("value") == firstname

    def is_middle_name_correct(self, middlename):
        middle_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='middleName']")
        return middle_name_field.get_attribute("value") == middlename

    def is_last_name_correct(self, lastname):
        last_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
        return last_name_field.get_attribute("value") == lastname


    def fill_nickname(self, nickname):
        nickname_field = self.driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[1]
        nickname_field.click()
        self.action_clear()
        self.actions.send_keys(nickname).perform()

    def is_nickname_correct(self, nickname):
        nickname_field = self.driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[1]
        return nickname_field.get_attribute("value") == nickname


    def fill_employee_id(self, employee_id):
        employee_id_field = self.driver.find_elements(By.XPATH, "//form[@class='oxd-form']/div/following-sibling::div"
                                                                "/div/div/div/div/following-sibling::div/input")[0]
        self.action_click(employee_id_field)
        self.action_clear()
        self.actions.send_keys(employee_id).perform()

    def is_employee_id_correct(self, employee_id):
        self.wait.attribute_text_to_be_present((By.XPATH, "//form[@class='oxd-form']/div/following-sibling::div"
            "/div/div/div/div/following-sibling::div/input"), "value", employee_id)
        return self.driver.find_element(By.XPATH, "//form[@class='oxd-form']/div/following-sibling::div"
                "/div/div/div/div/following-sibling::div/input").get_attribute("value") == employee_id


    def fill_other_id(self, other_id):
        other_id_field = self.driver.find_elements(By.XPATH, "//form[@class='oxd-form']/div/"
        "following-sibling::div/div/div/following-sibling::div/div/div/"
        "following-sibling::div/input")[0]
        other_id_field.click()
        self.action_clear()
        self.actions.send_keys(other_id).perform()

    def is_other_id_correct(self, other_id):
        other_id_field = self.driver.find_elements(By.XPATH, "//form[@class='oxd-form']/div/"
        "following-sibling::div/div/div/following-sibling::div/div/div/"
        "following-sibling::div/input")[0]
        return other_id_field.get_attribute("value") == other_id


    def fill_drivers_license(self, license_id):
        drivers_license_field = self.driver.find_elements(
            By.XPATH, "//form[@class='oxd-form']/div/"
        "following-sibling::div/div/following-sibling::div/div/div/div/"
        "following-sibling::div/input")[0]
        drivers_license_field.click()
        self.action_clear()
        self.actions.send_keys(license_id).perform()

    def is_drivers_license_correct(self, license_id):
        drivers_license_field = self.driver.find_elements(
            By.XPATH, "//form[@class='oxd-form']/div/"
                      "following-sibling::div/div/following-sibling::div/div/div/div/"
                      "following-sibling::div/input")[0]
        return drivers_license_field.get_attribute("value") == license_id


    def write_expiry_date(self, yyyy_mm_dd):
        expiry_date_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='yyyy-mm-dd']")
        expiry_date_field.click()
        self.action_clear()
        self.actions.send_keys(yyyy_mm_dd).perform()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").click()

    def is_expiry_date_error_message_displayed(self):
        error_message = self.wait.to_be_visible((By.CSS_SELECTOR,
          "span[class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"))
        return error_message.is_displayed()

    def pick_expiry_date(self, day: str, month: str = None, year: str = None):
        self.wait.till_scrollable()
        self.page_scroll(0, 368)
        self.wait.wait_for_y_scroll(368) # if this doesn't work, try 420
        expiry_date_field = self.wait.to_be_visible((By.CSS_SELECTOR, "input[placeholder='yyyy-mm-dd']"))
        expiry_date_field.click()
        self.wait.to_be_visible_plural((By.CSS_SELECTOR, "div[class='oxd-calendar-dates-grid'] div div"))

        if year is not None:
            year_selector = self.wait.to_be_visible((
                By.CSS_SELECTOR, "div[class='oxd-calendar-selector-year-selected']")).click()
            all_years = self.wait.to_be_visible_plural((By.CSS_SELECTOR, "li[class='oxd-calendar-dropdown--option']"))
            # in case "2023" is not in the list, we will use the commented out scripts below
            # year_2023 = self.driver.find_element(
            #             By.CSS_SELECTOR, "li[class='oxd-calendar-dropdown--option --selected']")
            for year_element in all_years:
                if year_element.text == year:
                    year_element.click()
                    break
            # if year == "2023":
            #     year_2023.click()

        if month is not None:
            month_selector = self.wait.to_be_visible((
                By.CSS_SELECTOR, "div[class='oxd-calendar-selector-month-selected']")).click()
            all_months = self.wait.to_be_visible_plural((By.CSS_SELECTOR, "ul[class='oxd-calendar-dropdown'] li"))
            for month_element in all_months:
                if month_element.text.lower() == month.lower():
                    month_element.click()
                    break
            else:
                raise ValueError("The month should be a stirng value from January to December.")

        all_days = self.driver.find_elements(
            By.CSS_SELECTOR, "div[class='oxd-calendar-dates-grid'] div div")
        for day_element in all_days:
            if day_element.text == day:
                day_element.click()
                break
        else:
            raise ValueError("The days should be the days of the month passed as an argument without a 0.")

    def is_expiry_date_correct(self, date_type_1, date_type_2):
        expiry_date_field = self.wait.to_be_visible((By.CSS_SELECTOR, "input[placeholder='yyyy-mm-dd']"))
        return expiry_date_field.get_attribute("value") == date_type_1 \
            or expiry_date_field.get_attribute("value") == date_type_2


    def fill_SSN(self, SSN_number, test_separartely=False):
        if test_separartely == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 368)
            self.wait.wait_for_y_scroll(420)
        SSN_number_field = self.wait.to_be_clickable((
            By.XPATH, "//form[@class='oxd-form']/div/following-sibling::div/div/following-sibling::div/"
                             "following-sibling::div/div/div/div/following-sibling::div/input"))
        SSN_number_field.click()
        self.action_clear()
        self.actions.send_keys(SSN_number).perform()

    def is_SSN_number_correct(self, SSN_number):
        SSN_number_field = self.wait.to_be_visible((
            By.XPATH, "//form[@class='oxd-form']/div/following-sibling::div/div/following-sibling::div/"
                      "following-sibling::div/div/div/div/following-sibling::div/input"))
        return SSN_number_field.get_attribute("value") == str(SSN_number)


    def fill_SIN(self, SIN_number, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 368)
            self.wait.wait_for_y_scroll(420)
        SIN_number_field = self.wait.to_be_clickable((
            By.XPATH, "//form[@class='oxd-form']/div/following-sibling::div/div/following-sibling::div/"
            "following-sibling::div/div/following-sibling::div/div/div/following-sibling::div/input"))
        SIN_number_field.click()
        self.action_clear()
        self.actions.send_keys(SIN_number).perform()

    def is_SIN_number_correct(self, SIN_number):
        SIN_number_field = self.wait.to_be_visible((
            By.XPATH, "//form[@class='oxd-form']/div/following-sibling::div/div/following-sibling::div/"
                      "following-sibling::div/div/following-sibling::div/div/div/following-sibling::div/input"))
        return SIN_number_field.get_attribute("value") == str(SIN_number)


    def select_nationality(self, nationality: str, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 562)
            self.wait.wait_for_y_scroll(588)
        nationality_field = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-wrapper']")[0]
        nationality_field.click()
        all_nationalities = self.driver.find_elements(By.CSS_SELECTOR, "div[role='listbox'] div span")
        for nationality_element in all_nationalities:
            if nationality_element.text.lower() == nationality.lower():
                nationality_element.click()
                break
        else:
            raise ValueError("Nationality argument must be written correctly.")

    def is_nationality_correctly_chosen(self, nationality):
        nationality_text = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text-input']")[0].text
        return nationality_text.lower() == nationality.lower()

    def is_nationality_correctly_ordered(self, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 562)
            self.wait.wait_for_y_scroll(588)
        nationality_button = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-wrapper']")[0]
        nationality_button.click()
        all_nationalities = self.driver.find_elements(By.CSS_SELECTOR, "div[role='listbox'] div span")
        nationality_texts = [nation_el.text for nation_el in all_nationalities]
        return nationality_texts == sorted(nationality_texts)


    def marital_status(self, status: str, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 562)
            self.wait.wait_for_y_scroll(588)
        self.page_scroll(562)
        marital_status_button = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-wrapper']")[1]
        marital_status_button.click()
        all_statuses = self.driver.find_elements(By.CSS_SELECTOR, "div[role='listbox'] div span")
        for status_el in all_statuses:
            if status_el.text.lower() == status.lower():
                status_el.click()
                break
        else:
            raise ValueError("Marital status must be 'single', 'married' or 'other'")

    def is_marital_status_correct(self, status):
        marital_status_text = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text-input']")[1].text
        return marital_status_text.lower() == status.lower()


    def write_date_of_birth(self, yyyy_mm_dd, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(622)
            self.wait.wait_for_y_scroll(674)
        date_of_birth_field = self.driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-mm-dd']")[1]
        date_of_birth_field.click()
        self.action_clear()
        self.actions.send_keys(yyyy_mm_dd).perform()
        self.driver.find_element(By.XPATH, "//label[text()='Male']").click()

    def date_of_birth_error_message(self):
        error_message = self.driver.find_element(By.XPATH,
        "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        return error_message.is_displayed()

    def pick_date_of_birth(self, year: str, month: str, day: str, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 622)
            self.wait.wait_for_y_scroll(674)
        date_of_birth_field = self.driver.find_elements(By.XPATH, "//div[@class ='oxd-date-input']/input")[1]
        date_of_birth_field.click()
        self.wait.to_be_visible_plural((By.CSS_SELECTOR, "div[class='oxd-calendar-wrapper']"))

        year_selector = self.wait.to_be_visible((
            By.CSS_SELECTOR, "div[class='oxd-calendar-selector-year-selected']")).click()
        all_years = self.wait.to_be_visible_plural((By.CSS_SELECTOR, "li[class='oxd-calendar-dropdown--option']"))
        year_2023 = self.driver.find_element(
            By.CSS_SELECTOR, "li[class='oxd-calendar-dropdown--option --selected']")
        for year_element in all_years:
            if year_element.text == year:
                year_element.click()
                break

        month_selector = self.wait.to_be_visible((
            By.CSS_SELECTOR, "div[class='oxd-calendar-selector-month-selected']")).click()
        all_months = self.wait.to_be_visible_plural((By.CSS_SELECTOR, "ul[class='oxd-calendar-dropdown'] li"))
        for month_element in all_months:
            if month_element.text.lower() == month.lower():
                month_element.click()
                break
        else:
            raise ValueError("The month should be a stirng value from January to December.")

        all_days = self.driver.find_elements(
            By.CSS_SELECTOR, "div[class='oxd-calendar-dates-grid'] div div")
        for day_element in all_days:
            if day_element.text == day:
                day_element.click()
                break
        else:
            raise ValueError("The days should be the days of the month passed as an argument without a 0.")

    def is_date_of_birth_correct(self, date_type_1, date_type_2):
        date_of_birth_field = self.driver.find_elements(By.XPATH, "//div[@class ='oxd-date-input']/input")[1]
        return date_of_birth_field.get_attribute("value") == date_type_1 \
            or date_of_birth_field.get_attribute("value") == date_type_2


    def select_gender(self, gender: str, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 622)
            self.wait.wait_for_y_scroll(674)
        male_radio_button = self.driver.find_element(By.XPATH, "//label[text()='Male']")
        female_radio_button = self.driver.find_element(By.XPATH, "//label[text()='Female']")

        if gender.lower() == "male":
            male_radio_button.click()
        elif gender.lower() == "female":
            female_radio_button.click()
        else:
            raise ValueError("The gender must be either 'male' or 'female'.")

    def is_male_selected(self):
        male_radio_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='1']")
        return male_radio_button.is_selected()

    def is_female_selected(self):
        female_radio_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='2']")
        return female_radio_button.is_selected()


    def fill_military_service(self, service, test_separately=False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 622)
            self.wait.wait_for_y_scroll(674)
        military_service_field = self.driver.find_element( By.XPATH, "//form[@class='oxd-form']/div/following-sibling"
            "::div/following-sibling::div/""following-sibling::div/div/div/div/div/following-sibling::div/input")
        military_service_field.click()
        self.action_clear()
        self.actions.send_keys(service).perform()
        if test_separately == True:
            self.driver.find_element(By.XPATH, "//label[text()='Male']").click()

    def is_military_service_correct(self, service):
        military_service_field = self.driver.find_element(By.XPATH, "//form[@class='oxd-form']/div/following-sibling"
        "::div/following-sibling::div/""following-sibling::div/div/div/div/div/following-sibling::div/input")
        return military_service_field.get_attribute("value").lower() == service.lower()


    def smoking_checkbox_click(self, test_separately = False):
        if test_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 622)
            self.wait.wait_for_y_scroll(674)
        smoking_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        if smoking_checkbox.is_selected():
            self.actions.click(smoking_checkbox).perform()

    def is_smoking_checkbox_selected(self):
        smoking_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        return smoking_checkbox.is_selected()


    def save_button_click(self, click_separately=False):
        if click_separately == True:
            self.wait.till_scrollable()
            self.page_scroll(0, 622)
            self.wait.wait_for_y_scroll(674)
        save_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_button.click()

    def is_success_message_displayed(self):
        success_message = self.wait.to_be_visible((By.XPATH, "//p[text()='Successfully Updated']"))
        return success_message.is_displayed()
