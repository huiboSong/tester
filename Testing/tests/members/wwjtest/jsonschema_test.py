__author__ = 'Administrator'
# coding=utf-8


import unittest
import config
import comall
from setting.wwjtest import jsonschema_setting


class Test(unittest.TestCase):

    def test(self):
        """国科PC端登录"""
        request_uri = jsonschema_setting.api_uri + "loginCheck"
        request_body_data_json = {'loginName': '13683526129', 'loginPassword': 'test123456', 'rememberMe': 'false'}
        file_dir = config.base_dir + "setting/wwjtest/jsonschema.json"
        api = comall.ComallApi(request_uri, jsonschema_setting.common_headers, json_schema_file=file_dir)
        re_data = api.http_request("post", request_body_data_json)
        print re_data
        json_code = re_data[0]['loginResult']
        if json_code != "True":
            # json_message = re_data[0]['message']
            raise NameError("message:登录失败！")


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    result = unittest.TextTestRunner(verbosity=2).run(suite)