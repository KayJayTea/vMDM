from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time


class LookUpStateWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _state_field = "STATE_TBL_STATE"
    _search_result = "SEARCH_RESULT1"
    _look_up_btn = "#ICSearch"

    def select_random_state(self):
        self.util.sleep(1, "for popup window to open")

        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.util.sleep(1, "for states to be counted")

        total_states = len(self.driver.find_elements(By.XPATH, "//a[contains(@name, 'RESULT2$')]"))
        random_state = random.randint(0, total_states)
        state = self.driver.find_element(By.NAME, "RESULT1$" + str(random_state) + "")
        self.util.sleep(1, "state to be selected")
        state.click()
        self.util.sleep(1, "for popup window to close")

        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        time.sleep(1)

    def select_state(self, state):
        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.sendkeys(state, self._state_field)
        self.element_click(self._look_up_btn)
        self.util.sleep(1, "for " + str(state) + " to be found.")
        self.element_click(self._search_result)
        self.util.sleep(1, "for popup window to close")
        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        time.sleep(1)

    def select_county(self, county):
        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.sendkeys(county, self._state_field)
        self.util.sleep(3, "for test purposes")
        self.element_click(self._look_up_btn)
        self.util.sleep(3, "for " + str(county) + " to be found.")
        self.element_click(self._search_result)
        self.util.sleep(3, "for popup window to close")
        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        time.sleep(1)
