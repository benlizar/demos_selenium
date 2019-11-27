from selenium.webdriver.common.by import By

from pages.anotaciones import element
from pages.base_page import BasePage


class PageLogin(BasePage):
    _textbox_email = (By.ID, "email")
    _textbox_password = (By.ID, "password")
    _button_login = (By.ID, 'button')
    _grid = (By.XPATH, "//*[@class='table __table_white']//a[contains(text(),'#2270')]")
    _dispatch = (By.XPATH, "//a[text()= 'Despachos']")

    @element
    def get_textbox_name(self):
        return self._textbox_email

    @element
    def get_textbox_password(self):
        return self._textbox_password

    @element
    def get_login_button(self):
        return self._button_login

    @element
    def get_grid(self):
        return self._grid

    @element
    def dispatch(self):
        return self._dispatch

# Completar Login | Mejoras
#  EC & IMPLICITS WAITS
# Xpath - Inputs types[Checkbox, Radiobutton, File,...]
# TODO: Annotations - Decorator | Factory[Factory builder]
# TODO: Reporting
# TODO: ActionsChains Selenium
