# coding=utf-8

import comall
import unittest
from core.databaseDriver import SqlDriver
from setting.wwjtest import setting
from setting.wwjtest.data import TestData as TD


class Squirrel_Api_Test(unittest.TestCase):
    # 参数化数据获得
    d = TD().get("review")
    d1 = TD().get("db_review_update")

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

    def squirrel_GetReviewProduct(self):
        """获取评论商品操作"""
        request_uri = setting.api_uri + "remark/reviewProduct"
        request_body_data_json = {"param": "{'orderId':'"+self.d.get('orderId')+"'}"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        json_status = re_data[0]['data']['items'][0]['status']
        if json_code == 0 & json_status == 0:
            setting.params.update(
                {
                    'productId':    str(re_data[0]['data']['items'][0]['productId']),
                    'productToRemarkId':    str(re_data[0]['data']['items'][0]['productToRemarkId']),
                    'reviewId':    str(re_data[0]['data']['items'][0]['reviewId'])

                })
        else:
            print "Error, reviewProduct key [productId][productId][reviewId] value is not updated."
        self.assertEqual("0", str(json_code), "GetReviewProduct Test Failed! stateCode != 0")

    def squirrel_UploadReviewImage(self):
        """上传评论图片操作"""
        request_uri = setting.api_uri + "global/uploadImage"
        request_body_data_json = {"param": "{'pic':'"+self.d.get('pic')+"','location':'review'}"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        if json_code == 0:
            setting.params.update(
                {
                    'pictureId':    str(re_data[0]['data']['pictureId'])

                })
        else:
            print "Error, reviewImage key [pictureId] value is not updated."
        self.assertEqual("0", str(json_code), "Upload ReviewImage Test Failed! stateCode != 0")

    def test_squirrel_addReview(self):
        self.squirrel_login()
        self.squirrel_GetReviewProduct()
        self.squirrel_UploadReviewImage()
        """添加评论操作"""
        request_uri = setting.api_uri + "remark/add"
        request_body_data_json = {"param": "{'orderId':'"+self.d.get('orderId')+"','productId':'" + str(setting.params.get('productId')) + "','content':'Goods is very good！！！','score':5,'isAnonymously':true,'productToRemarkId':'" + str(setting.params.get('productToRemarkId')) + "','pictureIds':[" + str(setting.params.get('pictureId')) + "]}"}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("post", request_body_data_json)
        json_code = re_data[0]['stateCode']
        if json_code == 0:
            mysql = SqlDriver()
            table_name = self.d1.get('table_name')
            update_values = self.d1.get('update_values')
            where = "orderId=" + self.d.get("orderId") + " and ProductId=" + str(setting.params.get("productId")) + ""
            mysql.exec_mysql_update(table_name, update_values, where)
        else:
            print "Error, review products tables key [status] value is not updated."
        self.assertEqual("0", str(json_code), "AddReview Test Failed! stateCode != 0")

    def test_squirrel_getReviewCount(self):
        """获取商品的评论数量操作"""
        request_uri = setting.api_uri + "remark/count?param={'productId':'"+self.d.get('productId')+"'}"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Get ReviewCount Test Failed! stateCode != 0")

    def test_squirrel_getReviewList(self):
        """获取商品评论列表操作"""
        request_uri = setting.api_uri + "remark/list?param={'type':0,'productId':'"+self.d.get('productId')+"','page':1,'pageCount':3}"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Get ReviewList Test Failed! stateCode != 0")

    def test_squirrel_getReviewInfo(self):
        self.squirrel_GetReviewProduct()
        """获取商品评论详情操作"""
        request_uri = setting.api_uri + "remark/info?param={'id':'" + str(setting.params.get('reviewId')) + "'}"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Get ReviewInfo Test Failed! stateCode != 0")

    def test_squirrel_getIndexInfo(self):
        """获取首页数据操作"""
        request_uri = setting.api_uri + "index/info?param={'type':'" + self.d.get('type') + "'}"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Get IndexInfo Test Failed! stateCode != 0")

    def test_squirrel_getRecommendList(self):
        """获取热评推荐商品列表操作"""
        request_uri = setting.api_uri + "index/recommendList/1"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Get RecommendList Test Failed! stateCode != 0")

    def test_squirrel_getRecommendArticleList(self):
        """获取编辑精选列表操作"""
        request_uri = setting.api_uri + "index/getRecommendArticleList"
        request_body_data_json = {}
        api = comall.ComallApi(request_uri, setting.common_headers)
        re_data = api.http_request("get", request_body_data_json)
        json_code = re_data[0]['stateCode']
        self.assertEqual("0", str(json_code), "Get RecommendArticleList Test Failed! stateCode != 0")

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Squirrel_Api_Test)
    result = unittest.TextTestRunner(verbosity=2).run(suite)


