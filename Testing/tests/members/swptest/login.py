# coding=utf-8
__author__ = 'sun'

import unittest
import comall
import time
from setting.swptest import setting
from setting.swptest import el
from setting.swptest.data import TestData
from ddt import ddt, data, unpack


@ddt
class Login (unittest.TestCase):
    m = TestData().get("wm_login")
    # 测试执行前的方法

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()

    @data(m[0], m[1])
    @unpack
    def test_login(self, username, pwd):
        dr = self.dr
        #打开我买网首页
        dr.open(setting.womai_online_url)
        #点击首页登录链接
        dr.click("xpath", el.womai_index_topbtn_login_a)
        time.sleep(3)
        #登录页面输入用户名
        dr.send_keys("xpath", el.login_username, username)
        time.sleep(3)
        #登录页面输入密码
        dr.send_keys("xpath", el.login_pwd, pwd)
        time.sleep(3)
        #点击登录按钮
        dr.click("xpath", el.login_btn)
        time.sleep(3)

    def tearDown(self):
        #关闭浏览器
        dr = self.dr
        dr.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

