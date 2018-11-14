# coding=utf-8
import time

import comallmobile
from core import constants
from setting.zx_test import setting
from setting.zx_test import el
from setting.zx_test.Elements import Element


__author__ = 'zhangxue'

import unittest

'''
1、打开三只松鼠APK，点击个人中心 。（无登录的情况）
2、输入用户名、密码登录
3、点击首页，点击搜索。
4、搜索框中输入 “芒果干”点击搜索
5、把搜索结果第一个加入购物车。
'''


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dr = comallmobile.ComallMobile(setting.desired_caps)

    def test_something(self):
        time.sleep(10)
        contexts = self.dr.get_contexts()
        source = self.dr.page_source()
        print source
        self.dr.switch_to_web(contexts[1])
        source_2 = self.dr.page_source()
        print source_2
        # time.sleep(10)
        # self.dr.click(constants.el_type_xpath, el.jlf_cancel)
        time.sleep(10)
        self.dr.click(constants.el_type_xpath, el.jlf_index)
        time.sleep(10)
        # self.dr.click(constants.el_type_xpath, el.jlf_no)
        # time.sleep(10)


        # loc= [40,150]
        # res=self.dr.tap([loc])
        self.dr.click(constants.el_type_xpath, el.jlf_person)
        time.sleep(10)

        self.dr.click(constants.el_type_xpath, el.jlf_login)
        self.dr.send_keys(constants.el_type_xpath, el.jlf_name, '18518915432')
        self.dr.send_keys(constants.el_type_xpath, el.jlf_pass, 'zx404521')
        time.sleep(10)
        gologin = self.dr.get_element(constants.el_type_xpath, el.jlf_go_login)
        location = gologin.location

        # jsre= self.dr.js("window.document.getElementsByClassName('button button-block button-primary ng-binding disable-user-behavior')[0].on-tap()")
        self.dr.switch_to_nat()

        # # element_locator = Element()
        login_button_location = [int(location['x']) * 2 + 10, int(location['y'] * 2 + 45)]
        login_button_location = [351, 418]
        res = self.dr.tap([login_button_location])

        print res
        # self.dr.assert_equal(text, name, '找不到。。。。', True, self.__class__.__name__)
        # self.dr.switch_to_nat()
        # self.dr.click_back()


        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
