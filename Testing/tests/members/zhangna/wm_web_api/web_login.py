# coding=utf-8
__author__ = 'Administrator'

import requests
import unittest
from setting.zhangna import setting
from ddt import ddt, data, unpack
from setting.zhangna.data import TestData as dt


@ddt
class wm_test(unittest.TestCase):

    d = dt().get('web_login')
    @data(d[0])
    @unpack
    def test_a_login(self, username, pwd, validateCode):
        # 请求的uri拼写
        uri = setting.web_url + 'login/login.do'
        # 请求的数据体
        body = {'serverPath': 'http://ftest.womaiapp.com', 'loginId': username, 'password': pwd, 'validateCode': validateCode, 'tempcode': '', 'mid': '0', 'returnUrl': 'http://ftest.womaiapp.com/index-31000-0.htm'}
        headers = {}
        # 发送请求
        http_request = requests.post(url=uri, headers=headers, data=body, verify=False)
        print(http_request.text[78:110])
        print(http_request.text)
        s = http_request.text[78:110]
        setting.uuid.append(s)