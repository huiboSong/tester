# coding=utf-8

import comall
import unittest
from ddt import ddt, data, unpack
from setting.liuguijie.API import setting
from setting.liuguijie.API import data as dt


@ddt
class FTTest(unittest.TestCase):
    """
        测试福田APP登录状态的加车请求
    """
    # 获得测试数据
    my_data= dt.TestData().get("jie_study")

    @data(my_data[0])
    @unpack
    def test_001(self,goods_id, number, ex_info, msg):
        """加车"""
        # 拼好接口的url
        url = setting.FT_url + "api/cart/addGoods"
        # 准备请求的测试数据
        request_data = {'param': '[{"goodsId":290006261,"number":1,"type":1}]'}
        # 实例化接口类
        api = comall.ComallApi(url, setting.my_header)
        # 发请求,并保存返回的信息
        re = api.http_request("post", request_data)
        # 根据请求的信息,判断测试是否成功
        print re[1]
        self.assertEqual(0, re[0]['stateCode'], msg)

