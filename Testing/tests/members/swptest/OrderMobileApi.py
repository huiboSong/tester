# coding=utf-8
__author__ = 'sun'

import unittest
import comall
from setting.swptest import setting


class MobileLoginApi(unittest.TestCase):
    def test_login(self):
        # 接口的uri
        login_url = setting.api_uri + "loginnew"
        # 接口参数
        login_data_josn = {"username": "comalltest", "password": "comalltest"}
        # 实例化ComallApi这个类
        womai_login_api = comall.ComallApi(login_url, setting.womaiapilogin_header)
        # 调用http_request方法，发送请求，返回请求结果
        return_data = womai_login_api.http_request("post", login_data_josn)
        # 截取返回结果的userid
        userid = return_data[0]['userid']
        usersession = return_data[0]['usersession']
         # 增加断言，对比userid
        self.assertEqual("7618438", str(userid), "test_login failed.")
        #此处判断需要优化
        if userid == 7618438:
            setting.womaiapilogin_header.update({
                'userid': str(userid),
                'usersession': usersession}
            )
        return setting.womaiapilogin_header
    def test_loadcart(self):
        self.test_login()
        # 接口的uri
        loadcart_url = setting.api_uri + "html5/cart/loadCart"
        # 接口参数
        loadcart_data_josn = {"data": '[{"productId":"504492","amount": "2","productType": "0","ruleId":""}]'}
        # 实例化ComallApi这个类
        womai_loadcart_api = comall.ComallApi(loadcart_url, setting.womaiapilogin_header)
        # 调用http_request方法，发送请求，返回请求结果
        return_data = womai_loadcart_api.http_request("post", loadcart_data_josn)
        # 截取返回结果的userid
        productid = return_data[0]['shoppingCarts'][0]['cartsInfo'][0]['cartProducts'][0]['productId']
        cartid = return_data[0]['shoppingCarts'][0]['cartsInfo'][0]['cartId']
        self.assertEqual("504492", productid, "Mobile AddToCard failed.")
        return cartid
        # 增加断言，对比productid
    def test_addresslist(self):
        self.test_login()
        # 接口的uri
        addresslist_url = setting.api_uri + "html5/addresslistnew/listnew"
        # 接口参数
        addresslist_data_josn = {"data": '{"cartId":'+'"'+self.test_loadcart()+'"'+'}'}
        # 实例化ComallApi这个类
        womai_addresslist_api = comall.ComallApi(addresslist_url, setting.womaiapilogin_header)
        # 调用http_request方法，发送请求，返回请求结果
        return_data = womai_addresslist_api.http_request("post", addresslist_data_josn)
        addressid = return_data[0]['valid_address_list'][0]['address']
        return addressid
    def test_checkout(self):
        self.test_login()
        # 接口的uri
        checkout_url = setting.api_uri + "html5/newCheckOut"
        # 接口参数
        checkout_data_josn = {"data": '{"addressId": '+self.test_addresslist()+',"deliveryMethod":{"deliveryId":"","deliveryDate":"","segmentTime":""},"cartMsgs":[{"cartId":'+'"'+self.test_loadcart()+'"'+',"chooseCoupon":[""]}],"payWay":{"wmPayAmount":"0.0","otherPayId":""},"isFirst":"1","fromRecharge":"0","foodyPassword":"555555","orderLeaverMsg":"ABCD","invoice":{"isNeedInvocie":"1","invoiceType":"1","invoiceTitle":"1","companyName":"EFG","invoiceContent":"1","receiverPhone":"1213123","receiverEmail":"asdfsaf@111.com"}}'}
        # 实例化ComallApi这个类
        womai_checkout_api = comall.ComallApi(checkout_url, setting.womaiapilogin_header)
        # 调用http_request方法，发送请求，返回请求结果
        return_data = womai_checkout_api.http_request("post", checkout_data_josn)
        checkout_address = return_data[0]['consigneeInfo']['consigneeId']
        self.assertEqual(self.test_addresslist(), checkout_address, "收获地址获取错误哦")
        # 截取返回结果的userid
    def test_submitorder(self):
        self.test_login()
        # 接口的uri
        submitorder_url = setting.api_uri + "html5/submitorder/submitordermobile"
        # 接口参数
        submitorder_data_josn = {"data": '{"addressId":'+self.test_addresslist()+',"isNeedInvoice":"1","invoiceTitle":"1","invoiceType":"1","invoiceContent":"1", "receiverPhone":"13393112621","companyName":"haha","receiverEmail":"15465@163.com","payPassword": "","isShowPrice":"1","payway":{"wmPayAmount":"0.0","otherPayId":"200" },"cpsData":"","userName":"hehe",  "userIdentify":"","identifyPicPath":[],"deliveryMethod":{"deliveryId":"1","deliveryDateId":"","segmentTime":"1"},"cartMsgs":[{"cartId":'+'"'+self.test_loadcart()+'"'+',"chooseCoupon":[]}], "orderLeaverMsg":"LEAVER","foodyPassword":"SFDX"}'}
        # 实例化ComallApi这个类
        womai_submitorder_api = comall.ComallApi(submitorder_url, setting.womaiapilogin_header)
        # 调用http_request方法，发送请求，返回请求结果
        return_data = womai_submitorder_api.http_request("post", submitorder_data_josn)
        # 截取返回结果的userid
        successinfo = return_data[0]['successInfo']
        ordernum = return_data[0]['orderAliasId']
        print successinfo
        print ordernum

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MobileLoginApi)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
