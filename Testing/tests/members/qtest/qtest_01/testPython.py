# coding=utf-8

__author__ = 'qiguojie'

import unittest
import time
from ddt import ddt, data, unpack
# 引入主框架文件
import comall
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.qtest import el
from setting.qtest import setting
from setting.qtest.data import TestData as dt
from logs.tests import common


@ddt
class TestCase(unittest.TestCase):
    d = dt().get("gongdan")

    @classmethod
    def setUpClass(cls):
        cls.dr = comall.Comall(setting.driver_type)
        cls.dr.max_window()
        time.sleep(1)
        common.login_success(cls.dr)


    @data(d[0], d[1], d[2])
    @unpack
    def test_Q(self, search_value, get_res_value, failed_msg):

        # 定义浏览器变量
        dr = self.dr

        # 打开一个url
        dr.open(setting.login_baidu_url)

        # 输入一个关键字
        dr.send_keys("xpath", el.baidu_editor, search_value)

        # 点击搜索按钮
        dr.click("xpath", el.baidu_search_btn)

        # 等待2秒
        time.sleep(2)

        # 验证搜索结果正确
        search_name = dr.get_text("xpath", el.search_result_first_record)
        self.assertEqual(get_res_value, search_name, failed_msg)

    @classmethod
    def tearDownClass(cls):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = cls.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)