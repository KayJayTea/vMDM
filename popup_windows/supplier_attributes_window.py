from base.base_page import BasePage
from random import choice
import time
import utilities.custom_logger as cl
import logging


class SupplierAttributesWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _type_list = "WG_VNDR_ATTRIB_VENDOR_TYPE$0"
    _url = "WG_VNDR_ATTRIB_WG_TRL_URL$0"
    _ok_button = "#ICSave"

    def select_type(self):
        supplier_attribute_type = [
            "Lighting",
            "Tool",
            # "PVF",
            # "PLB-R",
            "WSYS",
            "Waterworks",
            "BUILD",
            "H/C",
            "Electric",
            "Irrigation",
            # "MILL",
            "Industrial",
            "Chemicals"
        ]
        self.sendkeys(str(choice(supplier_attribute_type)), self._type_list)
        self.element_click(self._ok_button)

        time.sleep(1)

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)
