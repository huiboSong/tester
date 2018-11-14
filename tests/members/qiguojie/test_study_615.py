# coding=utf-8

import comall
import unittest
from ddt import ddt, data, unpack
from setting.qiguojie import setting
from setting.qiguojie import data as dt


@ddt
class SanyanTest(unittest.TestCase):
    """
        测试中免三亚的无登录状态的加车请求
    """
    # 获得测试数据
    d = dt.TestData().get("sanya")

    @data(d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9])
    @unpack
    def test_001(self, pid, number, ex_info, msg):
        """加车"""
        # 拼好接口的url
        url = setting.sanya_url + "addcart"
        # 准备请求的测试数据
        request_data = {"pid": pid, "amount": number}
        # 实例化接口类
        api = comall.ComallApi(url, setting.my_header)
        # 发请求,并保存返回的信息
        re = api.http_request("get", request_data)
        # 根据请求的信息,判断测试是否成功
        self.assertEqual(ex_info, re[0]['response'], msg)
