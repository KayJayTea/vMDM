from base.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.util import Util

import utilities.custom_logger as cl
import logging
import time


class LocationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.util = Util()

    # LOCATORS
    _navbar_actions_list = "pthdr2ActionList"
    _actions_list_sign_out = "pthdr2signout"
    _summary_tab = "//a//span[contains(text(), 'ummary')]"  # XPATH
    _identifying_info_tab = "//a//span[contains(text(), 'dentifying Information')]"  # XPATH
    _address_tab = "//a//span[contains(text(), 'ddress')]"  # XPATH
    _contacts_tab = "//a//span[contains(text(), 'ontacts')]"  # XPATH
    _custom_tab = "//a//span[contains(text(), 'C')]"  # XPATH
    _location_field = "VNDR_LOC_SCROL_VNDR_LOC$0"
    _description_field = "VNDR_LOC_SCROL_DESCR$0"
    _sam_type = "VNDR_LOC_SCROL_CCR_ADDR_TYPE$0"
    _add_location_btn = "$ICField5$new$0$$0"
    _payables_link = "Payables"  # LINK_TEXT
    _procurement_link = "Procurement"  # LINK_TEXT
    _sales_use_tax_link = "Sales/Use Tax"  # LINK_TEXT
    _global_1099_withholding_link = "Global/1099 Withholding"  # LINK_TEXT
    _fei_trilogie_xref_link = "FEI Trilogie Xref"  # LINK_TEXT
    _save_button = "#ICSave"
    # SAVE WARNING
    _yes_button = "ptpopupmsgbtn1"
    _no_button = "ptpopupmsgbtn2"

    """ GET ELEMENT """
    def get_sam_type(self):
        return self.driver.find_element(By.ID, self._sam_type)

    """ DO SOMETHING WITH ELEMENTS """
    def click_summary_tab(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.XPATH, self._summary_tab)))
        self.element_click(self._summary_tab, "xpath")
        time.sleep(1)

    def enter_location(self, location):
        self.sendkeys(location, self._location_field)

    def enter_description(self, description):
        self.sendkeys(description, self._description_field)

    def select_sam_type(self):
        sel = Select(self.get_sam_type())
        sel.select_by_visible_text("Remit")

    def click_add_location_btn(self):
        self.element_click(self._add_location_btn)
        time.sleep(1)

    def click_payables_link(self):
        self.element_click(self._payables_link, "link")
        self.driver.switch_to.default_content()
        time.sleep(1)
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

    def click_procurement_link(self):
        self.element_click(self._procurement_link, "link")
        self.driver.switch_to.default_content()
        time.sleep(1)
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

    def click_fei_trilogie_xref_link(self):
        self.element_click(self._fei_trilogie_xref_link, "link")
        self.driver.switch_to.default_content()
        time.sleep(2)
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

    def click_save_btn(self):
        self.element_click(self._save_button)

        time.sleep(5)

        self.driver.switch_to.default_content()
        warning_msg = self.is_element_present("//div[contains(@id, 'ptModTable_')]", "xpath")

        if warning_msg:
            print("Warning Message Displayed!")
            ok_btn = self.driver.find_element(By.ID, "#ICOK")
            ok_btn.click()

            try:
                iframe = self.driver.find_element(By.ID, "ptifrmtgtframe")
                self.driver.switch_to.frame(iframe)
            except Exception as e:
                print(e)
        else:
            print("No Warning Message!")
            self.util.sleep(3, "the record to save.")
            self.driver.switch_to.frame("ptifrmtgtframe")

    def click_actions_list_icon(self):
        self.element_click(self._navbar_actions_list)

    def click_sign_out(self):
        self.element_click(self._actions_list_sign_out)
        self.util.sleep(2, "the test to logout AUTOTEST3.")

    """ SAVE WARNING Elements """
    def click_no_button(self):
        self.driver.switch_to.default_content()
        self.element_click(self._no_button)

    """ THESE MODULES ARE CALLED BY THE TEST """
    def add_location(self, location, description):
        self.enter_location(location)
        self.enter_description(description)
        self.select_sam_type()

        time.sleep(1)

    def sign_out_location_page(self):
        self.driver.switch_to.default_content()
        self.click_actions_list_icon()
        self.click_sign_out()
        self.click_no_button()

    def verify_supplier_id(self):
        result = self.is_element_present("//span[@id='VENDOR_VENDOR_ID']", locator_type="path")

        return result
