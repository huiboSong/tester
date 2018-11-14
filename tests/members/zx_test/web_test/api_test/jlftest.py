# coding=utf-8
import re
import comall
from core.commonutils import CommonUtils

__author__ = 'zhangxue'

import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):

        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = 'http://www.carrefour.cn/cart/getMiniCart?t=0.3070578598049768'
        # comallApi实例化
        api = comall.ComallApi(request_uri, '')
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("get")
        # 保存和判断返回的restful json数据的stateCode
        test = re_data[0]

        result = CommonUtils().pitchstr(test,'show\'">','</button>')
        print(result[0])
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
