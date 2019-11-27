from selenium import webdriver


class Driver(object):
    _driver = None
    _url = "https://tms-qa.liftit-sandbox.com/login"

    def set_up(self):
        self._driver = webdriver.Chrome()

    def get_driver(self):
        return self._driver

    def goto_login(self):
        self._driver.get(self._url)

    def tear_down(self):
        self._driver.quit()

    @staticmethod
    def getInstance():
        if Driver._driver is None:
            Driver()
        return Driver._driver

    def __init__(self):
        Driver._driver = self
