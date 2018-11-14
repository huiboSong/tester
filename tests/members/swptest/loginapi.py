# coding=utf-8
__author__ = 'sun'

import unittest
import comall
import time
from setting.swptest import setting


class Mobile_Login_api(unittest.TestCase):
    def test_login(self):
        # 接口的uri
        login_url = setting.api_uri + "loginnew"
        # 接口参数
        login_data_josn = {"username": "comalltest", "password": "comalltest"}
        # 实例化ComallApi这个类
        womai_login_api = comall.ComallApi(login_url, setting.womaiapilogin_header)
        # 调用http_request方法，发送请求，返回请求结果
        return_data = womai_login_api.http_request("post", login_data_josn)
        # 截取返回结果的userid
        userid = return_data[0]['userid']
        print userid
         # 增加断言，对比userid
        self.assertEqual("7618438", str(userid), "Test failed.")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Mobile_Login_api)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
