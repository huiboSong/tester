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
        # 验证手机号发送验证码
    def test_sendCode(self, registerMobile):
        request_url = setting.api_uri + "html5/fastRegistration/sendCode"
        request_body_json = {"registerMobile":registerMobile}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCode Request Test Failed! msg != 发送成功")

    @data(d[3])
    @unpack
    def test_html5sendCode(self, registerMobile, authCode, password):
        # h5输入密码完成注册
        request_url = setting.api_uri + "html5/fastRegistration/fastFinishRegister"
        request_body_json = {"registerMobile":registerMobile,"authCode":authCode,"password":password}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        message = return_data[0]['sendcouponcard']['message']
        self.assertEqual("欢迎使用手机我买网", str(message), "fastRegistration Request Test Failed! message != 欢迎使用手机我买网")




if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(register)
        result = unittest.TextTestRunner(verbosity=2).run(suite)