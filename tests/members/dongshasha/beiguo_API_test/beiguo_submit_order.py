#coding=utf-8

import testgo
import unittest
import time
from setting.dongshasha import setting
from setting.dongshasha import el
from setting.dongshasha.data import TestData
import random
import base64
import json
import re

class beiguoSubmitOrder(unittest.TestCase):

    #获取商品分类
    def normal_column_get(self):
        #平台商品分类接口的地址
        normal_column = setting.api_url + "json/sys/api/column/normalColumn"
        #请求参数
        normal_column_params={"mid":0}
        #实例化接口类
        request=testgo.testApi(normal_column, setting.api_request_header)
        #发起请求,获取返回结果
        res_data=request.http_request("get",normal_column_params)
        len_data=len(res_data[0]["data"])
        i=random.randint(0,len_data-1)
        #print i,len_data
        self.columnId = res_data[0]["data"][i]["columnId"]
        print  "加车商品的columnId为：%s"%self.columnId







    #获取商品信息（下单前的可卖数可卖数）
    def product_search_get(self):
        self.normal_column_get()
        #商品列表接口的地址
        product_search = setting.api_url + "json/sys/api/product/search"
        #请求参数(分类id)
        product_search_params={"columnId":self.columnId}
        #实例化接口类
        request=comall.ComallApi(product_search,setting.api_request_header)
        #发起请求
        res_data=request.http_request("get",product_search_params)
        #获取商品数
        self.num=res_data[0]["all_counts"]
        #获取要添加进购物车的商品可卖数
        self.sellable = {}
        #要添加进购物车的商品ID
        self.pros = []
        #要添加进购物车的商品所属商户的ID
        self.mids = {}
        #使用columnId进行搜索，随机选择几个商品(3~5个)，之后加车
        self.number=random.randint(3,5)
        #要添加的商品中可卖数充足的商品数
        self.items=0
        for j in range(0,self.number):
            #从获取的分类下的随机选择商品的位置
            rand_no=random.randint(0,self.num-1)
            #保存商品ID
            product=res_data[0]["data"]["searchArticles"][rand_no]["productId"]
            #若商品重复，则重新选择商品
            for n in range(len(self.pros)):
                if(product==self.pros[n]):
                    rand_no=random.randint(0,self.num-1)
                    product=res_data[0]["data"]["searchArticles"][rand_no]["productId"]
            #print "rand_no%d"%rand_no,self.num
            #获得商品的可卖数
            sell=res_data[0]["data"]["searchArticles"][rand_no]["sellable"]
            #可卖数充足，则获取商户名与商品ID
            if sell > 0:
                self.items+=1
                self.pros.append( product)
                self.mids[product]=res_data[0]["data"]["searchArticles"][rand_no]["mid"]
                self.sellable[product]=sell
            #遍历完所有要加车的商品，可卖数均不足，则重新获取加车商品
            elif  j==self.number-1 and self.items==0:
                j=0
        #去除重复的值，set：集合，无序，不重复
        self.pros=list(set(self.pros))
        print "加车商品的商品ID：%s"%self.pros
        print "加车商品的mids：%s"%self.mids
        print "加车商品的可卖数sellable：%s"%self.sellable




        #加车前查询购物车
    def show_cart_before_add_get(self):
        self.product_search_get()
        #查询购物车商品接口的地址
        show_cart = setting.api_url + "json/sys/api/cart/showCart"
        #实例化接口类
        request=comall.ComallApi(show_cart,setting.api_request_header)
        #发起请求,获取返回结果
        res_data=request.http_request("post")
        #加车前，购物车已有商品数量以及要加车的商品，但购物车没有的，置为0
        self.itemNum={}
        self.pro_amounts=0
        mid_num=len(res_data[0]["data"])
        #购物车不为空
        if mid_num!=0:
            #加车前购物车已有商品及要添加商品的数目
            self.itemNum={}
            #商品的商户数
            for i in range(0,mid_num):
                #每个商户的商品种类数
                pro_num=len(res_data[0]["data"][i]["cartItems"])
                for j in range(0,pro_num):
                    #购物车商品总数
                    self.pro_amounts+=res_data[0]["data"][i]["cartItems"][j]["amount"]
                    #获得每件商品
                    product=res_data[0]["data"][i]["cartItems"][j]
                    #加车前购物车中每件商品的数量
                    self.itemNum[product["productId"]]=product["amount"]
                    #遍历所有加车商品，若不在self.itemNum（购物车中所有商品加车前的数量）中，则将其置为0
                    for key in range(len(self.pros)):
                        if self.pros[key] not in self.itemNum:
                            self.itemNum[self.pros[key]]=0
        else:
            for key in range(len(self.pros)):
                self.itemNum[self.pros[key]]=0
        print "加车前，购物车已有商品及数量：%s"%self.itemNum
        print "加车前，购物车已有商品总数为：%d"%self.pro_amounts





    #调用加车接口
    def add_product_cart_post(self):
        self.show_cart_before_add_get()
        #添加进购物车的商品数量
        self.cart_pro_num={}
        for i in range(len(self.pros)):
            amount=random.randint(1,5)
            #可卖数不足<要加车数量，则将所有商品加车（在获取商品信息接口，获得的商品均有可卖数）
            #print self.sellable[self.pros[i]],amount
            if self.sellable[self.pros[i]]<amount:
                amount=self.sellable[self.pros[i]]
            self.cart_pro_num[self.pros[i]]=amount


            request_params={"productId":self.pros[i],"amount":amount,"mid":self.mids[self.pros[i]]}
            #print "self.pros[i]:%s"%self.pros[i]
            #加车接口的地址
            add_product_cart = setting.api_url + "json/sys/api/cart/addProductCart"
            #实例化接口类
            request=comall.ComallApi(add_product_cart,setting.api_request_header)
            #发起请求
            res_data=request.http_request("post",request_params)

            if res_data[0]["errerrcode"]==200:
                self.cart_amount=res_data[0]["data"]["totalAmount"]
                #print "self.pros[i]:%s"%self.pros[i]
                self.pro_amounts+=amount
                #self.assertEqual(self.cart_amount,self.pro_amounts,"商品加车失败self.cart_amount：%d,self.pro_amounts:%d"%(self.cart_amount,self.pro_amounts))
            else:
                self.cart_pro_num[self.pros[i]]=0
                #self.assertEqual(self.cart_amount,self.pro_amounts,"商品加车失败self.cart_amount：%d,self.pro_amounts:%d"%(self.cart_amount,self.pro_amounts))
        print "添加进购物车的商品数量：%s"%self.cart_pro_num
        print "加车后，购物车的商品总数：%s"%self.pro_amounts




    #加车后查询购物车商品
    #获取购物车商品列表
    def show_cart_after_add_get(self):
        self.add_product_cart_post()
        #查询购物车商品接口的地址
        product_search = setting.api_url + "json/sys/api/cart/showCart"
        #实例化接口类
        request=comall.ComallApi(product_search,setting.api_request_header)
        #发起请求,获取返回结果
        self.re_data=request.http_request("post")
        self.cartids=""
        mid_num=len(self.re_data[0]["data"])
        for i in range(mid_num):
            pro_num=len(self.re_data[0]["data"][i]["cartItems"])
            #获取结算时所需购物车ids
            if i==mid_num-1:
                self.cartids+=str(self.re_data[0]["data"][i]["cartId"])
            else:
                self.cartids+=str(self.re_data[0]["data"][i]["cartId"])+","
            for j in range(0,pro_num):
                product=self.re_data[0]["data"][i]["cartItems"][j]
                for key in self.itemNum:
                    if key==product["productId"] and (key in self.cart_pro_num):
                        print "self.itemNum[key]:%s" %self.itemNum[key]
                        self.itemNum[key]+=self.cart_pro_num[key]
                        print "购物车商品%s添加%d件后，为%d件" %(key,self.cart_pro_num[key],self.itemNum[key])
                        self.assertEqual(self.itemNum[key],product["amount"],"购物车中商品%s的数目%d与加进购物车的数目%d不符"%(key,product["amount"],self.itemNum[key]))
                    elif key==product["productId"] and (key not in self.cart_pro_num):
                        print "购物车中商品%s数量不变，现有%d件，原有%d"%(key,product["amount"],self.itemNum[key])
                        self.assertEqual(self.itemNum[key],product["amount"],"购物车中商品%s的数目%d与加车前购物车该商品的数目%d不符"%(key,product["amount"],self.itemNum[key]))
        print "购物车ids为：%s"%self.cartids
        print "加车后，购物车所有商品的数量：%s"%self.itemNum


    #获取结算页基础信息
    def base_info_post(self):
        self.show_cart_after_add_get()
        #结算页基础信息接口地址
        base_info = setting.api_url + "json/sys/api/order/baseinfo"
        #请求参数
        params=base64.b64encode('{"cartids":"%s"}'%self.cartids)
        #print self.cartids,params
        base_info_params={"params":params}
        #实例化接口类
        request=comall.ComallApi(base_info,setting.api_request_header)
        #发起请求,获取返回结果
        res_data=request.http_request("post",base_info_params)
        #print res_data
        len_pro_item=len(res_data[0]["data"]["productItems"])
        #地址id
        self.addressId=res_data[0]["data"]["accepterAddress"]["addressId"]
        #支付方式集合
        self.payres={}
        self.payres["payModeName"]=res_data[0]["data"]["payres"]["payModeName"]
        self.payres["payModeId"]=res_data[0]["data"]["payres"]["payModeId"]
        self.payres["payPrice"]=res_data[0]["data"]["payres"]["payPrice"]
        #配送方式集合
        self.deliveryModes=[]
        self.soldNum={}
        self.products=""
        for cartNum in range(0,len_pro_item):
            #print cartNum,len_pro_item
            self.deliveryModes.append(res_data[0]["data"]["productItems"][cartNum]["deliveryModes"])
            len_cart_pro_num=len(res_data[0]["data"]["productItems"][cartNum]["productInfos"])
            for  proNum in range(0,len_cart_pro_num):
                product=res_data[0]["data"]["productItems"][cartNum]["productInfos"][proNum]["productId"]
                self.soldNum[product]=res_data[0]["data"]["productItems"][cartNum]["productInfos"][proNum]["amount"]
                self.products+=str(product)+","
        #使用正则表达式去掉最后的逗号（用空字符替换）
        replace_reg= re.compile(r',$')
        self.products=replace_reg.sub('',self.products)

        #提交订单所需数据
        self.cart={}
        self.cart["cartids"]=self.cartids
        self.cart["addressId"]=self.addressId
        self.cart["payres"]=self.payres
        self.cart["deliveryModes"]=self.deliveryModes
        print "提交订单参数：%s"%json.dumps(self.cart).decode('unicode_escape')
        print "购物车商品的所有商品的IDS：%s"%self.products
        print "下单前，购物车中所有商品的数量：%s"%self.soldNum



        #下单前对商品进行查询，并保存
    def product_lists_bafore_submit_get(self):
        self.base_info_post()
        #接口请求的详细地址
        request_url = setting.api_url + "json/sys/api/product/search"
        #请求的参数，结算页得到的商品
        request_param = {"productIds":self.products}
        #实例化ComallApi类
        request = comall.ComallApi(request_url,setting.api_request_header)
        #调用ComallApi类的http_request方法，发起请求，获得返回值
        res_data = request.http_request("get",request_param)
        self.sellable={}
        #获取商品数
        self.cart_pro_amount=res_data[0]["all_counts"]
        for item in self.itemNum:
            for t in range(0,self.cart_pro_amount):
                self.pro=res_data[0]["data"]["searchArticles"][t]
                self.sellable[self.pro["productId"]]=self.pro["sellable"]
        print "下单前，商品的可卖数：%s"%self.sellable




    #提交订单
    def submit_order_post(self):
        self.product_lists_bafore_submit_get()
        #提交订单接口地址
        submit_order = setting.api_url + "json/sys/api/order/submitOrder"
        #请求参数，根据结算页接口返回信息，对其进行base64加密，获得提交订单参数
        params=base64.b64encode(json.dumps(self.cart).decode('unicode_escape'))
        #decode('unicode_escape')用来将unicode编码转化为对应的字符
        #print json.dumps(self.cart).decode('unicode_escape')
        #print params
        submit_order_params={"params":params}
        #实例化接口类
        request=comall.ComallApi(submit_order,setting.api_request_header)
        #发起请求,获取返回结果
        res_data=request.http_request("post",submit_order_params)
        #print res_data
        self.parentAliaserrcode=res_data[0]["data"]["parentAliaserrcode"]
        print "订单编号为：%s"%self.parentAliaserrcode



    #获取订单状态为待付款的订单列表
    def order_lists_get(self):
        #订单列表接口请求的详细地址
        request_url = setting.api_url + "json/sys/api/user/orderLists"
        #请求的参数，订单状态为待付款,查找范围为30天
        request_param = {"status":1,"page":1,"pageCount":20,"scope":"1"}
        #实例化ComallApi类
        request = comall.ComallApi(request_url,setting.api_request_header)
        #调用ComallApi类的http_request方法，发起请求，获得返回值
        self.res_datas = request.http_request("get",request_param)
        #print self.res_datas



    #下单成功后，判断可卖数是否变化
    def test_product_lists_after_submit_get(self):
        #提交订单
        self.submit_order_post()
        time.sleep(5)

        #查看订单列表
        self.order_lists_get()
        self.orderId=0
        order_num= self.res_datas[0]["all_counts"]
        for i in range(0,order_num):
            parentAliasid=self.res_datas[0]["data"][i]["parentAliasid"]
            if parentAliasid==self.parentAliaserrcode:
                #若找到刚下单的订单号，则获取其orderId
                self.orderId=self.res_datas[0]["data"][i]["orderId"]
                #self.assertTrue(self.orderId!=0,"订单号存在")
                break
        print  "订单%s的orderId为：%s"%(parentAliasid,self.orderId)
        self.assertTrue(self.orderId!=0,"订单号%s存在，其orderId为：%s"%(parentAliasid,self.orderId))



        #下单后对商品进行查询，判断其可卖数是否变化
        #接口请求的详细地址
        request_url = setting.api_url + "json/sys/api/product/search"
        #请求的参数，结算页得到的商品
        request_param = {"productIds":self.products}
        #实例化ComallApi类
        request = comall.ComallApi(request_url,setting.api_request_header)
        #调用ComallApi类的http_request方法，发起请求，获得返回值
        res_data = request.http_request("get",request_param)
        #下单后商品可卖数
        self.sellNum={}
        #获取商品数
        self.cart_pro_amount=res_data[0]["all_counts"]
        for item in self.soldNum:
            for t in range(0,self.cart_pro_amount):
                self.pro=res_data[0]["data"]["searchArticles"][t]
                if self.pro["productId"]==item:
                    self.sellNum[item]=self.pro["sellable"]
                    self.surplus=self.sellable[item]-self.soldNum[item]
                    #print self.surplus
                    self.assertEqual(self.surplus,self.sellNum[item],"商品%s下单前可卖数为：%d，购买：%d件，还剩：%d"%(item,self.sellable[item],self.soldNum[item],self.sellNum[item]))
        print "下单后,商品的可卖数为：%s"%self.sellNum
















