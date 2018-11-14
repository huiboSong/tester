# coding=utf-8
__author__ = "song"
__project__ = "cofcoweb"
import unittest
import comall
from setting.cofcoweb import setting
from setting.cofcoweb.data.apiregister import TestData
from ddt import ddt, data, unpack
@ddt
class register(unittest.TestCase):
    d = TestData().get("register_phone")
    @data(d[0])
    # 验证手机号发送验证码
    def test_a_sendCode(self, mobile):
        request_url = setting.api_uri + "html5/fastRegistration/sendCode"
        request_body_json = {"registerMobile":mobile}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCode Request Test Failed! msg != 发送成功")
    @data(d[1])
    @unpack
    def test_b_fastRegistration(self, mobilephone, authCode):
        # 校验验证码
        request_url = setting.api_uri + "html5/fastRegistration/verifyCode"
        request_body_json = {"registerMobile":mobilephone ,"authCode":authCode}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("验证码正确", str(msg), "fastRegistration Request Test Failed! msg != 验证码正确")
    @data(d[2])
    @unpack
    def test_c_finishRegister(self, phone ,password, verifyPassword):
        # 输入密码完成注册
        request_url = setting.api_uri + "html5/fastRegistration/finishRegister"
        request_body_json = {"registerMobile":phone,"password":password,"verifyPassword":verifyPassword}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        message = return_data[0]['sendcouponcard']['message']
        self.assertEqual("欢迎使用手机我买网", str(message), "finishRegister Request Test Failed! message != 欢迎使用手机我买网")

if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(register)
        result = unittest.TextTestRunner(verbosity=2).run(suite)