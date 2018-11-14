# coding=utf-8
import time
from ddt import ddt, data, unpack
import testmobile
from core import constants
from setting.test_test import setting
from setting.test_test import el
from setting.test_test.data import TestData

__author__ = 'zhaoyongze'

import unittest
'''
1、打开三只松鼠APK，点击个人中心 。（无登录的情况）
2、输入用户名、密码登录
3、点击首页，点击搜索。
4、搜索框中输入 “芒果干”点击搜索
5、把搜索结果第一个加入购物车。
6、下单并取消
'''

@ddt
class MyTestCase(unittest.TestCase):

    d = TestData().get('user_login')

    def setUp(self):
        self.dr = testmobile.Mobile(setting.desired_caps)
        pass

    @data(d[0])
    @unpack
    def test_something(self,name,password,mgg):
        time.sleep(10)
        contexts= self.dr.get_contexts()
        self.dr.switch_to_web(contexts[1])
        self.dr.click(constants.el_type_xpath)
        time.sleep(5)
        self.dr.send_keys(constants.el_type_xpath, el.szs_name,name)
        self.dr.send_keys(constants.el_type_xpath, el.szs_pass,password)
        time.sleep(5)
        self.dr.click(constants.el_type_xpath, el.szs_login)
        time.sleep(5)
        self.dr.click(constants.el_type_xpath, el.btn_sy)
        time.sleep(5)
        self.dr.click(constants.el_type_xpath, el.btn_ss)
        time.sleep(5)
        self.dr.send_keys(constants.el_type_xpath, el.szs_ss,mgg)
        time.sleep(2)
        self.dr.click(constants.el_type_xpath, el.szs_ss1)
        time.sleep(6)
        self.dr.click(constants.el_type_xpath, el.szs_jc)
        time.sleep(5)
        self.dr.click(constants.el_type_xpath, el.szs_gwc)
        time.sleep(20)
        self.dr.click(constants.el_type_xpath, el.szs_qjs)
        time.sleep(20)
        self.dr.click(constants.el_type_xpath, el.szs_qrf)
        time.sleep(10)
        self.dr.click_back()
        time.sleep(5)
        self.dr.click_back()
        self.dr.click_back()
        self.dr.click_back()
        self.dr.click_back()
        time.sleep(5)
        self.dr.click(constants.el_type_xpath, el.btn_grzx)
        time.sleep(3)
        self.dr.click(constants.el_type_xpath, el.szs_dfk)
        time.sleep(3)
        self.dr.click(constants.el_type_xpath, el.szs_dxq)
        time.sleep(3)
        self.dr.click(constants.el_type_xpath, el.szs_qx)
        time.sleep(3)
        self.dr.click(constants.el_type_xpath, el.szs_qr)
        pass



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

