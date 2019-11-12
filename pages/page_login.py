from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PageLogin(BasePage):
    _textbox_email = (By.ID, "email")
    _textbox_password = (By.ID, "password")
    _button_login = (By.ID, 'button')
    _grid = (By.XPATH, "//*[@class='table __table_white']//a[contains(text(),'#2270')]")

    def get_textbox_name(self):
        return self.find_element(self._textbox_email)

    def get_textbox_password(self):
        return self.find_element(self._textbox_password)

    def get_login_button(self):
        return self.find_element(self._button_login)

    def get_grid(self):
        return self.find_element(self._grid)

# Completar Login | Mejoras
#  EC & IMPLICITS WAITS
# TODO: Xpath - Inputs types[Checkbox, Radiobutton, File,...]
# TODO: Annotations - Decorator | Factory[Method Factory, Abstract Factory, Factory builder]
