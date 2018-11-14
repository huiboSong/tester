# coding=utf-8

import comall
import unittest
from ddt import ddt, data, unpack
from setting.hena_test import setting
from setting.hena_test import data as dt

@ddt
class SquirrelsTest(unittest.TestCase):
    """
        测试三只松鼠登录的请求
    """
    # 获得测试数据
    d = dt.TestData().get("songshu")
    @unpack
    @data(d[0], d[1])
    def test_login_001(self, loginName, password, imageVerifyCode,er_msg):
        """登录"""
        # 拼好接口的url
        squirrels_url = setting.squirrels_url + "user/login"
        # 准备请求的测试数据
        request_data ={"param":"{loginName:'"+loginName+"',password:'"+password+"',imageVerifyCode:'"+imageVerifyCode+"'}"}
        # 实例化接口类
        api = comall.ComallApi(squirrels_url, setting.squirrels_headers)
        # 发请求，把处理后的数据返回给re
        re = api.http_request("post", request_data)
        # 根据请求的信息,判断测试是否成功
        satate = re[0]['stateCode']
        self.assertEqual(0, re[0]['stateCode'], er_msg)
        if satate == 0 :
            print (loginName+"用户登录成功！")
        else :
            print (loginName+"用户登录失败！")

