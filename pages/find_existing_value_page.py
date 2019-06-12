from base.base_page import BasePage
from utilities.util import Util
import utilities.custom_logger as cl
import logging


class FindExistingValuePage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    """ Unless otherwise noted, locator_type is 'ID' """
    # LOCATORS
    _new_window_link = "New Window"  # LINK_TEXT
    _help_link = "Help"  # LINK_TEXT
    _keyword_search_tab = "ICTAB_1"
    _add_new_value_tab = "ICTAB_2"
    _supplier_id_txt = "VENDOR_AP_VW_VENDOR_ID"
    _persistence_select = "VENDOR_AP_VW_VENDOR_PERSISTENCE"
    _short_supplier_name_txt = "VENDOR_AP_VW_VENDOR_NAME_SHORT"
    _our_customer_number_txt = "VENDOR_AP_VW_AR_NUM"
    _supplier_name = "VENDOR_AP_VW_NAME1"
    _search_btn = "#ICSearch"
    _clear_btn = "#ICClear"
    _basic_search_link = "Basic Search"  # LINK_TEXT
    _save_search_criteria_link = "Save Search Criteria"  # LINK_TEXT
    _find_existing_value_link = "Find an Existing Value"  # LINK_TEXT
    _keyword_search_link = "Keyword Search"  # LINK_TEXT
    _add_new_value_link = "Add a New Value"  # LINK_TEXT

    def click_add_new_value_tab(self):
        self.element_click(self._add_new_value_tab)

    def add_a_new_value(self):
        self.driver.switch_to.frame("ptifrmtgtframe")
        self.util.sleep(1, "the active window to be recognized by the app.")
        self.click_add_new_value_tab()

    def search_for_supplier(self):
        self.driver.switch_to_frame("ptifrmtgtframe")
        self.util.sleep(1, "the active window to be recognized by the app.")

    def enter_supplier_id(self, supplier):
        self.driver.switch_to_frame("ptifrmtgtframe")
        self.util.sleep(1, "the active window to be recognized by the app.")

        self.sendkeys(supplier, self._supplier_id_txt)

    def click_search_btn(self):
        self.element_click(self._search_btn)
        self.util.sleep(2, "the Summary page to open.")
