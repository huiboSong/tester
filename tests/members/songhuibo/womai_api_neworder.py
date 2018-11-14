# coding=utf-8
import testgo,hashlib,unittest,time
from setting.test_test import setting
from setting.test_test import el
from setting.test_test.data import TestData as dt

#
# class TestCase(unittest.TestCase):
#
#     def test_login_post(self):
#         #api登录
#         request_url = setting.hooli_url + "loginnew"
#         request_body_data_json = {"username":"13520843514","password":"123456qq"}
#         womai = hooli.hooliApi(request_url,setting.hooli_header)
#         return_data = womai.http_request("post", request_body_data_json)
#         usersession = return_data[0]['usersession']
#         userid = return_data[0]['userid']
#         message = return_data[0]['sendcouponcard']['message']
#         #self.assertEqual("58803862",str(userid),"return_data[0]['userid']")
#         if message == "欢迎使用手机我买网":
#             # 更新headers[dict格式]的值，方便其他请求调用
#             setting.hooli_header.update(
#                 {
#                     'Usersession': return_data[0]['usersession'],
#                     'Userid': str(return_data[0]['userid'])}
#                      )
#         else:
#             print ("Error, HTTP Headers[dict] key[usersession] value is not updated.")
# #
# #     def test_loadCart_post(self):
# #         #加载购物车
# #         request_url = setting.api_uri + "html5/cart/loadCart"
# #         {"productId":"956849","amount": "1","productType": "0","ruleId": ""}
# #         request_body_data = {"data": '[{"productId":"956849","amount": "1","productType": "0","ruleId": ""}]'}
# #         womai = comall.ComallApi(request_url,setting.womaiapi_header)
# #         return_data = womai.http_request("post",request_body_data)
# #         #print return_data[0]['shoppingCarts']
# #         cartid = return_data[0]['shoppingCarts'][0]['cartsInfo'][0]['cartId']
# #         activeId= return_data[0]['shoppingCarts'][0]['cartsInfo'][0]['activeId']
# #         if cartid > 0:
# #         # 更新headers[dict格式]的值，方便其他请求调用
# #              setting.params.update(
# #                 {'cartids': str(return_data[0]['shoppingCarts'][0]['cartsInfo'][0]['cartId'])}
# #                  )
# #         else:
# #             print "Error, HTTP params[dict] key[cartids] value is not updated."
# #         print setting.params
# #         #print str(setting.params.get("cartIds"))
# #         #print cartid
# #     def test_cartCheck_post(self):
# #         #合车校验
# #         request_url = setting.api_uri + "html5/cart/cartCheck"
# #         #print str(setting.params("cartIds"))
# #         request_body_data = {"data":'{"cartIds:"'+str(setting.params.get("cartids"))+'}'}
# #         womai = comall.ComallApi(request_url,setting.womaiapi_header)
# #         return_data = womai.http_request("post",request_body_data)
# #         print return_data
# #     def test_newCheckOut_post(self):
# #         #结算中心
# #         request_url = setting.api_uri + "html5/newCheckOut"
# #         request_body_data = {"data":'{{"addressId":"9662935", "deliveryMethod":{"deliveryId":"0","deliveryDate":"0","segmentTime":"0"},"cartMsgs":[{"cartId":'+str(setting.params.get("cartids"))+', "chooseCoupon":[""]}],"payWay":{"wmPayAmount":"10","otherPayId":"200"},"isFirst":"1","foodyPassword":"", "orderLeaverMsg":"songbo","invoice":{"isNeedInvoice":"true","invoiceType":"0", "invoiceTitle":"1","companyName":"sss","invoiceContent":"1","receiverPhone":"1213123","receiverEmail":"asdfsaf@111.com"}}}'}
# #         womai = comall.ComallApi(request_url,setting.womaiapi_header)
# #         return_data = womai.http_request("post",request_body_data)
# #         print return_data
# #     def test_submidorder_post(self):
# #         #提交订单
# #         request_url = setting.api_uri + "html5/submitorder/submitordermobile"
# #         request_body_data = {"data":'{{"addressId":"9662935","isNeedInvoice":"1","invoiceTitle":"1","invoiceType":"1","invoiceContent":"1", "receiverPhone":"13393112621","companyName":"haha","receiverEmail":"15465@163.com","payPassword": "123qq123","isShowPrice":"1","payway":{"wmPayAmount":"0.0","otherPayId":"200" },"cpsData":"","userName":"JAMES",  "userIdentify":"130425199012205812","identifyPicPath":["",""],"deliveryMethod":{"deliveryId":"1","deliveryDateId":"","segmentTime":"1"},"cartMsgs":[{"cartId":'+str(setting.params.get("cartids"))+',"chooseCoupon":[]}], "orderLeaverMsg":"LEAVER","foodyPassword":"SFDX"}}'}
# #         womai = comall.ComallApi(request_url,setting.womaiapi_header)
# #         return_data = womai.http_request("post",request_body_data)
# #         print return_data
# #
# #
# # if __name__ == "__main__":
# #     suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
# #     result = unittest.TextTestRunner(verbosity=2).run(suite)
# #

class test (unittest.TestCase):
    def sign (self):
        dict = setting.hooli_header
        value = (dict.get('t') + 'salt') + (dict.get('v') + 'salt') + (dict.get('c') + 'salt') + (dict.get('sign') + 'salt')
        key = ('t'  + 'v' + 'c' + 'sign')
        key ="".join((lambda x:(x.sort(),x)[1])(list(key)))
        data = (key + value)
        c = hashlib.md5()
        c.update(data)
        d = (c.hexdigest()).upper() + 'salt'
        a = hashlib.md5()
        a.update(d)
        f = (a.hexdigest()).upper()
        return f
    #setting.hooli_header.update('sign',f)
    # if sign():
    #
    #     setting.hooli_header.update(
    #         {'sign':str(f)}
    #     )
    #     print setting.hooli_header
    # else:
    #     print ("Error, HTTP Headers[dict] key[sign] value is not updated")
a = 'vJBt7mBBEh'
b = 'password'
def md5(str):
        '''md5加密方法'''
        m = hashlib.md5  ()
        m.update(str)
        return m.hexdigest()
c =  md5(md5(b) + a)
print c