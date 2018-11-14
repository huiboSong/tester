# coding=utf-8
import time

import comallmobile
from core import constants
from setting.zx_test import setting
from setting.zx_test import el


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
        contexts= self.dr.get_contexts()

        self.dr.switch_to_web(contexts[1])
        time.sleep(5)

        self.dr.click(constants.el_type_xpath,'/html/body/ion-nav-view/ion-view/ion-tabs/div/a[5]')

        time.sleep(5)

        self.dr.send_keys(constants.el_type_xpath,'/html/body/div[4]/div[2]/ion-modal-view/ion-content/div/form/div[2]/p[1]/span/input','zhangxue')
        # self.dr.click_back()


        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
