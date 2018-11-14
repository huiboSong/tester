# coding=utf-8
import unittest
import comall
from setting.songhuibo import setting
from setting.songhuibo import el
from setting.songhuibo.data import TestData as dt
import time

class TestCase(unittest.TestCase):

    def test_login_post(self):
        #api登录
        request_url = setting.api_uri + "loginnew"
        request_body_data_json = {"username":"mobile_ceshi20","password":"123456qq"}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_data_json)
        usersession = return_data[0]['usersession']
        userid = return_data[0]['userid']
        message = return_data[0]['sendcouponcard']['message']
        #self.assertEqual("58803862",str(userid),"return_data[0]['userid']")
        if message == "欢迎使用手机我买网":
            # 更新headers[dict格式]的值，方便其他请求调用
            setting.womaiapi_header.update(
                {
                    'Usersession': return_data[0]['usersession'],
                    'Userid': str(return_data[0]['userid'])}
                     )
        else:
            print "Error, HTTP Headers[dict] key[usersession] value is not updated."
        print usersession,userid

    def test_cartnew_post(self):
         #api加车
         request_url = setting.api_uri + "html5/car/cartnew"
         request_body_data = {"data": '[{"type":1,"skuId":"956726","amount":"1","productType":"0","classType":"1"}]'}
         womai = comall.ComallApi(request_url,setting.womaiapi_header)
         return_data = womai.http_request("post", request_body_data)
         sellername = return_data[0]['shoppingCarts'][0]['sellerName']
         cart_id = return_data[0]['shoppingCarts'][0]['cart_id']
         if cart_id > 0:
        # 更新headers[dict格式]的值，方便其他请求调用
             setting.params.update(
                {'cartids': str(return_data[0]['shoppingCarts'][0]['cart_id'])}
                 )
         else:
              print "Error, HTTP params[dict] key[cartids] value is not updated."
         #print setting.params


    def test_checkout_post(self):
         #api结算中心
         request_url = setting.api_uri + "html5/checkout/checknew"
         request_body_data = {"data":'{"address":"9662935","couponcard":[],"cartId":'+str(setting.params.get("cartids"))+',"payway":{"amount":"","other":"200"},"express_time":{"delivery_id":"0","segment_id":"0"},"is_first":"0"}'}
         womai = comall.ComallApi(request_url,setting.womaiapi_header)
         return_data = womai.http_request("post", request_body_data)

    def test_submitorder_post(self):
        #api提交订单
        request_url = setting.api_uri + "html5/submitorder/submitnew"
        request_body_data = {"data":'{"notShowPrice":false,"remark":"songhuibo","invoice_title":"song","invoice_id":"0","payPassword":"","address":"9662935","cartId":'+str(setting.params.get("cartids"))+',"couponcard":[],"payway":{"amount":"","other":"200"},"express_time":{"delivery_id":"1","segment_id":"1"}}'}
        womai = comall.ComallApi(request_url,setting.womaiapi_header)
        return_data = womai.http_request("post", request_body_data)
        orderAliasId = return_data[0]['orderAliasId']
        successInfo = return_data[0]['successInfo']
        print orderAliasId
        print successInfo
        self.assertEqual("恭喜！订单已提交成功！", str(successInfo), "successed")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
