# coding=utf-8

import time
import unittest
import comallmobile
from ddt import ddt, data, unpack
from core import constants
from setting.hyptest import setting
from setting.hyptest import el_appium
from setting.hyptest.data_appium import TestData

@ddt
class HYPTestCase(unittest.TestCase):

    d = TestData().get('user_login')

    def setUp(self):
        self.dr = comallmobile.ComallMobile(setting.desired_caps)
        pass

    @data(d[0])
    @unpack
    def test_a_index(self, loginname, password):

        contexts= self.dr.get_contexts()
        self.dr.switch_to_web(contexts[1])
        #点击进入首页按钮
        self.dr.click(constants.el_type_xpath, el_appium.bg_comein_index)
        time.sleep(5)
        #关闭首页弹出层
        self.dr.click(constants.el_type_xpath, el_appium.bg_activity_closebtn)
        # 点击全球购图标
        self.dr.click(constants.el_type_xpath, el_appium.bg_global_icon)
        time.sleep(5)
        # 单品精选-第一个商品加入购物车按钮
        self.dr.click(constants.el_type_xpath, el_appium.bg_cart)
        time.sleep(5)
        # 进入底部导航栏-购物车，进入购物车页面
        self.dr.click(constants.el_type_xpath, el_appium.bg_cart_icon)
        time.sleep(5)
        # 点击购物车-去结算按钮
        self.dr.click(constants.el_type_xpath, el_appium.bg_check_btn)
        time.sleep(10)
        # 跳转登录页-输入手机号
        self.dr.send_keys(constants.el_type_xpath, el_appium.bg_mobile_num, loginname)
        # 跳转登录页-输入密码
        self.dr.send_keys(constants.el_type_xpath, el_appium.bg_mobile_password, password)
        time.sleep(5)
        # 跳转登录页-点击登录按钮
        gologin = self.dr.get_element(constants.el_type_xpath, el_appium.bg_login_btn)
        location=gologin.location
        self.dr.switch_to_nat()
        # # element_locator = Element()
        login_button_location = [int(location['x'])*2+10, int(location['y']*2+45)]
        login_button_location = [351, 418]
        res=self.dr.tap([login_button_location])
        print res
        text = self.dr.get_text(constants.el_type_xpath, el_appium.bg_login_name)
        print text
        self.dr.assert_equal(text, loginname, '登录失败', False, self.__class__.__name__)

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HYPTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
