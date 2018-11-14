# coding=utf-8

import comall
import unittest
from setting.wwjtest import setting
from setting.wwjtest.data import TestData as TD


class CreateOrderTest(unittest.TestCase):
    # 参数化数据获得
    d = TD().get("create_order")

    def squirrel_login(self):
        """三只松鼠-登录操作"""
        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "user/login"
        # 请求的数据体
        request_body_data_json = {"param": "{loginName:'"+self.d.get('login_name')+"',password:'"+self.d.get('password')+"'}"}
        # comallApi实例化
        api = comall.ComallApi(request_uri, setting.common_headers)
        # 发送http请求，把处理后的数据返回给re_data
        re_data = api.http_request("post", request_body_data_json)
        # 保存和判断返回的restful json数据的stateCode
        json_code = re_data[0]['stateCode']
        if json_code == 0:
            # 更新headers[dict格式]的值，方便其他请求调用
            setting.common_headers.update(
                {
                    'userid':      str(re_data[0]['data']['id']),
                    'userSession': re_data[0]['data']['userSession']})
        else:
            print "Error, HTTP Headers[dict] key[userid][usersession] value is not updated."
        # 断言判断测试是否通过
        self.assertEqual("0", str(json_code), "Login Request Test Failed! stateCode != 0")

    def test_squirrel_getIndexInfo(self):
        """获取松鼠币商城首页数据操作"""
        request_uri = setting.api_uri + "integral/index/info"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "GetIndexInfo Test Failed! stateCode != 0")

    def test_squirrel_getProductInfo(self):
        """获取松鼠币商城商品详情数据操作"""
        request_uri = setting.api_uri + "integral/product/baseInfo?param={'id':'"+self.d.get('product_id')+"','type':0}"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "GetProductInfo Test Failed! stateCode != 0")

    def squirrel_addCart(self):
        """购物袋加车操作"""
        request_uri = setting.api_uri + "integral/cart/addGoods"
        request_body_data_json = {"param": "[{'goodsId':'"+self.d.get('good_id')+"','number':1}]"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Cart addGoods Test Failed! stateCode != 0")

    def squirrel_getCartInfo(self):
        """获取松鼠币商城购物车信息操作"""
        request_uri = setting.api_uri + "integral/cart/info"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "GetCartInfo Test Failed! stateCode != 0")

    def squirrel_cart_unselect(self):
        self.squirrel_addCart()
        """购物车取消商品操作"""
        request_uri = setting.api_uri + "integral/cart/unselect"
        request_body_data_json = {"param": "{'basketItemId':1}"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Cart unselect Goods Test Failed! stateCode != 0")

    def squirrel_getPoint(self):
        """获取松鼠币信息操作"""
        request_uri = setting.api_uri + "point/amount"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Get squirrel Point Test Failed! stateCode != 0")

    def squirrel_checkout(self):
        """生成结算信息操作"""
        request_uri = setting.api_uri + "integral/checkout/"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        if json_code == 0:
            setting.params.update(
                {
                    'payableAmount':    str(re_data[0]['data']['info']['payableAmount']),
                    'payableIntegral':    str(re_data[0]['data']['info']['payableIntegral']),
                    'cartToken':        str(re_data[0]['data']['cartToken'])})
        else:
            print "Error, goods key [payableAmount][payableIntegral][cartToken] value is not updated."
        self.assertEqual("0", str(json_code), "checkout Test Failed! stateCode != 0")

    def squirrel_scanrule(self):
        """扫描结算规则操作"""
        request_uri = setting.api_uri + "integral/asyncCheckout/scanCheckoutRule"
        request_body_data_json = {"param": "{'consigneeId':595500016,'paymentModeType':2,'deliveryModeId':100100008,'couponIds':[],'pointPaymentStatus':true}"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "scanrule Test Failed! stateCode != 0")

    def squirrel_createOrder(self):
        """创建松鼠币商城订单操作"""
        request_uri = setting.api_uri + "integral/checkout/createOrder"
        request_body_data_json = {"param": "{'consigneeId':595500016,'couponIds':[],'pointPaymentStatus':true,'cartToken':'" + str(setting.params.get('cartToken')) + "','invoice':{'status':0},'paymentModeType':2,'deliveryModeId':100100008,'paymentModeId':2,'payableAmount':'" + str(setting.params.get('payableAmount')) + "','pointPayment':'" + str(setting.params.get('payableIntegral')) + "'}"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        if json_code == 0:
            setting.params.update(
                {
                    'orderId':    str(re_data[0]['data']['orderId'])
                })
        else:
            print "Error, goods key [orderId] value is not updated."
        self.assertEqual("0", str(json_code), "createOrder Test Failed! stateCode != 0")

    def test_squirrel_cancelOrder(self):
        self.squirrel_login()
        self.squirrel_addCart()
        self.squirrel_getCartInfo()
        self.squirrel_getPoint()
        self.squirrel_checkout()
        self.squirrel_scanrule()
        self.squirrel_createOrder()
        """取消松鼠币商城订单操作"""
        request_uri = setting.api_uri + "order/cancel"
        request_body_data_json = {"param": "{'orderId':'" + str(setting.params.get('orderId')) + "','reasonId':1}"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "cancelOrder Test Failed! stateCode != 0")

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CreateOrderTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

