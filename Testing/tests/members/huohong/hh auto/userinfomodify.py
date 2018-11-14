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
        dr = self.dr
        # 检查并点击我的账户框存在
        dr.until("xpath", el.womai_myaccount_a)
        dr.click("xpath", el.womai_myaccount_a)
        # 打开新窗口
        dr.switch_next_window()
        # 输入用户名密码
        dr.send_keys("xpath", el.womai_name_inoput_login_t,login_name)
        dr.send_keys("xpath", el.womai_pwd_inoput_login_t, pw)
        # 点击登录按钮
        dr.click("xpath", el.womai_info_submit_login_btn)
        login_name = dr.get_text("xpath", el.womai_login_success_login_t)
        # 检查是否登录成功
        self.assertEqual('springhh，您好!',login_name, '登陆成功')

        # 检查并点击我的账户框存在
        dr.until("xpath", el.womai_accountcenter_myinfo_a)
        dr.click("xpath", el.womai_accountcenter_myinfo_a)
        time.sleep(2)
        dr.switch_to_frame()
        # 输入用户名密码
        dr.send_keys("xpath", el.womai_myinfo_name, u"科码1")
        dr.click("xpath", el.womai_myinfobtn_submit_btn)
        time.sleep(2)
        dr.switch_to_frame_out()
        time.sleep(2)
        message = dr.get_text("xpath", el.womai_myinfo_text)
        #self.assertEqual("修改资料成功！", message，"操作成功")
        self.assertEquals(u"修改资料成功！" , message,"操作成功")



    def tearDown(self):
       pass




if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    result = unittest.TextTestRunner(verbosity=2).run(suite)