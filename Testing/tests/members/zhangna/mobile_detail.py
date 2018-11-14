# coding=utf-8

import comall
import unittest
from setting.zhangna import setting
from setting.zhangna import data
from setting.zhangna import el


class Mobilepage(unittest.TestCase):

    my_id = data.TestData().get("product_detail")

    def test_(self):
        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "html5/productnew"
        print request_uri
        # 请求的数据体
        request_body_data_json = {"productid": "956691"}
        # comallApi实例化
        womai = comall.ComallApi(request_uri, setting.womaiapi_header)
        # 发送http请求，把处理后的数据返回给re_data
        return_data = womai.http_request("get", request_body_data_json)
        # 返回的数据存到product_type
        product_type = return_data[0]['product']['product_type']

        self.assertEqual("1", product_type, "Test failed.")


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Mobilepage)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
