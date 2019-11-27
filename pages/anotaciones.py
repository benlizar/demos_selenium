from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver.driver import Driver


def element(func):
    def wrapper(*args, **kwargs):
        # class_name = args[0].__class__.__name__
        # element_name = func.__name__
        locator = func(*args, **kwargs)
        driver = Driver.getInstance()

        _element = WebDriverWait(driver.get_driver(), 10).until(
            EC.visibility_of_element_located(locator)
        )
        return _element
    return wrapper
