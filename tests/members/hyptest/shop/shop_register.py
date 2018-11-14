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
from setting.hyptest.data_register import TestData
from ddt import ddt, data, unpack


@ddt
class shopregister(unittest.TestCase):
    d = TestData().get("shop_user_register_success")
    e = TestData().get("shop_user_register_failed")

    def setUp(self):
        """初始化方法，在所有test执行前执行"""
        # 初始化浏览器对象，从setting文件中的driver_type读取启动浏览器的类型（ff\firefox、chrome、ie、opera等）
        self.dr = comall.Comall(setting.driver_type)
        time.sleep(1)
        # 最大化浏览器窗口
        self.dr.max_window()
        time.sleep(1)
        # 调用地址
        shop_common.shop_area_select(self.dr)

    @data(d[0])
    @unpack
    def test_first_case(self, register_data, phoneVerifyCode, mobileVerifyCode, password, resetpassword, outputmessage, message):
        """测试case，必须以test开头命名"""
        # 获得setUp初始化的对象
        dr = self.dr
        # 点击首页注册按钮,跳转到注册页面
        dr.click("xpath", el.shop_index_register)
        time.sleep(1)
        # 手机号码输入
        dr.send_keys("xpath", el.shop_register_mobile, register_data)
        # 图片验证码
        dr.send_keys("xpath", el.shop_register_phoneVerifyCode, phoneVerifyCode)
        # 手机验证码
        dr.send_keys("xpath", el.shop_register_mobileVerifyCode, mobileVerifyCode)
        # 设置密码
        dr.send_keys("xpath", el.shop_register_password_mobile, password)
        # 确认密码
        dr.send_keys("xpath", el.shop_register_password_mobile_confirm, resetpassword)
        # 选中协议
        dr.click("xpath", el.shop_register_chk_mobile)
        # 点击注册按钮
        dr.click("xpath", el.shop_register_btn_submitMobile)
        time.sleep(2)
        #dr.click("xpath", el.shop_register_btn_goShop)
        # 检查是否注册成功
        shop_nickname = dr.get_text("xpath", el.shop_nickname)
        self.assertEqual(outputmessage, shop_nickname, message)

    @data(e[0])
    @unpack
    def test_second_case(self, register_data, phoneVerifyCode, mobileVerifyCode, password, resetpassword, outputmessage, message):
        """测试case，必须以test开头命名"""
        # 获得setUp初始化的对象
        dr = self.dr
        # 点击首页注册按钮,跳转到注册页面
        dr.click("xpath", el.shop_index_register)
        time.sleep(1)
        # 手机号码输入
        dr.send_keys("xpath", el.shop_register_mobile, register_data)
        # 图片验证码
        dr.send_keys("xpath", el.shop_register_phoneVerifyCode, phoneVerifyCode)
        # 手机验证码
        dr.send_keys("xpath", el.shop_register_mobileVerifyCode, mobileVerifyCode)
        # 设置密码
        dr.send_keys("xpath", el.shop_register_password_mobile, password)
        # 确认密码
        dr.send_keys("xpath", el.shop_register_password_mobile_confirm, resetpassword)
        # 选中协议
        dr.click("xpath", el.shop_register_chk_mobile)
        # 点击注册按钮
        dr.click("xpath", el.shop_register_btn_submitMobile)
        time.sleep(2)
        #dr.click("xpath", el.shop_register_btn_goShop)
        # 检查是否注册成功
        error_message = dr.get_text("xpath", el.shop_reput_mobile)
        dr.debug_info(error_message)
        self.assertEqual(outputmessage, error_message, message)


    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(shopregister)
    result = unittest.TextTestRunner(verbosity=2).run(suite)