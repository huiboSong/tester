# coding=utf-8

__author__ = 'qiguojie'

import comall
import unittest
from ddt import ddt, unpack, data
from setting.qiguojie import data as d
from setting.qiguojie import el
from setting.qiguojie import setting


@ddt
class QiguojieTest(unittest.TestCase):
    """测试是我给大家培训的时候做的测试"""

    # 获得测试数据
    my_data = d.TestData().get("qi_study")

    # 初始化方法，打开浏览器
    def setUp(self):
        # 打开一个浏览器，使用的是setting里面设置的
        self.dr = comall.Comall(setting.driver_type)
        # 最大化浏览器
        self.dr.max_window()

    @data(my_data[0], my_data[1], my_data[2], my_data[3],
          my_data[4], my_data[5], my_data[6], my_data[7],
          my_data[8], my_data[9])
    @unpack
    def test_001(self, search, equal, error_message):
        """在某网站，查找著名画家的测试"""
        # 获得driver浏览器对象
        dr = self.dr
        # 打开一个网址，是setting里面设置的url
        self.dr.open(setting.baidu_url)
        # 在输入框里输入一个值
        dr.send_keys(el.baidu_el_type, el.keyword_input, search)
        # 点击一个什么按钮
        dr.click(el.baidu_el_type, el.search_button)
        # 获得一个结果页面的一个文本内容
        huajia = dr.get_text(el.baidu_text_type, el.first_title_em)
        # 判断是否获得文本和我们期望的一样，测试是否成功或失败
        self.assertEqual(equal, huajia, error_message)

    def tearDown(self):
        dr = self.dr
        # 关闭浏览器
        dr.close()



