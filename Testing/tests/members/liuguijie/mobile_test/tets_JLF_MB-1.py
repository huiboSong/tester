# coding=utf-8
__author__ = 'liuguijie'
import time
# from ddt import ddt, data, unpack
# import comallmobile
# from core import constants
# from setting.zx_test import setting
# from setting.zx_test import el
# from setting.zx_test.data import TestData

import unittest
from appium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps={}
        desired_caps['platformName']="Android"
        desired_caps['platformVersion']="5.0.0"
        desired_caps['deviceName']="192.168.56.101:5555"
        desired_caps["noReset"]=True
        # 远程连接appium并发送初始化参数
        self.mydr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def test_001(self):
        time.sleep(15)
        self.mydr.swipe(765,692,3,954,1000)
        time.sleep(15)
        self.mydr.switch_to.context("WEBVIEW")
        time.sleep(2)
        # 点击进入首页
        self.mydr.find_element_by_xpath("/html/body/div[3]/div[2]/ion-modal-view/ion-content/div/div[1]/ion-"
                                        "slide[2]/div[2]/button").click()
        time.sleep(5)
        # 点击全球购物
        self.mydr.find_element_by_xpath("/html/body/ion-nav-view/ion-view/ion-tabs/ion-nav-view[1]/ion-view"
                                        "/ion-content/div[1]/div[3]/ul[1]/li[1]/img").click()
        time.sleep(5)
        # 点击第一个商品  加入购物车 按钮
        self.mydr.find_element_by_xpath("/html/body/ion-nav-view/ion-view/ion-tabs/ion-nav-view[1]/ion-view"
                                        "[2]/ion-content/div[1]/div[2]/ul/li[1]/div[2]/div[3]/button").click()
        time.sleep(5)
        # 点击购物车
        self.mydr.find_element_by_xpath("/html/body/ion-nav-view/ion-view/ion-tabs/ion-nav-view[1]/ion-view"
                                        "[2]/cm-overseas-shop-tabs/div/cm-tab[3]").click()
        time.sleep(5)
        # 点击结算
        self.mydr.find_element_by_xpath("/html/body/ion-nav-view/ion-view/ion-tabs/ion-nav-view[1]/ion-view"
                                        "[3]/ion-footer-bar[1]/div[2]/button").click()
        time.sleep(5)
        #  点击  输入 账户
        self.mydr.find_element_by_xpath("/html/body/div[5]/div[2]/ion-modal-view/ion-content/div[1]/form/div"
                                        "[1]/label[1]/input").click()
        self.mydr.find_element_by_xpath("/html/body/div[5]/div[2]/ion-modal-view/ion-content/div[1]/form/div"
                                        "[1]/label[1]/input").send_keys("13381253931")
        time.sleep(3)
        # 点击 输入 密码
        self.mydr.find_element_by_xpath("/html/body/div[5]/div[2]/ion-modal-view/ion-content/div[1]/form/div"
                                        "[1]/label[2]/input").click()
        self.mydr.find_element_by_xpath("/html/body/div[5]/div[2]/ion-modal-view/ion-content/div[1]/form/div"
                                        "[1]/label[2]/input").send_keys("123456")
        # 点击登录
        self.mydr.find_element_by_xpath("/html/body/div[5]/div[2]/ion-modal-view/ion-content/div[1]/form/div"
                                        "[2]").click()
        time.sleep(5)
        # 断言 登录成功，进入购物车（shopping_cart）页面  抓取顶端“购物车”三个字判断
        shopping_cart = self.mydr.find_element_by_xpath("/html/body/ion-nav-view/ion-view/ion-tabs/ion-nav-view"
                                                        "[1]/ion-view[3]/ion-header-bar[1]/h1").text
        print shopping_cart
        self.assertEqual(u"购物车",shopping_cart,u"登录失败")




#     def tearDown(self):
#         pass
#
#
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
#     result = unittest.TextTestRunner(verbosity=2).run(suite)

