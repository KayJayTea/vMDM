from base.base_page import BasePage
from faker import Faker
from random import randint
from selenium.webdriver.common.by import By
from utilities.util import Util

from popup_windows.supplier_attributes_window import SupplierAttributesWindow

import utilities.custom_logger as cl
import logging


class IdentifyingInformationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # LOCATORS
    _new_window_link = "New Window"  # LINK_TEXT
    _help_link = "Help"  # LINK_TEXT
    _personalize_page = "Personalize Page"  # LINK_TEXT
    _summary_tab = "//span[contains(text(), 'ummary')]"  # XPATH
    _address_tab = "//span[contains(text(), 'ddress')]"  # XPATH
    _contacts_tab = "//span[contains(text(), 'ontacts')]"  # XPATH
    _location_tab = "//span[contains(text(), 'ocation')]"  # XPATH
    _custom_tab = "//span[contains(text(), 'C')]"  # XPATH
    _supplier_name_txt = "VENDOR_NAME1"
    _supplier_short_name_txt = "VENDOR_VNDR_NAME_SHRT_USR"
    _fei_trl_attributes_link = "FEI TRL Attributes"  # LINK_TEXT
    _additional_id_numbers_arrow = "VNDR_MAINT_WRK_VNDR_ID_PB"
    _customer_id = "VENDOR_CUST_ID"
    _id_num_type = "STD_ID_NUM_QUAL$0"
    _id_number = "STD_ID_NUM$0"
    _add_id_number_btn = "BUS_UNIT_IDS_AP$new$0$$0"

    def enter_supplier_name(self):
        fake_data = Faker()
        fake_company = fake_data.company()
        self.sendkeys("TEST_AK_" + fake_company, self._supplier_name_txt)

    def enter_supplier_short_name(self):
        random_num = randint(999, 9999)
        self.sendkeys("AKTST_" + (str(random_num)), self._supplier_short_name_txt)

    def click_fei_trl_attr_link(self):
        self.element_click(self._fei_trl_attributes_link, locator_type="link")
        self.util.sleep(1, "the active window to be recognized by the app.")
        self.driver.switch_to.default_content()
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

    def expand_additional_id_numbers(self):
        self.element_click(self._additional_id_numbers_arrow)

    def enter_id_type(self, id_type):
        self.sendkeys(id_type, self._id_num_type)

    def enter_id_number(self):
        self.util.sleep(2, "the ID Type to be recognized by the app.")
        random_num = randint(100000000, 999999999)
        self.sendkeys(random_num, self._id_number)

    def click_add_id_number_btn(self):
        self.element_click(self._add_id_number_btn)

    def click_address_tab(self):
        self.element_click(self._address_tab, "xpath")
        self.util.sleep(2, "the Address page to open.")

    """ THE MODULE THAT GETS CALLED BY THE TEST """
    def input_identifying_info(self, id_type):
        self.enter_supplier_name()
        self.enter_supplier_short_name()

        self.util.sleep(1, "the Supplier's Short Name to be recognized by the app.")

        """ SELECT FEI Trl Attribute """
        self.click_fei_trl_attr_link()

        supplier_attr = SupplierAttributesWindow(self.driver)
        supplier_attr.select_type()

        # Expand Additional ID Numbers section
        self.expand_additional_id_numbers()
        self.enter_id_type(id_type)
        self.element_click(self._id_number)
        self.enter_id_number()
