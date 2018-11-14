# coding=utf-8

import comall
import unittest
from ddt import ddt, data, unpack
from setting.qtest import setting
from setting.qtest.data import TestData as dt


@ddt
class LoginDDTTest(unittest.TestCase):
    # 取得要数据驱动测试的数据
    d = dt().get("interface_carrefour_login")

    @classmethod
    def setUpClass(cls):
        request_uri = setting.api_uri + "user/login"

    @unpack
    @data(d[0], d[1])
    def test_carrefour_inner_login(self, login_phone_number, login_pw, user_id, login_error_msg):
        u"""家乐福内网-登录请求和测试验证；保存user_id和user_session到dict中"""
        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "user/login"
        # 请求的数据体
        request_body_data_json = {"param": "{loginName:'" + login_phone_number + "',password:'" + login_pw + "'}"}
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']

        if json_code != 0:
            api.log("error", "Failed, Request URI: %s, Input data: %s, But return data: %s"
                    % (request_uri, request_body_data_json, re_data[1]))

        # 断言判断测试是否通过
        self.assertEqual("0", str(json_code), login_error_msg)
        self.assertEqual(user_id, str(re_data[0]['data']['id']))

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(LoginDDTTest)
    # suite = unittest.TestLoader().loadTestsFromTestCase(LoginDDTTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite1)