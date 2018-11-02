from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import utilities.custom_logger as cl
import logging


class SummaryPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.supplier_id = [""]

    # LOCATORS
    _navbar_action_button = "pthdr2ActionList"
    _action_list_sign_out = "pthdr2signout"
    _identifying_info_tab = "//a//span[contains(text(), 'dentifying Information')]"  # XPATH
    _address_tab = "//a//span[contains(text(), 'ddress')]"  # XPATH
    _contacts_tab = "//a//span[contains(text(), 'ontacts')]"  # XPATH
    _location_tab = "//span[contains(text(), 'ocation')]"  # XPATH
    _custom_tab = "//a//span[contains(text(), 'C')]"  # XPATH
    _save_btn = "#ICSave"
    _return_to_search_btn = "#ICList"
    _notify_btn = "#ICSendNotify"
    _add_btn = "#ICAdd"
    _include_history_btn = "#ICUpdateAll"
    _correct_history_btn = "#ICCorrection"
    _new_window_link = "New Window"  # LINK_TEXT
    _help_link = "Help"  # LINK_TEXT
    _personalize_page_link = "Personalize Page"  # LINK_TEXT
    _identifying_info_link = "Identifying Information"  # LINK_TEXT
    _address_link = "CleanAddressPage"  # LINK_TEXT
    _contacts_link = "ContactsPage"  # LINK_TEXT
    _location_link = "Location"  # LINK_TEXT
    _custom_link = "Custom"  # LINK_TEXT
    _master_vendor_id = "//span[@id='VENDOR_VENDOR_ID']"  # XPATH

    def get_supplier_id(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.XPATH, self._master_vendor_id)))

        master_vendor = self.get_element(self._master_vendor_id, "xpath").text
        print("Supplier ID: " + master_vendor)

    def click_actions_list_icon(self):
        self.element_click(self._navbar_action_button)

    def click_sign_out(self):
        self.element_click(self._action_list_sign_out)
        self.util.sleep(2, "the test to logout AUTOTEST3.")

    def click_new_window_link(self):
        self.element_click(self._new_window_link, "link")

    def click_location_tab(self):
        self.element_click(self._location_tab, "xpath")
        self.util.sleep(2, "the Location page to open.")

    def verify_title(self):
        return self.verify_page_title("Supplier")

    def verify_supplier_id_created(self):
        result = self.is_element_present("//span[@id='VENDOR_VENDOR_ID']", locator_type="xpath")

        return result

    def verify_supplier_short_name(self):
        result = self.is_element_present("//span[@id='VENDOR_VNDR_NAME_SHRT_USR']", locator_type="xpath")

        return result

    def sign_out_summary_page(self):
        self.driver.switch_to.default_content()
        self.click_actions_list_icon()
        self.click_sign_out()
