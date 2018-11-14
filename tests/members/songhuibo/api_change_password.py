# coding=utf-8
__author__ = "song"
__project__ = "cofcoweb"
import unittest
import comall
from setting.cofcoweb import setting
from setting.cofcoweb.data.otherlogin import TestData as dt
from ddt import ddt, data, unpack
@ddt
class register(unittest.TestCase):
    O = dt.get("api_mobile")
    @data(O[0])
    def test_findPassword(self, mobile):
        # 找回密码发送验证码
        request_url = setting.api_uri + "html5/findPassword/sendCaptcha"
        request_body_json = {"mobile":mobile}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCaptcha Request Test Failed! msg != 发送成功")
    p = dt.get("api_findPassword")
    @data(p[0])
    @unpack
    def test_verifyCaptcha(self, mobile, authCode):
        # 找回密码发送验证码
        request_url = setting.api_uri + "html5/findPassword/verifyCaptcha"
        request_body_json = {"mobile":mobile,"authCode":authCode}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("验证码正确", str(msg), "findPassword Request Test Failed! msg != 验证码正确")
    d = dt.get("api_change_password")
    @data(d[0])
    @unpack
    def test_updateUserPassword(self, mobile, password, verifyPassword):
        # 找回密码发送验证码
        request_url = setting.api_uri + "html5/findPassword/updateUserPassword"
        request_body_json = {"mobile":mobile,"password":password,"verifyPassword":verifyPassword}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("密码修改成功", str(msg), "updateUserPassword Request Test Failed! msg != 密码修改成功")


if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(register)
        result = unittest.TextTestRunner(verbosity=2).run(suite)