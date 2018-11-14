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
        self.dr.open(my_set.local_url)
        self.dr.max_window()
        time.sleep(3)

    def test_q(self):
        qq = self.dr
        qq.click("xpath", el.localhost_confirm_btn)
        time.sleep(5)
        qq.accept_alert()

    def test_q_1(self):
        qq = self.dr
        qq.click("xpath", el.localhost_alert_btn)
        time.sleep(5)
        qq.accept_alert("ok")  # "cannel"

    def tearDown(self):
        # qq = self.dr
        # qq.quit()
        pass


if __name__ == "main":
    pass