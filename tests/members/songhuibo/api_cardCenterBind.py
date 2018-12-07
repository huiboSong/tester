# coding=utf-8
__author__ = "song"
__project__ = "cofcoweb"
import time
import unittest

import comall
from ddt import ddt, data, unpack
from setting.cofcoweb import setting
from setting.cofcoweb.data.otherlogin import TestData as dt


@ddt
class card(unittest.TestCase):
    # 生成时间格式timestamp
    def test_a_timestamp(self):

        timestamp = int(time.strftime('%S%H%M',time.localtime(time.time())))*7-1995
        # print timestamp
        if timestamp > 0:
        # 更新params[dict格式]的值方便其他请求调用
            setting.params.update(
                {'timestamp': int(time.strftime('%S%H%M',time.localtime(time.time())))*7-1995}
                 )
        else:
            print("Error, HTTP params[dict] key[timestamp] value is not updated.")
        # print setting.params

    O = dt.get("api_user")
    @data(O[0])
    @unpack
    def test_b_login_post(self, username, password):
        # api登录
        request_url = setting.api_uri + "loginnew"
        request_body_data_json = {"username":username,"password":password}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_data_json)
        usersession = return_data[0]['usersession']
        userid = return_data[0]['userid']
        message = return_data[0]['sendcouponcard']['message']
        #  self.assertEqual("58803862",str(userid),"return_data[0]['userid']")
        if message == "欢迎使用手机我买网":
            # 更新headers[dict格式]的值，方便其他请求调用
            setting.womaiapilogin_header.update(
                {
                    'Usersession': str(return_data[0]['usersession']),
                    'Userid': str(return_data[0]['userid'])}
                     )
        else:
            print("Error, HTTP womaiapilogin_header[dict] key[usersession] value is not updated.")
        # print usersession,userid
    p = dt.get("api_cardCenterBind")
    @data(p[0])
    @unpack
    def test_c_cardCenterBind(self, cardBatchId, activityId, bindway):
        # 卡券中心领券接口
        request_url = setting.api_uri + "html5/cardCenterBind"
        request_body_json = {"timestamp":''+str(setting.params.get("timestamp"))+'',"cardBatchId":cardBatchId,"activityId":activityId,"bindway":bindway}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        msg = return_data[0]['msg']
        self.assertEqual("领取成功，已绑定到领取手机号账号", str(msg), "sendCaptcha Request Test Failed! msg != 领取成功，已绑定到领取手机号账号")
    d = dt.get("api_cardlist")
    @data(d[0])
    def test_d_frontend(self, cardBatchId):
        # 给前端提供的数据接口
        request_url = setting.api_uri + "html5/getCardByCardBatchId/frontend"
        request_body_json = {"cardBatchId":cardBatchId}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        #msg = return_data[0]['msg']
        #self.assertEqual("领取成功，已绑定到领取手机号账号", str(msg), "sendCaptcha Request Test Failed! msg != 领取成功，已绑定到领取手机号账号")

    @data(d[0])
    def test_e_afterend(self, cardBatchId):
        # 给CMS后端提供的数据接口
        request_url = setting.api_uri + "html5/getCardByCardBatchId/afterend"
        request_body_json = {"cardBatchId":cardBatchId}
        womai = comall.ComallApi(request_url,setting.womaiapilogin_header)
        return_data = womai.http_request("post", request_body_json)
        #msg = return_data[0]['msg']
        #self.assertEqual("领取成功，已绑定到领取手机号账号", str(msg), "sendCaptcha Request Test Fa


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(card)
    result = unittest.TextTestRunner(verbosity=2).run(suite)