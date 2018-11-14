# coding=utf-8
import HTMLTestRunner
import time

from ddt import ddt

import comall
from setting.zx_test import setting
from logs.tests.members.zx_test.web_test import CommonLogin


__author__ = 'zhangxue'

import unittest


@ddt
class MyTestCase(unittest.TestCase):
    apilogin = CommonLogin()

    def test_a_login(self):
        self.apilogin.login()

    # 添加购物车商品

    def test_b_addGoods(self, goodId, num):
        req_url = setting.api_uri + "cart/addGoods"
        api = comall.ComallApi(req_url, setting.common_headers)
        req_json = {"param": "[{'goodsId:'" + '2400890' + "',' 'flashSaleId':'', 'number':" + num + "'}]"}
        re_data = api.http_request("post", req_json)
        code = re_data[0]['stateCode']
        if code != 0:
            msg = re_data[0]['message']
            self.fail(msg)

    #点击去结算
    def test_c_addOrder(self):
        req_url = setting.api_uri + "checkout/info"
        api = comall.ComallApi(req_url, setting.common_headers)
        req_json = {"param": ""}
        re_data = api.http_request("post", req_json)
        code = re_data[0]['stateCode']
        if code == 0:
            setting.params.update({

                'deliveryModeId': str(re_data[0]['data']['deliveryModes'][0]['id']),
                'paymentModeType': str(re_data[0]['data']['payModeTypes'][0]['paymentModeType'])

            })
        else:
            msg = re_data[0]['message']


    # 获取收货地址
    def test_d_getaddlist(self):
        req_url= setting.api_uri+"consignee/list"
        api=comall.ComallApi(req_url, setting.common_headers)
        re_data=api.http_request(req_url,"")
        code=re_data[0]['stateCode']
        if code==0:
            setting.params.update({
               'consigneeId':    str(re_data[0]['data']['validAddress'][0]['id'])
            })
        else:
            msg=re_data[0]['message']
            self.assertEqual(1, 2,"不相等")

    #选择配送方式
    def test_driving(self):
        req_url= setting.api_uri+"checkout/getDeliverys"
        api=comall.ComallApi(req_url, setting.common_headers)

        req_json = {"param": "{consigneeId:'" + str(setting.params.get('consigneeId')) + "',paymentModeType:'" + str(
            setting.params.get('paymentModeType')) + "'}"}
        re_data=api.http_request("post",req_json)
        code=re_data[0]['stateCode']
        if code==0:
            # 选择准时达要用到的参数值
            setting.params.update(
                {
                    'deliveryModeId':       str(re_data[0]['data']['deliveryModes'][0]['id'])
                })
        else:
            msg=re_data[0]['message']
            raise NameError("message:"+msg)






if __name__ == "__main__":
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # 打开一个文件，将result写入此file中
    fp = open("result" + now + ".html", 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(suite)
    fp.close()