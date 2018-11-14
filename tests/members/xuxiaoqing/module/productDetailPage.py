# coding=utf-8

import comall
import unittest
from setting.xuxiaoqing import setting
from setting.xuxiaoqing import data
from setting.xuxiaoqing import el
import time


class WomaiProductInfoTest(unittest.TestCase):
   qq = data.id
   #http://10.6.24.235:8080/wmapi/html5/productnew?productid=566238
   def testproductDetailPage(self):
       request_uri = setting.api_uri + "html5/productnew"  #http://10.6.24.235:8080/wmapi/html5/productnew
       request_body_data_json = {"productid": self.qq}       #productid:566238
       womai = comall.ComallApi(request_uri,setting.womaiapi_header)   #http://10.6.24.235:8080/wmapi/html5/productnew,header
       return_data = womai.http_request("get",request_body_data_json)
       product_type = return_data[0]['product']['product_type']
       self.assertEqual("1", product_type, "Test success.")




# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WomaiProductInfoTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)