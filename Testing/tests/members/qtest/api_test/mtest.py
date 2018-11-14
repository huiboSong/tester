# coding=utf-8

import comall
import unittest
from setting.qtest import setting


class GoodsAddCartTest(unittest.TestCase):

    def test_carrefour_inner_login(self):
        u"""家乐福内网-登录请求和测试验证；保存user_id和user_session到dict中"""
        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "user/login"
        # 请求的数据体
        request_body_data_json = {"param": "{loginName:'18500302553',password:'techqa'}"}
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']
        # 断言判断测试是否通过
        self.assertEqual("0", str(json_code), "Login Request Test Failed! stateCode != 0")
        self.assertEqual("250043162", str(re_data[0]['data']['id']))

        if json_code == 0:
            # 更新headers[dict格式]的值，方便其他请求调用
            setting.common_headers.update(
                {
                    'user_id':      re_data[0]['data']['id'],
                    'user_session': re_data[0]['data']['userSession']})
        else:
            print "Error, HTTP Headers[dict] key[user_id][user_session] value is not updated."

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(GoodsAddCartTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

