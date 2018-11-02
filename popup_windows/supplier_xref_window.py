from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import random
import time
import utilities.custom_logger as cl
import logging

""" GLOBAL VARIABLES """
VENDOR_ACCOUNTS = ["HOUSTONWW", "LAHVAC", "OHIOHVAC", "PLYMOUTH", "SACRAMENTO", "SANTAROSAWW"]


class SupplierXrefWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _trl_vendor_acct_field = "WG_PS_TRL_VXREF_WG_TRL_VACCT$0"
    _ok_button = "#ICSave"
    _additional_po_address_link = "Additional PO CleanAddressPage"  # LINK_TEXT
    _email_link = "Email"  # LINK_TEXT
    _authorized_representative_link = "Authorized Representative"  # LINK_TEXT

    def click_supp_xref_ok_btn(self):
        self.element_click(self._ok_button)

        time.sleep(1)

        self.driver.switch_to.default_content()

        time.sleep(1)

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        time.sleep(1)

    def select_random_account(self):
        number_of_accounts = 1
        random_account = random.choices(population=VENDOR_ACCOUNTS, k=number_of_accounts)
        self.sendkeys(random_account, self._trl_vendor_acct_field)
        self.sendkeys(Keys.TAB, self._trl_vendor_acct_field)
        time.sleep(1)
        self.click_supp_xref_ok_btn()

    def select_one_account(self, acct_1):
        self.sendkeys(acct_1, self._trl_vendor_acct_field)
        self.sendkeys(Keys.TAB, self._trl_vendor_acct_field)
        time.sleep(1)
        self.click_supp_xref_ok_btn()

        time.sleep(1)

    def select_two_accounts(self, acct_1, acct_2):
        vendor_accounts = [
            acct_1,
            acct_2,
        ]

        for i in range(len(vendor_accounts)):
            trl_vendor_account = self.driver.find_element(
                By.ID, "WG_PS_TRL_VXREF_WG_TRL_VACCT$" + str(i) + "")
            trl_vendor_account.send_keys(vendor_accounts[i])
            if i <= len(vendor_accounts):
                add_vendor_btn = self.driver.find_element(
                    By.ID, "WG_PS_TRL_VXREF$new$" + str(i) + "$$0")
                add_vendor_btn.click()
            else:
                break

            time.sleep(2)

        self.click_supp_xref_ok_btn()

        time.sleep(1)

    def select_three_accounts(self, acct_1, acct_2, acct_3):
        vendor_accounts = [
            acct_1,
            acct_2,
            acct_3
        ]

        for i in range(len(vendor_accounts)):
            trl_vendor_account = self.driver.find_element(
                By.ID, "WG_PS_TRL_VXREF_WG_TRL_VACCT$" + str(i) + "")
            trl_vendor_account.send_keys(vendor_accounts[i])
            if i <= len(vendor_accounts):
                add_vendor_btn = self.driver.find_element(
                    By.ID, "WG_PS_TRL_VXREF$new$" + str(i) + "$$0")
                add_vendor_btn.click()
            else:
                break

            time.sleep(2)

        self.click_supp_xref_ok_btn()

        time.sleep(1)

    def select_four_accounts(self, acct_1, acct_2, acct_3, acct_4):
        vendor_accounts = [
            acct_1,
            acct_2,
            acct_3,
            acct_4,
        ]

        for i in range(len(vendor_accounts)):
            trl_vendor_account = self.driver.find_element(
                By.ID, "WG_PS_TRL_VXREF_WG_TRL_VACCT$" + str(i) + "")
            trl_vendor_account.send_keys(vendor_accounts[i])
            if i <= len(vendor_accounts):
                add_vendor_btn = self.driver.find_element(
                    By.ID, "WG_PS_TRL_VXREF$new$" + str(i) + "$$0")
                add_vendor_btn.click()
            else:
                break

            time.sleep(2)

        self.click_supp_xref_ok_btn()

        time.sleep(1)

    def select_five_accounts(self, acct_1, acct_2, acct_3, acct_4, acct_5):
        vendor_accounts = [
            acct_1,
            acct_2,
            acct_3,
            acct_4,
            acct_5
        ]

        for i in range(len(vendor_accounts)):
            trl_vendor_account = self.driver.find_element(
                By.ID, "WG_PS_TRL_VXREF_WG_TRL_VACCT$" + str(i) + "")
            trl_vendor_account.send_keys(vendor_accounts[i])
            if i <= len(vendor_accounts):
                add_vendor_btn = self.driver.find_element(
                    By.ID, "WG_PS_TRL_VXREF$new$" + str(i) + "$$0")
                add_vendor_btn.click()
            else:
                break

            time.sleep(2)

        self.click_supp_xref_ok_btn()

        time.sleep(1)

    def select_all_accounts(self):
        time.sleep(1)
        for i in range(len(VENDOR_ACCOUNTS)):
            trl_vendor_account = self.driver.find_element(
                By.ID, "WG_PS_TRL_VXREF_WG_TRL_VACCT$" + str(i) + "")
            trl_vendor_account.send_keys(VENDOR_ACCOUNTS[i])
            if i <= len(VENDOR_ACCOUNTS):
                add_vendor_btn = self.driver.find_element(
                    By.ID, "WG_PS_TRL_VXREF$new$" + str(i) + "$$0")
                add_vendor_btn.click()
            else:
                break

            time.sleep(1)

        self.click_supp_xref_ok_btn()

        time.sleep(1)

    def verify_trl_vendor_id(self):
        result = self.is_element_present("WG_PS_TRL_VXREF_WG_TRL_VNDR$0")

        return result
