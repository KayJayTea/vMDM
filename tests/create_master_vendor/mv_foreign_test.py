from pages.login_page import LoginPage
from pages.navigator_page import NavigatePage
from pages.find_existing_value_page import FindExistingValuePage
from pages.add_new_value_page import SupplierInformationANV
from pages.summary_page import SummaryPage
from pages.identifying_information_page import IdentifyingInformationPage
from pages.address_page import AddressPage
from pages.location_page import LocationPage
from popup_windows.procurement_options_window import ProcurementOptionsWindow
from utilities.tests_status import TestStatus

import pytest
import unittest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class TestCreateForeignMV(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.nav = NavigatePage(self.driver)
        self.sup_info_fev = FindExistingValuePage(self.driver)
        self.sup_info_anv = SupplierInformationANV(self.driver)
        self.summary = SummaryPage(self.driver)
        self.id_info = IdentifyingInformationPage(self.driver)
        self.addr = AddressPage(self.driver)
        self.loc = LocationPage(self.driver)
        self.procurement = ProcurementOptionsWindow(self.driver)

    @pytest.mark.run(order=1)
    @data(("AUTOTEST3", "wrongpassword"))
    @unpack
    def test_invalid_password(self, username, password):
        self.lp.login(username, password)
        result = self.lp.verify_login_failed()
        self.ts.mark(result, "Verified Login Failed!")

    @pytest.mark.run(order=2)
    @data(("AUTOTEST3", "Psoft1234!"))
    @unpack
    def test_foreign_master_vendor_creation(self, username, password):

        self.lp.login(username, password)
        result_1 = self.lp.verify_title()
        self.ts.mark(result_1, "Title is CORRECT")

        self.nav.navigate_to_supplier_info()
        self.sup_info_fev.add_a_new_value()
        self.sup_info_anv.click_add_button()
        self.id_info.input_identifying_info("DNS")

        """ FOREIGN CORPORATE INFORMATION """
        self.id_info.click_address_tab()
        self.addr.clean_germany_address()
        self.addr.enter_email_id()
        self.addr.enter_business_phone()
        self.addr.enter_fax()

        """ FOREIGN REMIT Address """
        self.addr.click_add_new_address_btn()
        self.addr.enter_foreign_master_vendor_address("Remit", "DEU")
        self.addr.enter_email_id()
        self.addr.enter_business_phone()
        self.addr.enter_fax()

        """ FOREIGN TRILOGIE PO ADDRESS """
        self.addr.click_add_new_address_btn()
        self.addr.enter_foreign_master_vendor_address("Trilogie PO Address", "DEU")
        self.addr.enter_email_id()
        self.addr.enter_business_phone()
        self.addr.enter_fax()

        """ ADD LOCATIONS """
        self.addr.click_location_tab()
        self.loc.add_location("MAIN", "Remit to Main")

        # Add Procurement
        self.loc.click_procurement_link()
        self.procurement.enter_additional_procurement_options("COD")

        """ SAVE RECORD """
        self.loc.click_save_btn()
        self.loc.click_summary_tab()

        self.summary.get_supplier_id()

        result2 = self.summary.verify_supplier_id_created()
        self.ts.mark(result2, "Successfully Created Foreign Master Vendor.")

    @pytest.mark.run(order=3)
    def test_sign_out(self):
        self.summary.sign_out_summary_page()

        result = self.lp.verify_title_of_log_out_page()
        self.ts.mark_final("Test Create Master and Branch Vendor", result, "Successfully Signed Out of Application.")
