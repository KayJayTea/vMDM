from base.base_page import BasePage
import time
import utilities.custom_logger as cl
import logging


class NavigatePage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _navbar_btn = "PT_NAVBAR"
    _navigator_link = "//*[@id='PTNB$PTNUI_NB_MENU']"  # XPATH
    _suppliers_link = "Suppliers"  # LINK_TEXT
    _supplier_info_link = "Supplier Information"  # LINK_TEXT
    _add_update_link = "Add/Update"  # LINK_TEXT
    _supplier_link = "Supplier"  # LINK_TEXT

    """ code to do stuff """
    def click_navbar_btn(self):
        self.element_click(self._navbar_btn)

    def click_navigator(self):
        self.element_click(self._navigator_link, "xpath")

    def click_suppliers(self):
        self.element_click(self._suppliers_link, "link")

    def click_supplier_info(self):
        self.element_click(self._supplier_info_link, "link")

    def click_add_update(self):
        self.element_click(self._add_update_link, "link")

    def click_supplier(self):
        self.element_click(self._supplier_link, "link")

    def navigate_to_supplier_info(self):
        self.click_navbar_btn()
        time.sleep(1)
        self.driver.switch_to.frame("psNavBarIFrame")
        time.sleep(1)
        self.click_navigator()
        time.sleep(1)
        self.click_suppliers()
        self.click_supplier_info()
        self.click_add_update()
        self.click_supplier()
