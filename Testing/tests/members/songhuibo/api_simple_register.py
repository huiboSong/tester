# coding=utf-8
__author__ = "song"
__project__ = "cofcoweb"
import unittest
import comall
from setting.cofcoweb import setting
from setting.cofcoweb.data.apiregister import TestData as dt
from ddt import ddt, data, unpack
@ddt
class register(unittest.TestCase):

    d = dt().get("register_phone")
    @data(d[0])
    def test_fastSignUp(self, mobilePhone):
        # 快速注册简易版-填写手机号发送验证码
        request_url = setting.api_uri + "html5/fastSignUp/sendCode"
        request_body_json = {"mobilePhone":mobilePhone}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCode Request Test Failed! msg != 发送成功")
    @data(d[1])
    @unpack
    def test_fastSignup(self, mobilePhone, authCode):
        # 快速注册简易版-填写手机号发送验证码
        request_url = setting.api_uri + "html5/fastSignUp/finishSignUp"
        request_body_json = {"mobilePhone":mobilePhone,"authCode":authCode}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        message = return_data[0]['sendcouponcard']['message']
        self.assertEqual("欢迎使用手机我买网", str(message), "finishSignUp Request Test Failed! message != 欢迎使用手机我买网")

if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(register)
        result = unittest.TextTestRunner(verbosity=2).run(suite)