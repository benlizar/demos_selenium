from driver.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    _driver = None

    def __init__(self):
        self.llamar_driver()

    def llamar_driver(self):
        self._driver = Driver.getInstance()
        self._driver.set_up()
        self._driver.goto_login()

        # return self._driver.get_driver().find_element(by=element[0], value=element[1])
    def get_title(self):
        return self._driver.get_driver().title

    def go_to(self, uri):
        print('Navigate to url')

