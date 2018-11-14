# coding=utf-8
import unittest
import comall
from setting.songhuibo import setting
from setting.songhuibo import el
from setting.songhuibo.data import TestData as dt
import time

class register(unittest.TestCase):
        # 验证手机号发送验证码
    def test_sendCode(self):
        request_url = setting.api_uri + "html5/fastRegistration/sendCode"
        request_body_json = {"registerMobile":"13520843514"}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCode Request Test Failed! msg != 发送成功")


    def test_fastRegistration(self):
        # 校验验证码
        request_url = setting.api_uri + "html5/fastRegistration/verifyCode"
        request_body_json = {"registerMobile":"13520843514","authCode":"913627"}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("验证码正确", str(msg), "fastRegistration Request Test Failed! msg != 验证码正确")


    def test_finishRegister(self):
        # 输入密码完成注册
        request_url = setting.api_uri + "html5/fastRegistration/finishRegister"
        request_body_json = {"registerMobile":"13520843514","password":"123456qq","verifyPassword":"123456qq"}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        message = return_data[0]['sendcouponcard']['message']
        self.assertEqual("欢迎使用手机我买网", str(message), "finishRegister Request Test Failed! message != 欢迎使用手机我买网")

    def test_html5sendCode(self):
        # h5输入密码完成注册
        request_url = setting.api_uri + "html5/fastRegistration/fastFinishRegister"
        request_body_json = {"registerMobile":"13520843514","authCode":"605489","password":"123456qq"}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        message = return_data[0]['sendcouponcard']['message']
        self.assertEqual("欢迎使用手机我买网", str(message), "fastRegistration Request Test Failed! message != 欢迎使用手机我买网")


    def test_fastSignUp(self):
        # 快速注册简易版-填写手机号发送验证码
        request_url = setting.api_uri + "html5/fastSignUp/sendCode"
        request_body_json = {"mobilePhone":"13520843514"}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCode Request Test Failed! msg != 发送成功")

    def test_fastSignup(self):
        # 快速注册简易版-填写手机号发送验证码
        request_url = setting.api_uri + "html5/fastSignUp/finishSignUp"
        request_body_json = {"mobilePhone":"13520843514","authCode":"342586"}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        message = return_data[0]['sendcouponcard']['message']
        self.assertEqual("欢迎使用手机我买网", str(message), "finishSignUp Request Test Failed! message != 欢迎使用手机我买网")

    def test_fastLogin(self):
        # 免密登录获取验证码
        request_url = setting.api_uri + "html5/fastLogin/sendCode"
        request_body_json = {"mobile":"13520843514"}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCode Request Test Failed! msg != 发送成功")

    def test_captchaLogin(self):
        # 免密登录手机号+验证码登录
        request_url = setting.api_uri + "html5/fastLogin/captchaLogin"
        request_body_json = {"mobile":"13520843514","authCode":"684259"}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_json)
        message = return_data[0]['sendcouponcard']['message']
        self.assertEqual("欢迎使用手机我买网", str(message), "fastLogin Request Test Failed! message != 欢迎使用手机我买网")

    def test_findPassword(self):
        # 找回密码发送验证码
        request_url = setting.api_uri + "html5/findPassword/sendCaptcha"
        request_body_json = {"mobile":"13520843514"}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("发送成功", str(msg), "sendCaptcha Request Test Failed! msg != 发送成功")

    def test_verifyCaptcha(self):
        # 找回密码发送验证码
        request_url = setting.api_uri + "html5/findPassword/verifyCaptcha"
        request_body_json = {"mobile":"13520843514","authCode":"713894"}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("验证码正确", str(msg), "findPassword Request Test Failed! msg != 验证码正确")

    def test_updateUserPassword(self):
        # 找回密码发送验证码
        request_url = setting.api_uri + "html5/findPassword/updateUserPassword"
        request_body_json = {"mobile":"13520843514","password":"123456wq","verifyPassword":"123456wq"}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("密码修改成功", str(msg), "updateUserPassword Request Test Failed! msg != 密码修改成功")

    if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(register)
        result = unittest.TextTestRunner(verbosity=2).run(suite)