# coding=utf-8

import unittest
import time
from ddt import ddt, data, unpack
# 引入主框架文件
import comall
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.dongshasha import el
from setting.dongshasha import setting
from setting.dongshasha.data import TestData as dt

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#搜索商品接口
class beiguoProductSearch(unittest.TestCase):
    #获取请求的参数
    productId = dt.get("product_search")[0]
    keyword = dt.get("product_search")[1]
    columnId = dt.get("product_search")[2]
    def test_product_search_get(self):
        #接口请求的详细地址
        request_url = setting.api_url + "json/sys/api/product/search"

        #请求的参数
        request_param_json = {"productIds":self.productId}

        #实例化ComallApi类
        request = comall.ComallApi(request_url,setting.api_request_header)

        #调用ComallApi类的http_request方法，发起请求，获得返回值
        res_data = request.http_request("get",request_param_json)

        #从返回数据中获得查找到的商品ID，用来和要查找的商品ID比较
        proId = res_data[0]["data"]["searchArticles"][0]["productId"]
        #转换数据类型（int->string），返回数据类型为int，输入参数为string,故比较结果为false
        prodductId = str(proId)

        #从返回数据中获得查找到的符合条件的商品数
        all_counts = res_data[0]["all_counts"]

        #查找到的商品ID与要查找的商品ID是否相同
        self.assertEqual(self.productId,prodductId,"商品搜索失败")

        #判断是否搜索到并且仅查到一条记录
        self.assertEqual(all_counts,1,"根据某一商品ID搜索，未得到或得到多条记录")






# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Module)
    result = unittest.TextTestRunner(verbosity=2).run(suite)