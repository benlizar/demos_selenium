import json
import os
import unittest
import time
from pages.factory import PageFactory


class TestLoginUser(unittest.TestCase):

    def test_user_login(self):
        path = os.path.join(os.getcwd(), "tests", "values.json")
        with open(f"{path}", "r") as f:
            self.data = json.load(f)

        user = self.data['user_values']
        PageFactory.login.get_textbox_name().send_keys(user['email'])
        PageFactory.login.get_textbox_password().send_keys(user['password'])
        PageFactory.login.get_login_button().click()

        time.sleep(5)





