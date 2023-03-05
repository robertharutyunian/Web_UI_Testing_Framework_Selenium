import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("page_start")
class TestPage:


    def test_radio_buttons(self):
        driver = self.driver
        bmw_radio = driver.find_element(By.CSS_SELECTOR, "input#bmwradio")
        benz_radio = driver.find_element(By.CSS_SELECTOR, "input#benzradio")
        honda_radio = driver.find_element(By.CSS_SELECTOR, "input#hondaradio")

        assert not bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert not honda_radio.is_selected()

        bmw_radio.click()
        assert bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert not honda_radio.is_selected()

        benz_radio.click()
        assert not bmw_radio.is_selected()
        assert benz_radio.is_selected()
        assert not honda_radio.is_selected()

        honda_radio.click()
        assert not bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert honda_radio.is_selected()


    def test_checkboxes(self):
        driver = self.driver
        bmw_box = driver.find_element(By.CSS_SELECTOR, "#bmwcheck")
        benz_box = driver.find_element(By.CSS_SELECTOR, "#benzcheck")
        honda_box = driver.find_element(By.CSS_SELECTOR, "#hondacheck")

        assert not bmw_box.is_selected()
        assert not benz_box.is_selected()
        assert not honda_box.is_selected()

        bmw_box.click()
        assert bmw_box.is_selected()
        assert not benz_box.is_selected()
        assert not honda_box.is_selected()

        benz_box.click()
        assert bmw_box.is_selected()
        assert benz_box.is_selected()
        assert not honda_box.is_selected()

        honda_box.click()
        assert bmw_box.is_selected()
        assert benz_box.is_selected()
        assert honda_box.is_selected()

        honda_box.click()
        assert bmw_box.is_selected()
        assert benz_box.is_selected()
        assert not honda_box.is_selected()

        benz_box.click()
        assert bmw_box.is_selected()
        assert not benz_box.is_selected()
        assert not honda_box.is_selected()

        bmw_box.click()
        assert not bmw_box.is_selected()
        assert not benz_box.is_selected()
        assert not honda_box.is_selected()


    def test_new_window(self):
        driver = self.driver
        wait = self.wait

        driver.find_element(By.CSS_SELECTOR, "#openwindow").click()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])
        courses = wait.until(condition.visibility_of_element_located((By.CSS_SELECTOR, "#zen_all_courses_dynamic")))
        assert courses.is_displayed()
        driver.close()
        driver.switch_to.window(window_handles[0])


    def test_new_tab(self):
        driver = self.driver

        driver.find_element(By.CSS_SELECTOR, "#opentab").click()
        assert len(driver.window_handles) == 2
        driver.switch_to.window(driver.window_handles[0])


    def test_dropdown(self):
        driver = self.driver
        model_select = driver.find_element(By.CSS_SELECTOR, "#carselect")
        select = Select(model_select)

        assert select.first_selected_option.text == "BMW"
        select.select_by_value("benz")
        assert select.first_selected_option.text == "Benz"
        select.select_by_index(2)
        assert select.first_selected_option.text == "Honda"
        select.select_by_visible_text("BMW")
        assert select.first_selected_option.text == "BMW"


    def test_multiple_select(self):
        driver = self.driver
        fruit_select = driver.find_element(By.CSS_SELECTOR, "#multiple-select-example")
        select = Select(fruit_select)
        apple = driver.find_element(By.CSS_SELECTOR, "option[value='apple']")
        orange = driver.find_element(By.CSS_SELECTOR, "option[value='orange']")
        peach = driver.find_element(By.CSS_SELECTOR, "option[value='peach']")

        assert not apple.is_selected()
        assert not orange.is_selected()
        assert not peach.is_selected()

        select.select_by_value("apple")
        assert apple.is_selected()
        assert not orange.is_selected()
        assert not peach.is_selected()

        select.select_by_value("orange")
        assert apple.is_selected()
        assert orange.is_selected()
        assert not peach.is_selected()

        select.select_by_value("peach")
        assert apple.is_selected()
        assert orange.is_selected()
        assert peach.is_selected()

        select.deselect_by_value("apple")
        assert not apple.is_selected()
        assert orange.is_selected()
        assert peach.is_selected()

        select.deselect_by_value("peach")
        assert not apple.is_selected()
        assert orange.is_selected()
        assert not peach.is_selected()

        select.deselect_by_value("orange")
        assert not apple.is_selected()
        assert not orange.is_selected()
        assert not peach.is_selected()


    def test_enable_disable(self):
        driver = self.driver
        enable_button = driver.find_element(By.CSS_SELECTOR, "#enabled-button")
        disable_button = driver.find_element(By.CSS_SELECTOR, "#disabled-button")
        field = driver.find_element(By.CSS_SELECTOR, "#enabled-example-input")

        assert field.is_enabled()

        disable_button.click()
        assert not field.is_enabled()

        enable_button.click()
        assert field.is_enabled()

        field.send_keys("random_text 123%")
        disable_button.click()
        assert field.get_attribute("value") == "random_text 123%"


    def test_element_displayed(self):
        driver = self.driver
        hide_button = driver.find_element(By.CSS_SELECTOR, "#hide-textbox")
        show_button = driver.find_element(By.CSS_SELECTOR, "#show-textbox")
        hiding_field = driver.find_element(By.CSS_SELECTOR, "#displayed-text")

        hide_button.click()
        assert not hiding_field.is_displayed()

        show_button.click()
        assert hiding_field.is_displayed()

        hiding_field.send_keys("random_text 123%")
        assert hiding_field.get_attribute("value") == "random_text 123%"
        hide_button.click()
        show_button.click()
        assert hiding_field.get_attribute("value") == "random_text 123%"


    def test_alert(self):
        driver = self.driver
        name_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Enter Your Name']")
        alert_button = driver.find_element(By.CSS_SELECTOR, "#alertbtn")
        confirm_button = driver.find_element(By.CSS_SELECTOR, "#confirmbtn")
        name_1 = "Robert"
        name_2 = "Daniel"
        driver.execute_script("arguments[0].scrollIntoView();", name_field)

        name_field.send_keys(name_1)
        alert_button.click()
        name_1_alert = driver.switch_to.alert
        assert name_1_alert.text == f"Hello {name_1}, share this practice page and share your knowledge"
        name_1_alert.accept()

        name_field.send_keys(name_2)
        alert_button.click()
        name_2_alert = driver.switch_to.alert
        assert name_2_alert.text == f"Hello {name_2}, share this practice page and share your knowledge"
        name_2_alert.accept()

        name_field.send_keys(name_1)
        confirm_button.click()
        name_1_confirm = driver.switch_to.alert
        assert name_1_confirm.text == f"Hello {name_1}, Are you sure you want to confirm?"
        name_1_confirm.accept()

        name_field.send_keys(name_2)
        confirm_button.click()
        name_2_confirm = driver.switch_to.alert
        assert name_2_confirm.text == f"Hello {name_2}, Are you sure you want to confirm?"
        name_1_confirm.accept()


    def test_mouse_hover(self):
        driver = self.driver
        wait = self.wait
        action = ActionChains(driver)
        mouse_hover_button = driver.find_element(By.CSS_SELECTOR, "#mousehover")
        top_button = driver.find_element(By.XPATH, "//a[text()='Top']")
        reload_button = driver.find_element(By.XPATH, "//a[text()='Reload']")
        y_offset_after_click = 124
        input_field = driver.find_element(By.CSS_SELECTOR, "input[class = 'inputs ui-autocomplete-input']")

        driver.execute_script("arguments[0].scrollIntoView();", mouse_hover_button)
        action.move_to_element(mouse_hover_button).perform()
        assert top_button.is_displayed()
        assert reload_button.is_displayed()

        top_button.click()
        wait.until(lambda driver: driver.execute_script("return window.pageYOffset") == y_offset_after_click)
        scroll_depth_after_click = driver.execute_script("return window.pageYOffset")
        assert scroll_depth_after_click == y_offset_after_click

        input_field.send_keys("disappears after reload")
        driver.execute_script("arguments[0].scrollIntoView();", mouse_hover_button)
        action.move_to_element(mouse_hover_button).perform()
        reload_button.click()
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        # We will not use "input_filed" variable below, since the element reference is lost after the reload.
        assert driver.find_element(By.CSS_SELECTOR, "input[class = 'inputs ui-autocomplete-input']").get_attribute(
            "value") != "disappears after reload"



























    



