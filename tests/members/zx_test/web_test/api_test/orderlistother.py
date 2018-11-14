#coding=utf-8
import comall
from setting.zx_test import setting
from logs.tests.members.zx_test.web_test import CommonLogin

__author__ = 'zhangxue'

import unittest


class OrderListOther(unittest.TestCase):

    login_api=CommonLogin()
    def test_login(self):
        self.login_api.login()

    def test_orderlist(self):
        request_url= setting.api_uri+"order/list"
        api=comall.ComallApi(request_url, setting.common_headers)
        request_json={"param":'{"type":0,"page":1,"pageCount":5}'}
        re_data=api.http_request("get",request_json)
        print re_data[0]
        jsonCode=re_data[0]['stateCode']
        if jsonCode!=0:
            api.log("error","request url: %s request json %s but requset %s" %(request_url,request_json,re_data[1]))



        self.assertEqual("0",str(0),"requset not getOrderlist")







if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OrderListOther)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
