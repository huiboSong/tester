# coding=utf-8
import HTMLTestRunner
import unittest
import time

import comall
from setting.zx_test import setting
from setting.zx_test.data import TestData
from logs.tests.members.zx_test.web_test import ApiLoginTest


class Order_Data(unittest.TestCase):
    d = TestData().get("user_login")
    # 登录公共模块实例化
    login = ApiLoginTest()

    def test_login(self):
        self.login.test_login()

    #获取订单列表
    def test_orderlist(self):
        #请求URI地址
        request_url = setting.api_uri + "order/list"
        #请求数据体
        # request_bady_data_json={"param":"{type:"+"0"+",page:1,pageCount:5}"}
        request_bady_data_json = {"param": '{"type":0,"page":1,"pageCount":5}'}
        api = comall.ComallApi(request_url, setting.common_headers)
        re_data = api.http_request("get", request_bady_data_json)

        json_code = re_data[0]["stateCode"]
        if json_code != 0:
            api.log("error", "Failed, Request URI: %s, Input data: %s, But return data: %s"
                    % (request_url, request_bady_data_json, re_data[1]))

        # 断言判断测试是否通过
        self.assertEqual("0", str(json_code), "GetorderList Request Test Failed!")


# 单独调试所需要的代码
if __name__ == "__main__":
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # 打开一个文件，将result写入此file中
    fp = open("result" + now + ".html", 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(Order_Data)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(suite)
    fp.close()