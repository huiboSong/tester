# coding=utf-8
import comall
from setting.zx_test import setting

__author__ = 'zhangxue'

class CommonLogin():

    def login(self):
        #登录请求地址拼写
        request_url = setting.api_uri + "/user/login"
        # 请求的数据体
        request_body_data_json = {"param": "{loginName:'15874671697',password:'123456'}"}
        # comallApi实例化(创建对象)
        api = comall.ComallApi(request_url, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']

        if json_code == 0:
            # 更新headers[dict格式]的值，方便其他请求调用
            print "login T"
            setting.common_headers.update(
               {
                    'userid':      str(re_data[0]['data']['id']),
                    'usersession': re_data[0]['data']['userSession']})
        else:
            print "Error, HTTP Headers[dict] key[user_id][user_session] value is not updated."











