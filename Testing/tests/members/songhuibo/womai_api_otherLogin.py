# coding=utf-8
import unittest
import comall
from setting.songhuibo import setting
from setting.songhuibo import el
from setting.songhuibo.data import TestData as dt
import time

class otherlogin(unittest.TestCase):

    def test_login_post(self):
        #微信联合登录
        request_url = setting.api_uri + "otherlogin"
        request_body_json = {"param":"{'openid':'olgysjghcv3yspcfjdbegi_arbp0','nickname':'GUANGUAN2221111','gender':'男','type':'211','unid':'12222111111'}"}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_json)
        userid = return_data[0]['userid']
        if userid > 0:
            # 更新headers[dict格式]的值，方便其他请求调用
            setting.womaiapi_header.update(
                {
                    'Usersession': str(return_data[0]['usersession']),
                    'Userid': str(return_data[0]['userid'])}
                     )
        else:
            print "Error, HTTP Headers[dict] key[Usersession],key[Userid] value is not updated."

# def test_logoutnew_post(self):
#         #微信联合登录
#         request_url = setting.api_uri + "logoutnew"
#         womai = comall.ComallApi(request_url,setting.womaiapi_header)
#         return_data = womai.http_request("post", request_url)
 #        request_body_json = {"openid":"olgysjghcv3yspcfjdbegi_arbp0","nickname":"GUANGUAN2221111","gender":"男","type":"211","unid":"12222111111"}

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(otherlogin)
    result = unittest.TextTestRunner(verbosity=2).run(suite)