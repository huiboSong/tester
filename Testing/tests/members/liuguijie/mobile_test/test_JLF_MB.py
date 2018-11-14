# coding=utf-8
__author__ = 'liuguijie'
import time
from ddt import ddt, data, unpack
import testmobile
from core import constants
from setting.test_test import setting
from setting.test_test import el
from setting.test_test import data

import unittest

@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dr = testmobile.Mobile(setting.desired_caps)
        pass

    # @data(my_data[0])
    # @unpack
    def test_something(self, user, password, error_message1):
        mydr = self.dr
        time.sleep(15)
        mydr.swipe(765,692,3,954,1000)
        time.sleep(15)
        mydr.switch_to_web()
        # 点击进入首页
        mydr.click(mb_el.xptah_type, mb_el.c_login_APPhomepage_btn)
        time.sleep(5)
        # 点击全球购
        mydr.click(mb_el.xptah_type, mb_el.c_APPhomepage_Gshop_btn)
        time.sleep(5)
        # 点击加入购物车   第一件商品
        mydr.click(mb_el.xptah_type, mb_el.c_Gshop_add1_btn)
        time.sleep(5)
        # 点击购物车
        mydr.click(mb_el.xptah_type, mb_el.c_Gshop_Scart_mdr)
        time.sleep(5)
        # 点击结算
        mydr.click(mb_el.xptah_type, mb_el.c_Scart_stt_btn)
        time.sleep(3)
        # 输入账户
        mydr.send_keys(mb_el.xptah_type, mb_el.c_login_user_input, user)
        time.sleep(2)
        # 输入密码
        mydr.send_keys(mb_el.xptah_type, mb_el.c_login_password_input, password)
        time.sleep(1)
        # 点击登录
        time.sleep(8)
        mydr.click(mb_el.xptah_type, mb_el.c_login_btn)
        # 获取购物车页面  “购物车”文字     shopping_cart 购物车
        shopping_cart = mydr.get_text(mb_el.xptah_type, mb_el.c_Scart_Scart1)
        self.assertEqual(u"购物车", shopping_cart, error_message1)


    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
