# coding=utf-8

import unittest
import time

from ddt import ddt

import comall
from setting.hyptest import el
from setting.hyptest import setting
from logs.tests.members.hyptest.shop import common


@ddt
class Logout(unittest.TestCase):
    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        common.login_success(self.dr, self)


    def test_loginout(self):
        dr = self.dr
        time.sleep(1)
        dr.click("xpath", el.shop_index_logout)
        #判断是否退出成功
        message = dr.get_text("xpath", el.shop_index_login)
        print message
        self.assertEqual(message, "[登录]", "退出成功")

    def tearDown(self):
        dr = self.dr
        dr.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Logout)
    result = unittest.TextTestRunner(verbosity=2).run(suite)