# coding=utf-8
# 点击首页一级分类,列表页加入继续购物,加入购物车,商品收藏,新增地址

import unittest
import time

import comall
from logs.tests.members.hyptest.shop import common
from setting.hyptest import el
from setting.hyptest import setting


class shopsubmitorder(unittest.TestCase):

    def setUp(self):
        """初始化方法，在所有test执行前执行"""
        # 初始化浏览器对象，从setting文件中的driver_type读取启动浏览器的类型（ff\firefox、chrome、ie、opera等）
        self.dr = comall.Comall(setting.driver_type)
        time.sleep(1)
        # 最大化浏览器窗口
        self.dr.max_window()
        time.sleep(1)
        # 调用地址
        #shop_common.shop_area_select(self.dr)
        common.login_success(self.dr, self)

    def test_first_case(self):
        # 获得setUp初始化的对象
        dr = self.dr
        # 检查一级分类存在
        dr.until("xpath", el.shop_category)
        # 点击左侧第一个一级分类
        dr.click("xpath", el.shop_category)
        # 输出数量
        num = dr.get_text("xpath", el.shop_data_statistics)
        print num

        if num > 0:
            # 列表页-点击价格排序
            dr.click("xpath", el.shop_list_price)
            # 列表页-第一个商品加入购物车
            dr.click("xpath", el.shop_list_gocart)
            # 列表页-继续购物
            dr.click("xpath", el.shop_list_goShopping)
            # 列表页-去购物车结算
            dr.click("xpath", el.shop_list_gocart)
            dr.click("xpath", el.shop_list_addSucceed)
            # 购物车-单品价格
            singleprice = dr.get_text("xpath", el.shop_singleprice)
            print singleprice
            # 购物车-商品数量增加
            dr.click("xpath", el.shop_addgoods)
            # 购物车-单品总价
            totalprice = dr.get_text("xpath", el.shop_totalprice)
            print totalprice
            # 购物车-收藏商品
            #dr.find_element_by_xpath("xpath", el.shop_tocollection)
            dr.click("xpath", el.shop_tocollection)
            # 购物车--去结算
            dr.click("xpath", el.shop_cartInfo)
            #dr.until("xpath", el.shop_select_area)
            # 结算页-点击新增地址按钮
            dr.click("xpath", el.shop_addaddress)
            # 结算页-地址收件人
            dr.until("xpath", el.shop_recipients)
            dr.send_keys("xpath", el.shop_recipients, "test")
            # 结算页-收货地址
            dr.click("xpath", el.shop_address1)
            dr.click("xpath", el.shop_address2)
            dr.click("xpath", el.shop_address3)
            dr.click("xpath", el.shop_address4)
            dr.click("xpath", el.shop_address5)
            dr.click("xpath", el.shop_address6)
            dr.click("xpath", el.shop_address7)
            dr.click("xpath", el.shop_address8)
            # 结算页新增收货地址
            dr.send_keys("xpath", el.shop_detail_address, "test123")
            # 结算页-新增邮政编码
            dr.send_keys("xpath", el.shop_postcode, "100010")
            # 结算页-新增手机号
            dr.send_keys("xpath", el.shop_iponenum, "13488885205")
            # 结算页-新增邮箱
            dr.send_keys("xpath", el.shop_email, "93406294@qq.com")
            # 结算页-保存按钮
            dr.click("xpath", el.shop_consignee)
            dr.click("xpath", el.shop_sure_area)
            # 结算页-选择支付方式
            dr.click("xpath", el.shop_payAndDelivery)
            # 结算页-选择配送方式
            dr.click("xpath", el.shop_deliverymode)
            dr.click("xpath", el.shop_choose_deliverymode)
            dr.click("xpath", el.shop_time)
            # 结算页-点击保存支付及配送方式按钮
            dr.click("xpath", el.shop_savepayment)
            # 结算页-点击不需要发票
            dr.click("xpath", el.shop_invoice)
            # 结算页-点击提交订单按钮
            dr.click("xpath", el.shop_submit_order)
            #idnum = dr.get_text("xpath", el.shop_idnumber)
            #print idnum
            message = dr.get_text("xpath", el.shop_order_success)
            print message
            self.assertEqual(message, "订单提交成功", "下单成功")
            #点击查看订单详情
            dr.click("xpath", el.shop_vieworder)
            #点击取消订单按钮
            dr.click("xpath", el.shop_cancelorder)
            #选择取消订单原因
            dr.until("xpath", el.shop_cancelreason)
            dr.click("xpath", el.shop_cancelreason)
            dr.click("xpath", el.shop_reasonBox)
            # 取消alert重写
            dr.js('window.alert = function(){return true};')
            #选择取消订单
            dr.click("xpath", el.shop_sure_cancle)
            time.sleep(2)
            #alert弹出框,点击确认按钮
            #dr.accept_alert()
            # 订单列表-已取消状态
            outmes = dr.get_text("xpath", el.shop_Cancelled)
            print outmes
            self.assertEqual(outmes, "已取消", "取消订单成功")

        else:
            message = dr.get_text("xpath", el.shop_list_empty)
            print message


    def tearDown(self):
        dr = self.dr
        dr.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(shopsubmitorder)
    result = unittest.TextTestRunner(verbosity=2).run(suite)