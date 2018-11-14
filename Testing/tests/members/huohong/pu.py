# coding=utf-8

import unittest
import comall
import time
from setting.huohong import el
from setting.huohong import setting
from setting.huohong.data import TestData
from ddt import ddt, data, unpack

class WebProductInfoTest(unittest.TestCase):

    def test_product_info_web(self):

            # 启动浏览器
            self.dr = comall.Comall("chrome")
            self.dr.open(setting.womai_producturl)