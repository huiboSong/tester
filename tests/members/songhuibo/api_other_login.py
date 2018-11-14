# coding=utf-8
__author__ = "song"
__project__ = "cofcoweb"
import unittest
import testgo
from setting.cofcoweb import setting
from setting.cofcoweb.data import TestData
from ddt import ddt, data, unpack

@ddt
class otherlogin(unittest.TestCase):
    O = TestData.get("api_other_login_type")
    @data(O[0])
    @unpack
    def test_a_weixin_login(self, openid, nickname, gender, type, unid):
        request_url = setting.api_uri + "otherLogin"
        request_body_json = {"openid":openid,"nickname":nickname,"gender":gender,"type":type,"unid":unid}
        womai = testgo.hooliApi(request_url, setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        userid = return_data[0]['userid']
        self.assertEqual("59004406", str(userid), "sendCode Request Test Failed! userid !=57600872")


    # def test_b_logoutnew_post(self):
    #     #微信联合登录
    #     request_url = setting.api_uri + "logoutnew"
    #     womai = hooli.hooliApi(request_url,setting.womaiapilogin_header)
    #     return_data = womai.http_request("post", request_url)
    #     msg = return_data[0]['response']
    #     self.assertEqual("logout", str(msg), "sendCode Request Test Failed! userid !=logout")



if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(otherlogin)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
