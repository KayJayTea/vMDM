from base.base_page import BasePage
from selenium.webdriver.common.keys import Keys

import logging
import random
import time
import utilities.custom_logger as cl

""" GLOBAL VARIABLES """
PROCUREMENT_OPTIONS = ["COD", "N10TH", "N15TH", "N20TH", "N25TH", "N30TH", "N5TH", "N7DAY", "NET10", "NET15", "NET20",
                       "NET25", "NET30", "NET45", "NET60", "NET75", "NET90"]


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
    def select_payment_terms_id(self, pmnt_terms):
        self.expand_additional_procurement_options()
        self.enter_payment_terms_id(pmnt_terms)
        self.click_ok_button()

        time.sleep(2)

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        time.sleep(2)

    def select_random_payment_terms_id(self):
        number_of_accounts = 1
        random_account = random.choices(population=PROCUREMENT_OPTIONS, k=number_of_accounts)
        self.expand_additional_procurement_options()
        self.sendkeys(random_account, self._payment_terms_id_field)
        self.sendkeys(Keys.TAB, self._payment_terms_id_field)
        time.sleep(1)
        self.click_ok_button()

        time.sleep(1)

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        time.sleep(2)
