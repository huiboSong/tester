# coding=utf-8
# gongdan #

import unittest

import comall
from setting.message import setting
import urllib


class MineSetting(unittest.TestCase):
    #d = TD().get("api_user_sendSMSVerifyCode")


   # 登录
    def test_login(self):
        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "session"
        # 请求的数据体
       # request_body_data_json = {"pa/ram": "{loginName:'13810218235',password:'111qqq'}"}
        request_body_data_json = {"loginName":"13810218235","password":"111qqq"}
        #request_body_data_jsonurl=urllib.urlencode(request_body_data_json)
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['loginName']
        # 断言判断测试是否通过
        self.assertEqual("13810218235", str(json_code), "Login Request Test Failed! stateCode != 0")

        if json_code == 201:
            # 更新headers[dict格式]的值，方便其他请求调用
            setting.common_headers.update(
                {
                    'id':      str(re_data[0]['data']['id']),
                    'userSession': re_data[0]['data']['userSession']})
        else:
            print "Error, HTTP Headers[dict] key[user_id][user_session] value is not updated."



# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MineSetting)
    result = unittest.TextTestRunner(verbosity=2).run(suite)