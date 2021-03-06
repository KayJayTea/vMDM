from pages.login_page import LoginPage
from pages.navigator_page import NavigatePage
from pages.find_existing_value_page import FindExistingValuePage
from pages.add_new_value_page import SupplierInformationANV
from pages.summary_page import SummaryPage
from pages.identifying_information_page import IdentifyingInformationPage
from pages.address_page import AddressPage
from pages.location_page import LocationPage
from popup_windows.procurement_options_window import ProcurementOptionsWindow
from popup_windows.supplier_xref_window import SupplierXrefWindow
from utilities.tests_status import TestStatus


import pytest
import unittest


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestCreateDomesticBV(unittest.TestCase):

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
        self.sup_xref = SupplierXrefWindow(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_password(self):
        self.lp.login("AUTOTEST3", "wrongpassword")
        result = self.lp.verify_login_failed()
        self.ts.mark(result, "Verified Login Failed!")

    @pytest.mark.run(order=2)
    def test_domestic_master_vendor_creation(self):
        # Login into PeopleSoft with CREATOR credentials
        self.lp.login("AUTOTEST3", "Psoft1234$")
        result_1 = self.lp.verify_title()
        self.ts.mark(result_1, "Title is correct")

        self.nav.navigate_to_supplier_info()
        self.sup_info_fev.add_a_new_value()
        self.sup_info_anv.click_add_button()
        self.id_info.enter_identifying_info("DNS")

        """ REMIT CleanAddressPage """
        self.id_info.click_address_tab()
        self.addr.enter_domestic_master_vendor_address("REMIT", "Remit")
        self.addr.enter_business_phone()
        self.addr.enter_fax()

        """ CORPORATE INFORMATION """
        self.addr.click_add_new_address_btn()
        self.addr.enter_domestic_master_vendor_address("CORPORATE INFO", "Corporate Info")
        self.addr.expand_alternate_names()
        self.addr.enter_pmnt_alt_name_1()
        self.addr.enter_business_phone()
        self.addr.enter_fax()

        """ TRILOGIE PO ADDRESS """
        self.addr.click_add_new_address_btn()
        self.addr.enter_domestic_master_vendor_address("TRL PO ADDR", "Trilogie PO Address")
        self.addr.enter_pmnt_alt_name_1()
        self.addr.enter_business_phone()
        self.addr.enter_fax()

        # Add a location
        self.addr.click_location_tab()
        self.loc.add_location("MAIN", "Remit to Main")

        # Add Procurement Options
        self.loc.click_procurement_link()
        self.procurement.select_payment_terms_id("COD")

        # Add Branch Vendor(s)
        self.loc.click_fei_trilogie_xref_link()
        self.sup_xref.select_three_accounts("OHIOHVAC", "SACRAMENTO", "SANTAROSAWW")

        """ SAVE RECORD """
        self.loc.click_save_btn()
        self.loc.click_summary_tab()

        self.summary.get_supplier_id()

        result2 = self.summary.verify_supplier_id_created()
        self.ts.mark(result2, "Successfully Created Domestic Master Vendor.")

    @pytest.mark.run(order=3)
    def test_sign_out(self):
        self.summary.sign_out_summary_page()

        result = self.lp.verify_title_of_log_out_page()
        self.ts.mark_final("Test Create Master and Branch Vendor", result, "Successfully Signed Out of Application.")

    # @pytest.mark.run(order=4)
    # def test_verify_branch_vendor_creation(self):
    #     # Verify Branch Vendors were created successfully
    #     """  ADD CODE HERE """
    #     # Log into PSFT as VALIDATOR
    #     self.lp.login("AUTOTEST4", "Psoft1234$")
    #     result_1 = self.lp.verify_title()
    #     self.ts.mark(result_1, "Title is incorrect")
    #
    #     self.nav.navigate_to_supplier_info()
    #     self.sup_info_fev.enter_supplier_id("0001137869")
    #     self.sup_info_fev.click_search_btn()
    #     self.summary.click_location_tab()
    #     self.loc.click_fei_trilogie_xref_link()
    #
    #     result2 = self.sup_xref.verify_trl_vendor_id()
    #     self.ts.mark_final("test_bv_creations_domestic", result2,
    #                        "TRL Vendor ID exists: " + str(result2))
