import json
import os
import unittest
import time

from driver import utils
from pages.factory import PageFactory as pages


class TestLoginUser(unittest.TestCase):

    def test_user_login(self):
        path = os.path.join(os.getcwd(), "tests", "values.json")
        with open(f"{path}", "r") as f:
            self.data = json.load(f)

        user = self.data['user_values']
        pages.login.get_textbox_name().send_keys(user['email'])
        pages.login.get_textbox_password().send_keys(user['password'])
        pages.login.get_login_button().click()

        pages.organization.organization.click()
        pages.organization.hubs_list.click()
        pages.organization.button_create_hub.click()
        pages.organization.name.send_keys(utils.get_random_name())
        pages.organization.address.send_keys(utils.get_random_address())
        time.sleep(5)





