# coding=utf-8

__author__ = 'heyanping'

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.shop import shop_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting
from setting.hyptest.data_login import TestData
from ddt import ddt, data, unpack


@ddt
class shoplogin(unittest.TestCase):
    d = TestData().get("shop_user_login_success")
    e = TestData().get("shop_user_login_failed")

    def setUp(self):
        """初始化方法，在所有test执行前执行"""
        # 初始化浏览器对象，从setting文件中的driver_type读取启动浏览器的类型（ff\firefox、chrome、ie、opera等）
        self.dr = comall.Comall(setting.driver_type)
        time.sleep(1)
        # 最大化浏览器窗口
        self.dr.max_window()
        # 打开测试地址
        #self.dr.open("http://172.31.0.253/login")
        time.sleep(1)
        shop_common.shop_area_select(self.dr)


    @data(d[0], d[1])
    @unpack
    def test_first_case(self, login_name_data, login_pw_data, shop_login_top_name, message):
        """登录成功case"""
        # 获得setUp初始化的对象
        dr = self.dr
        # 点击首页登录按钮,跳转到登录页面
        dr.click("xpath", el.shop_index_login)
        time.sleep(1)
        # 检查登录输入框存在
        dr.until("xpath", el.shop_login_name)
        # 用户名输入
        #dr.send_keys("xpath", el.shop_login_name, data_login.login_name_data)
        dr.send_keys("xpath", el.shop_login_name, login_name_data)
        # 密码输入
        #dr.send_keys("xpath", el.shop_login_pw_edit, data_login.login_pw_data)
        dr.send_keys("xpath", el.shop_login_pw_edit, login_pw_data)
        # 点击登录按钮
        dr.click("xpath", el.shop_login_button)
        time.sleep(2)
        #dr.open("http://172.31.0.253/index")
        # 检查是否登录成功
        shop_login_name = dr.get_text("xpath", el.shop_login_top_name)
        self.assertEqual(login_name_data, shop_login_name, message)

    @data(e[0], e[1], e[2])
    @unpack
    def test_second_case(self, login_name_data, login_pw_data, shop_login_top_name, message):
        """用户名错误case"""
        # 获得setUp初始化的对象
        dr = self.dr
        # 点击首页登录按钮,跳转到登录页面
        dr.click("xpath", el.shop_index_login)
        time.sleep(1)
        # 检查登录输入框存在
        dr.until("xpath", el.shop_login_name)
        # 用户名输入
        dr.send_keys("xpath", el.shop_login_name, login_name_data)
        # 密码输入
        dr.send_keys("xpath", el.shop_login_pw_edit, login_pw_data)
        # 点击登录按钮
        dr.click("xpath", el.shop_login_button)
        time.sleep(2)
        # 检查是否登录成功
        error_message = dr.get_text("xpath", el.shop_login_error_message)
        dr.debug_info(error_message)
        self.assertEqual(shop_login_top_name, error_message, message)


    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(shoplogin)
    result = unittest.TextTestRunner(verbosity=2).run(suite)