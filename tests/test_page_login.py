import json
import os
import unittest
import time
from pages.page_login import PageLogin


class TestLoginUser(unittest.TestCase):

    def test_user_login(self):
        # import JSON from "./test_page_login.json"
        path = os.path.join(os.getcwd(), "tests", "values.json")
        with open(f"{path}", "r") as f:
            self.data = json.load(f)

        user = self.data['user_values']
        login = PageLogin()
        login.get_textbox_name().send_keys(user['email'])
        login.get_textbox_password().send_keys(user['password'])
        login.get_login_button().click()

        assert '#2270' in login.get_grid().text




