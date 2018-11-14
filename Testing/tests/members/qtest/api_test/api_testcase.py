# coding=utf-8

import unittest

import comall
from setting.qtest import setting
from setting.qtest.data import TestData as TD


class GoodsAddCartTest(unittest.TestCase):
    # 参数化数据获得
    login_data = TD().get("interface_carrefour_login")

    def carrefour_inner_login(self):
        u"""家乐福内网-登录请求和测试验证；保存user_id和user_session到dict中"""
        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "user/login"
        # 请求的数据体
        request_body_data_json = {"param": "{loginName:'18500302553',password:'techqa'}"}
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']
        # 断言判断测试是否通过
        self.assertEqual("0", str(json_code), "Login Request Test Failed! stateCode != 0")
        self.assertEqual("250043162", str(re_data[0]['data']['id']))

        if json_code == 0:
            # 更新headers[dict格式]的值，方便其他请求调用
            setting.common_headers.update(
                {
                    'user_id':      str(re_data[0]['data']['id']),
                    'user_session': re_data[0]['data']['userSession']})
        else:
            print "Error, HTTP Headers[dict] key[user_id][user_session] value is not updated."

    def carrefour_product_search(self):
        """查询商品,并保存货品ID"""
        request_uri = setting.api_uri + "product/search"
        request_body_data_json = {"param": "{'keyword':'牛奶','order':1,'page':1,'pageCount':12}"}
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']
        # 断言判断测试是否通过
        self.assertEqual("0", str(json_code), "Product Search Request Test Failed! stateCode != 0")

        if json_code == 0:
            # goods[dict格式]的值，方便其他请求调用
            print(re_data[0]['data']['items'][2]['defaultGoodsId'])
            setting.params.update({
                    'good_id':      re_data[0]['data']['items'][2]['defaultGoodsId']})
        else:
            print "Error, goods key [good_id] value is not updated."

    def test_carrefour_add_cart(self):
        # 调用登录和搜索商品,从而获得货品ID
        self.carrefour_inner_login()
        self.carrefour_product_search()
        """物品加车操作"""
        request_uri = setting.api_uri + "cart/addGoods"
        request_body_data_json = {"param": "[{'goodsId':" + str(setting.params.get('good_id')) + ",'number':1}]"}
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        api.log("info", "Request uri: %s, Method: Post, Request Data: %s"
                % (request_uri, request_body_data_json))
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)

        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']
        # 断言判断测试是否通过
        self.assertEqual("0", str(json_code), "Cart addGoods Test Failed! stateCode != 0")



# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(GoodsAddCartTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)