from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time
import utilities.custom_logger as cl
import logging


class PayablesOptionsWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ Unless otherwise noted, all locator types are 'ID' """
    # LOCATORS
    _payment_notification_arrow = "VNDR_LOC_WRK1_NOTIFICATION"
    _enable_email_payment_advice_chbx = "VENDOR_PAY_EMAIL_ADVICE$0"
    _email_id_field = "VENDOR_PAY_EMAILID$0"
    _pmnt_method_list = "EMAIL_PAY_MTHD_PYMNT_METHOD$0"
    _ok_btn = "#ICSave"

    def enter_payment_notification_details(self, driver, email):
        time.sleep(1)
        self.element_click(self._payment_notification_arrow)
        self.element_click(self._enable_email_payment_advice_chbx)
        time.sleep(1)
        self.sendkeys((email, Keys.TAB), self._email_id_field)
        time.sleep(1)

        pymnt_method_list = driver.find_element(By.ID, self._pmnt_method_list)
        sel = Select(pymnt_method_list)
        sel.select_by_visible_text("System Check")

        time.sleep(1)

        self.element_click(self._ok_btn)

        time.sleep(1)

        try:
            driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        time.sleep(1)
