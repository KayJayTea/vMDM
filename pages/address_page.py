from base.base_page import BasePage
from faker import Faker
from random import randint
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from popup_windows.look_up_state_window import LookUpStateWindow
from utilities.util import Util
import utilities.custom_logger as cl
import logging

STATE_ABBR = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE",
              "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY",
              "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC",
              "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR",
              "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VI",
              "VT", "WA", "WI", "WV", "WY"]

GBR_COUNTIES = [
    "ANS", "ANT", "ARD", "ARM", "AYR", "BEDS", "BERKS", "BFS", "BLA", "BLY", "BNB", "BORDER", "BRIST", "BUCKS", "CAMBS",
    "CENT", "CFK", "CGV", "CHES", "CHL IS", "CKT", "CLR", "CLV", "CLWYD", "CNWLL", "CSR", "CUMB", "D&G", "DERBY",
    "DEVON", "DGN", "DORSET", "DOW", "DRY", "DUR", "DYFED", "E YORK", "E.SUSX", "ESSEX", "FER", "FIFE", "GLOUCS",
    "GRAMP", "GT LON", "GT MAN", "GWENT", "GWYND", "HANTS", "HERTS", "HFORD", "HIGHLD", "INV", "IOM", "IOS", "IOW",
    "KENT", "LANCS", "LEICS", "LINCS", "LMV", "LOTH", "LRN", "LSB", "M GLAM", "MDDSX", "MERYSD", "MFT", "MOR", "MYL",
    "N YORK", "NDN", "NHANTS", "NORFLK", "NOTTS", "NTA", "NTHUMB", "NYM", "OMH", "ORK", "OXON", "PER", "POWYS",
    "RUTLND", "S GLAM", "SEL", "SHET", "SHROPS", "SOMER", "STAFFS", "STB", "STI", "STRATH", "SUFFK", "SURREY", "SYORKS",
    "T&W", "TAYS", "W GLAM", "W ISLS", "W SUSX", "WARWKS", "WILTS", "WOR", "WSTMID", "WYORKS"
]


class AddressPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # LOCATORS
    _summary_tab = "//a//span[contains(text(), 'ummary')]"  # XPATH
    _identifying_info_tab = "//a//span[contains(text(), 'dentifying Information')]"  # XPATH
    _contacts_tab = "//a//span[contains(text(), 'ontacts')]"  # XPATH
    _location_tab = "//span[text() = 'ocation']"  # XPATH
    _custom_tab = "//a//span[contains(text(), 'C')]"  # XPATH
    _supplier_name = "VENDOR_NAME1"
    _description_field = "VNDR_ADDR_SCROL_DESCR$0"
    _sam_address_type = "VNDR_ADDR_SCROL_CCR_ADDR_TYPE$0"
    _add_new_address_btn = "$ICField2$new$0$$0"
    _country = "VENDOR_ADDR_COUNTRY$0"
    _address_1 = "VENDOR_ADDR_ADDRESS1$0"
    _address_2 = "VENDOR_ADDR_ADDRESS2$0"
    _address_3 = "VENDOR_ADDR_ADDRESS3$0"
    _address_4 = "VENDOR_ADDR_ADDRESS4$0"
    _number = "VENDOR_ADDR_NUM1$0"
    _door = "VENDOR_ADDR_NUM2$0"
    _city = "VENDOR_ADDR_CITY$0"
    _county = "VENDOR_ADDR_COUNTY$0"
    _state = "VENDOR_ADDR_STATE$0"
    _postal = "VENDOR_ADDR_POSTAL$0"
    _email_id = "VENDOR_ADDR_EMAILID$0"
    _override_address_box = "CLN_OVERRIDE_ADDRESS"
    _alt_names_arrow = "VNDR_ADDR_WRK_VNDR_WTHD_LBL$0"
    _pmnt_alt_name_1 = "VENDOR_ADDR_NAME1$17$$0"
    _pmnt_alt_name_2 = "VENDOR_ADDR_NAME2$0"
    _wh_alt_name_1 = "VENDOR_ADDR_NAME1_WTHD$21$$0"
    _wh_alt_name_2 = "VENDOR_ADDR_NAME2_WTHD$0"
    _phone_type = "VENDOR_ADDR_PHN_PHONE_TYPE$0"
    _telephone_field = "VENDOR_ADDR_PHN_PHONE$0"
    _add_new_row_phone = "VENDOR_ADDR_PHN$new$0$$0"
    _search_state = "VENDOR_ADDR_STATE$prompt$img$0"
    _effective_date = "VENDOR_ADDR_EFFDT$0"

    """ Get the elements """
    def get_sam_address_type(self):
        return self.driver.find_element(By.ID, self._sam_address_type)

    def get_phone_type(self):
        return self.driver.find_element(By.ID, self._phone_type)

    """ Do something with the elements """
    def click_location_tab(self):
        self.element_click(self._location_tab, "xpath")
        self.util.sleep(2, "the Location page to open.")

    def enter_description(self):
        sup_name = self.driver.find_element(By.ID, "VENDOR_NAME1").text
        self.sendkeys(sup_name, self._description_field)

    def select_sam_address_type(self, sam_type):
        sel = Select(self.get_sam_address_type())
        sel.select_by_visible_text(sam_type)

    def enter_country_code(self, country_code):
        self.clear_element(self._country)
        self.sendkeys(country_code, self._country)
        self.sendkeys(Keys.TAB, self._country)
        self.util.sleep(1, "the country code to be recognized by the app.")

    def click_add_new_address_btn(self):
        self.element_click(self._add_new_address_btn)
        self.util.sleep(1)

    def enter_address_one(self):
        fake_data = Faker()
        fake_street_address = fake_data.street_address()
        self.sendkeys(fake_street_address, self._address_1)

    def enter_address_two(self):
        random_num = randint(1, 10)
        self.sendkeys("Bldg. " + str(random_num), self._address_2)

    def enter_address_three(self):
        self.sendkeys("N/A", self._address_3)

    def enter_city(self):
        fake_data = Faker()
        fake_city = fake_data.city()
        self.sendkeys(fake_city, self._city)

    def enter_postal_code(self):
        fake_data = Faker()
        fake_postal_code = fake_data.postalcode()
        self.sendkeys(fake_postal_code, self._postal)
        self.util.sleep(1, "the postal code to be recognized by the app.")

    def enter_random_state(self):
        self.sendkeys(str(choice(STATE_ABBR)), self._state)
        self.util.sleep(1, "the state to be recognized by the app.")

    def enter_email_id(self):
        fake_data = Faker()
        fake_email = fake_data.safe_email()
        self.sendkeys(fake_email, self._email_id)
        self.util.sleep(1, "the email to be recognized by the app.")

    def click_override_address_verification_chkbx(self):
        self.element_click(self._override_address_box)
        self.util.sleep(1, "the app recognizes the override.")

    def expand_alternate_names(self):
        self.element_click(self._alt_names_arrow)

    def click_add_new_phone_btn(self):
        self.element_click(self._add_new_row_phone)

    def search_for_state(self):
        self.element_click(self._search_state)

    def enter_random_gb_county(self):
        self.sendkeys(str(choice(GBR_COUNTIES)), self._state)
        self.util.sleep(2, "the state to be recognized by the app.")

    """ THIS IS THE MODULE THAT IS CALLED BY THE TEST """
    def enter_pmnt_alt_name_1(self):
        fake_data = Faker()
        fake_name = fake_data.name()
        self.sendkeys(fake_name, self._pmnt_alt_name_1)

    def enter_pmnt_alt_name_2(self):
        fake_data = Faker()
        fake_name = fake_data.name()
        self.sendkeys(fake_name, self._pmnt_alt_name_2)

    def enter_business_phone(self):
        sel = Select(self.get_phone_type())
        sel.select_by_visible_text("Business Phone")

        fake_data = Faker()
        fake_phone = fake_data.random_int(min=2000000, max=9999999)

        self.sendkeys("555" + str(fake_phone), self._telephone_field)
        self.element_click(self._add_new_row_phone)
        self.util.sleep(1, "the new phone row to be recognized by the app.")

    def enter_fax(self):
        sel = Select(self.get_phone_type())
        sel.select_by_visible_text("FAX")

        fake_data = Faker()
        fake_phone = fake_data.random_int(min=2000000, max=9999999)

        self.sendkeys("555" + str(fake_phone), self._telephone_field)
        self.element_click(self._add_new_row_phone)
        self.util.sleep(1, "the new phone row to be recognized by the app.")

    def enter_trilogie_dm_fax(self):
        sel = Select(self.get_phone_type())
        sel.select_by_visible_text("Trilogie DM Fax Number")

        fake_data = Faker()
        fake_phone = fake_data.random_int(min=2000000, max=9999999)

        self.sendkeys("555" + str(fake_phone), self._telephone_field)
        self.element_click(self._add_new_row_phone)
        self.util.sleep(1, "the new phone row to be recognized by the app.")

    def enter_all_phone_types(self):
        phone_type_list = ['Business Phone', 'FAX', 'Trilogie DM Fax Number']
        # phone_type_list = ['Business Phone', 'FAX']

        for phone_type in phone_type_list:
            sel = Select(self.get_phone_type())
            sel.select_by_visible_text(phone_type)

            fake_data = Faker()
            fake_phone = fake_data.random_int(min=2000000, max=9999999)

            self.sendkeys("555" + str(fake_phone), self._telephone_field)
            self.element_click(self._add_new_row_phone)
            self.util.sleep(1, "the new phone row to be recognized by the app.")

    def enter_domestic_master_vendor_address(self, sam_type):
        self.select_sam_address_type(sam_type)
        self.enter_address_one()
        self.enter_address_two()
        self.enter_city()
        self.enter_postal_code()
        self.enter_random_state()

    def enter_foreign_master_vendor_address(self, sam_type, country_code):
        self.select_sam_address_type(sam_type)
        self.enter_country_code(country_code)
        self.click_override_address_verification_chkbx()
        self.enter_address_one()
        self.enter_address_two()
        self.enter_city()
        self.enter_postal_code()

        if country_code == "GBR":
            self.search_for_state()
            county = LookUpStateWindow(self.driver)
            county.select_county(str(choice(GBR_COUNTIES)))
        else:
            self.search_for_state()
            state = LookUpStateWindow(self.driver)
            state.select_random_state()

    """ BEGIN CLEAN ADDRESS DEFINITIONS """
    def ca_enter_description(self, desc_text):
        self.sendkeys(desc_text, self._description_field)

    def ca_enter_effective_date(self):
        self.clear_element(self._effective_date)
        self.sendkeys("01/01/1901", self._effective_date)

    def ca_enter_address_one(self, address_1):
        self.sendkeys(address_1, self._address_1)

    def ca_enter_address_two(self, address_2):
        self.sendkeys(address_2, self._address_2)

    def ca_enter_location(self, location):
        self.sendkeys(location, self._address_2)

    def ca_enter_street(self, street):
        self.sendkeys(street, self._address_3)

    def ca_enter_address_four(self, address_4):
        self.sendkeys(address_4, self._address_4)

    def ca_enter_po_address(self, po_box):
        self.sendkeys(po_box, self._address_4)

    def ca_enter_city(self, city):
        self.sendkeys(city, self._city)

    def ca_enter_area(self, area):
        self.sendkeys(area, self._county)

    def ca_enter_district(self, district):
        self.sendkeys(district, self._city)

    def ca_enter_neighborhood(self, neighborhood):
        self.sendkeys(neighborhood, self._country)

    def ca_enter_postal(self, postal):
        self.sendkeys(postal, self._postal)
        self.util.sleep(1, "the postal to be recognized by the app.")

    def ca_enter_postal_code(self, postal_code):
        self.sendkeys(postal_code, self._postal)
        self.util.sleep(1, "the postal code to be recognized by the app.")

    def ca_enter_cap(self, cap):
        self.sendkeys(cap, self._postal)
        self.util.sleep(1, "the CAP to be recognized by the app.")

    def clear_state_field(self):
        self.clear_element(self._state)
        self.util.sleep(1, "the field to be cleared.")

    def search_for_canton(self):
        self.element_click(self._search_state)
        self.util.sleep(1, "the 'Look Up State' window to open.")

    def search_for_community(self):
        self.element_click(self._search_state)
        self.util.sleep(1, "the 'Look Up State' window to open.")

    def search_for_county(self):
        self.element_click(self._search_state)
        self.util.sleep(1, "the 'Look Up State' window to open.")

    def search_for_department(self):
        self.element_click(self._search_state)
        self.util.sleep(1, "the 'Look Up State' window to open.")

    def search_for_prefecture(self):
        self.element_click(self._search_state)
        self.util.sleep(1, "the 'Look Up State' window to open.")

    def search_for_province(self):
        self.element_click(self._search_state)
        self.util.sleep(1, "the 'Look Up State' window to open.")
    """ END CLEAN ADDRESS DEFINITIONS """

    """ CLEAN ADDRESSES """
    def clean_domestic_us_addresses(self, desc_text="UNITED STATES", sam_type="Corporate Info",
                                    address_1="The Westin New Orleans Canal Place",
                                    address_2="100 Rue Iberville",
                                    city="New Orleans",
                                    postal="70130"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ ANGUILLA """
    def clean_anguillian_address(self, desc_text="ANGUILLA", sam_type="Corporate Info",
                                 country_code="AIA",
                                 address_1="Carimar BCH Club",
                                 address_2="P.O. Box 327",
                                 city="Meads Bay",
                                 post_code="AI 2640"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.ca_enter_effective_date()
        self.select_sam_address_type(sam_type)
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(post_code)

    """ ARGENTINA """
    def clean_argentine_address(self, desc_text="ARGENTINA", sam_type="Corporate Info",
                                country_code="ARG",
                                address_1="Avenida Leandro",
                                address_2="N. Alem 1193",
                                city="Bueno Aires",
                                postal="1001",
                                state="BA"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)
        self.search_for_state()

        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)

    """ AUSTRALIA """
    def clean_australian_address(self, desc_text="AUSTRALIA", sam_type="Corporate Info",
                                 country_code="AUS",
                                 address_1="The Australian",
                                 address_2="100 Cumberland St",
                                 city="Sydney",
                                 postal="2000",
                                 state="NSW"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

        self.search_for_state()
        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)

    """ BARBADOS """
    def clean_barbados_address(self, desc_text="BARBADOS", sam_type="Corporate Info",
                               country_code="BRB",
                               address_1="The Garrison Historic Area",
                               address_2="Hastings, Christ Church",
                               city="Bridgetown",
                               post_code="BB15028"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(post_code)

    """ BELGIUM """
    def ca_enter_number_for_belgium(self, num):
        self.sendkeys(num, self._number)

    def clean_belgian_address(self, desc_text="BELGIUM", sam_type="Corporate Info",
                              country_code="BEL",
                              location="Monsiuer Alain Dupont",
                              street="Rue Du Vivier",
                              number="7",
                              city="Bruxelles",
                              postal="1000",
                              province="BC"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_location(location)
        self.ca_enter_street(street)
        self.ca_enter_number_for_belgium(number)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)
        self.clear_state_field()
        self.search_for_province()

        sel_prov = LookUpStateWindow(self.driver)
        sel_prov.select_state(province)
    """ BRAZIL """
    def clean_brazilian_address(self, desc_text="BRAZIL", sam_type="Corporate Info",
                                country_code="BRA",
                                address_1="Rua Escritor Jorge de Limao",
                                address_2="58",
                                city="Barra de Sao Miguel",
                                neighborhood="Barra mar", postal="57180-000",
                                state="AL"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_neighborhood(neighborhood)
        self.ca_enter_postal(postal)
        self.clear_state_field()

        self.search_for_state()
        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)

    """ BIOT """
    def clean_british_indian_ocean_territory_address(self, desc_text="BIOT", sam_type="Corporate Info",
                                                     country_code="IOT",
                                                     address_1="BIOT Administration",
                                                     address_2="King Charles Street",
                                                     city="N/A",
                                                     post_code="SW1A 2AH"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(post_code)

    """ CANADA """
    def clean_canadian_address(self, desc_text="CANADA", sam_type="Corporate Info",
                               country_code="CAN",
                               address_1="Sheraton Hotel",
                               address_2="35 Rue Laurier",
                               city="Gatineau",
                               post_code="J8X 4E9",
                               province="QC"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(post_code)

        self.search_for_province()
        sel_prov = LookUpStateWindow(self.driver)
        sel_prov.select_state(province)

    """ CHINA """
    def clean_china_address(self, desc_text="CHINA", sam_type="Corporate Info",
                            country_code="CHN",
                            address_1="16 Bin Shui Road",
                            address_2="He Xi District",
                            city="Tianjin",
                            post_code="300061"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(post_code)

    """ FRANCE """
    def clean_french_address(self, desc_text="FRANCE", sam_type="Corporate Info",
                             country_code="FRA",
                             address_1="Holiday Inn Paris - Gare de Lyon Bastille",
                             address_2="11 Rue de Lyon",
                             city="Paris",
                             postal="75012",
                             department="75"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)
        self.clear_state_field()  # Clear Department field

        self.search_for_department()
        sel_dept = LookUpStateWindow(self.driver)
        sel_dept.select_state(department)

    """ GERMANY """
    def clean_germany_address(self, desc_text="GERMANY",
                              sam_type="Corporate Info", country_code="DEU",
                              address_1="Moxy Munich Messe",
                              address_2="Otto-Hahn 21",
                              city="Aschheim",
                              postal="85609",
                              state="BY"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(postal)

        self.search_for_state()
        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)

    def clean_germany_po_address(self, desc_text="GERMANY (PO BOX)", sam_type="Corporate Info",
                                 country_code="DEU",
                                 address_1="Sitfung Warentest",
                                 po_box="Postfach 3 14 41",
                                 city="Berlin",
                                 postal="10724",
                                 state="BE"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_po_address(po_box)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(postal)

        self.search_for_state()
        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)

    """ HONG KONG """
    def clean_hong_kong_address(self, desc_text="HONG KONG", sam_type="Corporate Info",
                                country_code="HKG",
                                address_1="International Commerce Center",
                                address_2="No. 1 Austin Road West",
                                district="Kowloon",
                                area="Kowloon"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_district(district)
        self.ca_enter_area(area)

    """ ISRAEL """
    def clean_israel_address(self, desc_text="ISRAEL", sam_type="Corporate Info",
                             country_code="ISR",
                             address_1="The Drisco Hotel",
                             address_2="Rehov Auerbach 6",
                             city="Tel Aviv",
                             postal="6100002"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ ITALY """
    def clean_italian_address(self, desc_text="ITALY", sam_type="Corporate Info",
                              country_code="ITA",
                              address_1="Via Bruno Buozzi, 35",
                              address_2="Bldg. 3",
                              city="Bozano",
                              cap="39100",
                              province="BZ"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_cap(cap)

        self.search_for_province()
        sel_prov = LookUpStateWindow(self.driver)
        sel_prov.select_state(province)

    """ JAPANESE """
    def clean_japanese_address(self, desc_text="JAPAN", sam_type="Corporate Info",
                               country_code="JPN",
                               address_1="1-1-43 ABENO-SUJI",
                               address_2="ABENO-KU",
                               city="Osaka",
                               postal="545-0052",
                               prefecture="27"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

        self.clear_state_field()  # Clear Prefecture field
        self.search_for_prefecture()
        sel_pref = LookUpStateWindow(self.driver)
        sel_pref.select_state(prefecture)

    """ MALAYSIA """
    def clean_malaysian_address(self, desc_text="MALAYSIA", sam_type="Corporate Info",
                                country_code="MYS",
                                address_1="Jalan Pantai 3",
                                address_2="Dessaru",
                                city="Bandar Penawar",
                                postal="81930",
                                state="01"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

        self.search_for_state()
        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)

    """ MEXICO """
    def clean_mexican_address(self, desc_text="MEXICO", sam_type="Corporate Info",
                              country_code="MEX",
                              street_and_num_1="Mission De Los Lagos 9020",
                              street_and_num_2="Partido Iglesias",
                              colony="Ciudad",
                              city="Juarez",
                              post_code="32688",
                              state="CHIH"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(street_and_num_1)
        self.ca_enter_address_two(street_and_num_2)
        self.ca_enter_address_three(colony)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(post_code)

        self.search_for_state()
        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)

    """ NETHERLANDS """
    def enter_number_for_netherlands(self, num):
        self.sendkeys(num, self._number)

    def clean_netherlands_address(self, desc_text="NETHERLANDS", sam_type="Corporate Info",
                                  country_code="NLD",
                                  location="Amsterdam Marriott Hotel",
                                  street="Stadhouderskade",
                                  number="12",
                                  city="Amsterdam",
                                  postal="1054 ES",
                                  community="0776"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_location(location)
        self.ca_enter_street(street)
        self.enter_number_for_netherlands(number)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(postal)

        self.search_for_community()
        sel_comm = LookUpStateWindow(self.driver)
        sel_comm.select_state(community)

    """ NEW ZEALAND """
    def clean_new_zealand_address(self, desc_text="NEW ZEALAND", sam_type="Corporate Info",
                                  country_code="NZL",
                                  address_1="The St. James",
                                  address_2="20 Chisholm Crescent",
                                  city="Hanmer Springs",
                                  postal="7360"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ PANAMA """
    def clean_panama_address(self, desc_text="PANAMA", sam_type="Corporate Info",
                             country_code="PAN",
                             address_1="La Rotunda Avenue",
                             address_2="Costa del Este",
                             city="Panama",
                             postal="1001"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ PHILIPPINES """
    def clean_philippines_address(self, desc_text="PHILIPPINES", sam_type="Corporate Info",
                                  country_code="PHL",
                                  address_1="1588 Pedro Gil St",
                                  address_2="Corner MH del Pilar",
                                  city="Manila",
                                  postal="1004"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ PORTUGAL """
    def clean_portugal_address(self, desc_text="PORTUGAL", sam_type="Corporate Info",
                               country_code="PRT",
                               address_1="Rua das Palmeiras",
                               address_2="Lote 5 Quinta da Marinha",
                               city="Cascais",
                               postal="2750-005"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ SINGAPORE """
    def clean_singapore_address(self, desc_text="SINGAPORE", sam_type="Corporate Info",
                                country_code="SGP",
                                address_1="Courtyard Singapore Novena",
                                address_2="99 Irrawaddy Road",
                                postal="329568"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_postal(postal)

    """ SPAIN """
    def enter_number_for_spain(self, num):
        self.sendkeys(num, self._number)

    def enter_door_for_spain(self, door):
        self.sendkeys(door, self._door)

    def clean_spain_address(self, desc_text="SPAIN", sam_type="Corporate Info",
                            country_code="ESP",
                            address_1="AC Hotel Coruna",
                            address_2="Enrique Marinas",
                            number="34",
                            door="A",
                            city="Coruna",
                            postal_code="15009",
                            province="C"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.enter_number_for_spain(number)
        self.enter_door_for_spain(door)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(postal_code)

        self.search_for_province()
        sel_prov = LookUpStateWindow(self.driver)
        sel_prov.select_state(province)

    """ SWAZILAND """
    def clean_swaziland_address(self, desc_text="SWAZILAND", sam_type="Corporate Info",
                                country_code="SWZ",
                                address_1="Summerfield Botanical Garden",
                                address_2="Matshpa Valley Rd.",
                                city="Manzini",
                                postal="M200"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ SWITZERLAND """
    def clean_swiss_address(self, desc_text="SWITZERLAND", sam_type="Corporate Info",
                            country_code="CHE",
                            address_1="The Cambrian, Abelboden",
                            address_2="Dorfstrasse 7",
                            city="Adelboden",
                            postal="3715",
                            canton="BE"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

        self.search_for_canton()
        sel_canton = LookUpStateWindow(self.driver)
        sel_canton.select_state(canton)

    """ UNITED KINGDOM """
    def clean_united_kingdom_address(self, desc_text="UNITED KINGDOM", sam_type="Corporate Info",
                                     country_code="GBR",
                                     address_1="160 Warfside Street",
                                     address_2="The Mailbox",
                                     city="Birmingham",
                                     post_code="B1 1RL",
                                     state="WSTMID"):
                self.clear_element(self._description_field)
                self.ca_enter_description(desc_text)
                self.select_sam_address_type(sam_type)
                self.ca_enter_effective_date()
                self.enter_country_code(country_code)
                self.ca_enter_address_one(address_1)
                self.ca_enter_address_two(address_2)
                self.ca_enter_city(city)
                self.ca_enter_postal_code(post_code)

                self.search_for_county()
                sel_county = LookUpStateWindow(self.driver)
                sel_county.select_state(state)

    """ VIRGIN ISLANDS (BRITISH) """
    def clean_virgin_islands_british_address(self, desc_text="BRITISH VIRGIN ISLANDS", sam_type="Corporate Info",
                                             country_code="VGB",
                                             address_1="Frenchmans (Hotel)",
                                             address_2="Frenchman's Cay",
                                             city="Tortola",
                                             postal="VG100"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal(postal)

    """ INDIA """
    def clean_indian_address(self, desc_text="INDIA", sam_type="Corporate Info",
                             country_code="IND",
                             address_1="1234 Test Street",
                             address_2="BLDG 3",
                             city="Chennai",
                             post_code="600073",
                             state="TN"):
        self.clear_element(self._description_field)
        self.ca_enter_description(desc_text)
        self.select_sam_address_type(sam_type)
        self.ca_enter_effective_date()
        self.enter_country_code(country_code)
        self.ca_enter_address_one(address_1)
        self.ca_enter_address_two(address_2)
        self.ca_enter_city(city)
        self.ca_enter_postal_code(post_code)

        self.search_for_state()
        sel_state = LookUpStateWindow(self.driver)
        sel_state.select_state(state)
