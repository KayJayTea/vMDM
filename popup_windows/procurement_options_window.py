from base.base_page import BasePage
from selenium.webdriver.common.keys import Keys

import time
import utilities.custom_logger as cl
import logging


class ProcurementOptionsWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _additional_proc_options_arrow = "VNDR_LOC_WRK1_PROC_OPT_PB"
    _payment_terms_id_field = "VENDOR_LOC_PYMNT_TERMS_CD"
    _ok_btn = "#ICSave"

    """ DO SOMETHING WITH ELEMENT """
    def expand_additional_procurement_options(self):
        self.element_click(self._additional_proc_options_arrow)

    def enter_payment_terms_id(self, pmnt_terms):
        self.sendkeys((pmnt_terms, Keys.TAB), self._payment_terms_id_field)

    def click_ok_button(self):
        self.element_click(self._ok_btn)

    """ THIS IS THE MODULE THAT IS CALLED BY THE TEST """
    def enter_additional_procurement_options(self, pmnt_terms):
        self.expand_additional_procurement_options()
        self.enter_payment_terms_id(pmnt_terms)
        self.click_ok_button()

        time.sleep(2)

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        time.sleep(2)
