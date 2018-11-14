# coding=utf-8

__author__ = 'qianxueping'

import unittest
import comall
from ddt import ddt, data, unpack
from setting.qianxueping import setting
from setting.qianxueping import data as dt

@ddt
class LoginTest(unittest.TestCase):
    u"""测试三亚登录接口"""

    # 获得测试数据信息
    login = dt.TestData().get("login")
    # print login

    @data(login[0], login[1], login[2])
    @unpack
    def test_loginTest(self, mobile, password, res_msg, msg):
        # 拼接登录URL
        sy_url = setting.url + "user/login"
        # 请求数据
        login_date = {'account':  mobile, "password": password}
        #给请求数据转为字符串
        #login_date = {'account': "\"" + mobile + "\"", "password": "\"" + password + "\""}
        #login_date = {"account": '18301472978', "password": 'snow1234'}
        # 实例化
        api = comall.ComallApi(sy_url, setting.sy_header)
        # 发送请求并保存请求数据
        res_data = api.http_request("post", login_date)

        #断言，判断请求是否成功
        self.assertEqual(res_msg, res_data[0]['response'], msg)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
