# coding = utf-8

import comall
import time
import unittest
import setting.qiguojie.setting as my_set
from setting.qiguojie import data
from setting.qiguojie import el


class QiGuoJieTest(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(my_set.driver_type)
        self.dr.open(my_set.carrefour)
        self.dr.max_window()
        time.sleep(3)

    def test_iframe(self):
        qq = self.dr
        qq.send_keys("xpath", el.c_login_username_input, "qtest01")
        qq.send_keys("xpath", el.c_login_password_input, "techqa")
        qq.click("xpath", el.c_login_submit_btn)
        time.sleep(2)
        qq.until_page_load()
        qq.click("xpath", el.c_dashboard_items_member)
        time.sleep(2)
        qq.js("window.scrollTo(0,100)")
        time.sleep(2)
        qq.click("xpath", el.c_dashboard_items_member_manage)

        time.sleep(3)

        qq.switch_to_frame()

        qq.click("xpath", el.c_member_add_btn)

        # qq.switch_to_frame_out()
        #
        # qq.click("xpath", el.c_dashboard_items_member)

    def tearDown(self):
        # qq = self.dr
        # qq.quit()
        pass


if __name__ == "main":
    pass