# coding=utf-8
# heyanping #

import unittest

import comall
from setting.zx_test import setting


class Index_Data(unittest.TestCase):


    #获取首页数据
    def test_index_data(self):

        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "index/info"
        # 请求的数据体
        request_body_data_json = {"param": '[{"type":"mobile"}]'}
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("get", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']

        if json_code != 0:
            json_message = re_data[0]['message']
            raise NameError("message:'"+json_message+"'")
        if json_code == 0:
            json_data = re_data[0]['data']
            print json_data;
            print re_data;



# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Index_Data)
    result = unittest.TextTestRunner(verbosity=2).run(suite)


