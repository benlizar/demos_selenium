from driver.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    _driver = None

    def __init__(self):
        self.llamar_driver()

    def llamar_driver(self):
        self._driver = Driver()
        self._driver.set_up()
        self._driver.goto_login()

    def find_element(self, element):
        return WebDriverWait(self._driver.get_driver(), 10).until(
            EC.visibility_of_element_located((element[0], element[1]))
        )

        # return self._driver.get_driver().find_element(by=element[0], value=element[1])
    def get_title(self):
        return self._driver.get_driver().title

    def go_to(self, uri):
        print('Navigate to url')

