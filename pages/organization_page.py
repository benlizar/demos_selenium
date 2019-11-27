from selenium.webdriver.common.by import By

from pages.anotaciones import element
from pages.base_page import BasePage


class PageOrganization(BasePage):
    _organization = (By.XPATH, "//a[contains(@href, '/admin/organization/')]/..")
    _hubs_list = (By.XPATH, "//div[@class='ant-tabs-nav ant-tabs-nav-animated']/div/div[2]")
    _create_hub_button = (By.XPATH, "//*[contains(@class,'ant-tabs-tabpane "
                                    "ant-tabs-tabpane-active')]/div[2]/div[2]/div/button")
    _name = (By.XPATH, "//input[@name ='name']")
    _address = (By.XPATH, "//form/div[2]/div[2]/div[1]/div[2]//input")
    _dispatch_id = (By.XPATH, "//input[@name ='dispatch_warehouse_code']")
    _phone_number = (By.XPATH, "//input[@name ='phones[0][1]']")
    _country_select = None
    _button_create = (By.XPATH, "//*[contains(@class,'ant-tabs-tabpane "
                                "ant-tabs-tabpane-active')]/div[2]/div[2]/div/button")
    _address_suggestion = (By.XPATH, "//form/div[2]/div[2]/div[1]/div[2]//input/../../div")
    _submit_button = (By.XPATH, "//form/div[3]/div/div/button")
    _search_bar = (By.XPATH, "//header/div[2]//input")
    _hub_name = None
    _options_button = None
    _delete_button = None
    _deactivate_hub = None
    _accept_deactivate = (By.XPATH,
                          "//div[contains(@class, 'ant-modal-body')]/div/div[3]/div/div[2]/div/button")

    @property
    @element
    def organization(self):
        return self._organization

    @property
    @element
    def hubs_list(self):
        return self._hubs_list

    @property
    @element
    def name(self):
        return self._name

    @property
    @element
    def address(self):
        return self._address

    @property
    @element
    def address_suggestion(self):
        return self._address_suggestion

    @property
    @element
    def dispatch_id(self):
        return self._dispatch_id

    @property
    @element
    def button_create_hub(self):
        return self._button_create

    @property
    @element
    def country_select_input(self):
        return self._country_select

    @property
    @element
    def phone_number(self):
        return self._phone_number

    @property
    @element
    def submit_button(self):
        return self._submit_button
