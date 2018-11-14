# coding=utf-8

import comall
import unittest

class SanyanTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        my_heard = {
            "Host": "wap.365autogo.com",
            "language": "zh-CN",
            "osVersion": "6",
            "userId": "1000011035",
            "unique": "android-a085276fccf629a0",
            "userSession": "4FA0052DA0A87FDAE6EE6AD079F1E986",
            "channel": "production",
            "os": "android",
            "appkey": "ef1fc57c13007e33",
            "appVersion": "1.5.1",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-cn"

        }
        url = "http://wap.365autogo.com/mobile/api/cart/addGoods"
        request_data = {'param': '[{"goodsId":290006261,"number":1,"type":1}]'}
        api = comall.ComallApi(url,my_heard)
        re =api.http_request("post",request_data)
        print re[1]
        self.assertEqual(0, re[0]['stateCode'], u"失败")



