# coding=utf-8
import comall
import unittest
import time

from ddt import ddt, unpack, data
from setting.cww_test import data as d
from setting.cww_test import el
from setting.cww_test import setting


@ddt
# 类的实例化
class CwwTest(unittest.TestCase):
    # 获得测试数据
    my_data = d.TestData().get("test_001")
    # 初始化方法 打开浏览器
    def setUp(self):
        # 打开一个浏览器 setting里设置的Driver_type
        self.dr = comall.Comall(setting.driver_type)
        self.dr.open(setting.baidu_url)
        # 浏览器最大化
        self.dr.max_window()
        time.sleep(5)

    # 取出数据第一组、第二组...
    @data(my_data[0],  my_data[1])
    # @data(my_data[0],  my_data[1],  my_data[2],  my_data[3])
    # 解包
    @unpack
    def test_01(self, search, equal, error_message):
        # 获得
        ww = self.dr
        time.sleep(5)
        ww.send_keys("xpath", el.send_text, search)
        time.sleep(5)
        ww.click("xpath", el.search_btn)
        ww.win_key("xpath", "//*[@id='su']", "ENTER")
        name = ww.get_text("xpath", el.first_name)
        self.assertEqual(equal, name, error_message)

    def tearDown(self):
        self.dr.close()
        pass



