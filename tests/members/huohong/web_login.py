# coding=utf-8

import unittest
import time
import comall
from setting.huohong import el
from setting.huohong import setting
from setting.huohong.data import TestData
from ddt import ddt, data, unpack


@ddt
class Login(unittest.TestCase):

    d = TestData().get("user_login_success")

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        #self.dr.max_window()
        self.dr.open(setting.womai_url)
        time.sleep(1)

    @data(d[0])
    @unpack
    def test_login_success(self,login_name, pw,message):
        u"""成功登录测试账号"""
        dr = self.dr
        # 检查登录输入框存在
        dr.until("xpath", el.womai_index_topbtn_login_a)
        time.sleep(2)
        dr.click("xpath", el.womai_index_topbtn_login_a)
        # 用户名输入
        dr.send_keys("xpath", el.womai_name_inoput_login_a,login_name)
        time.sleep(2)
        # 密码输入
        dr.send_keys("xpath", el.womai_pwd_inoput_login_a, pw)
        time.sleep(2)
        # 点击登录按钮
        dr.click("xpath", el.womai_info_submit_login_a)
        time.sleep(2)
        login_name = dr.get_text("xpath", el.womai_login_success_login_a)

        # 检查是否登录成功
        self.assertEqual('springhh，您好!',login_name, '登录成功')

        #self.assertEqual('user_name', login_name, '登陆成功')


    def tearDown(self):
        dr = self.dr
        time.sleep(2)
        dr.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    result = unittest.TextTestRunner(verbosity=2).run(suite)