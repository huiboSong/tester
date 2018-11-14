# coding=utf-8
# 订单用在线支付,准时达,提交订单,并取消订单

import unittest
import time

import comall
from setting.hyptest import el
from setting.hyptest import setting
from setting.hyptest import data
from logs.tests.members.hyptest.shop import common


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
        # 检查搜索框存在
        dr.until("xpath", el.shop_search)
        # 搜索内容输入
        dr.send_keys("xpath", el.shop_search, data.shop_search_content)
        # 点击搜索按钮
        dr.click("xpath", el.shop_search_button)
        # 输出数量
        num = dr.get_text("xpath", el.shop_data_statistics)
        print num

        if num > 0:
            dr.click("xpath", el.shop_first_commdity)
            # 新开页面
            dr.switch_next_window()
            name = dr.get_text("xpath", el.shop_commdity_name)
            print name
            # 列表页-清除购物车
            cart_num = dr.get_text("xpath", el.shop_list_cartnum)
            print cart_num
            # 详情页--加入购物车
            dr.click("xpath", el.shop_addToCart)
            # 详情页--去购物车结算
            dr.click("xpath", el.shop_gotocart)
            dr.until("xpath", el.shop_cartInfo)
            # 购物车--去结算
            dr.click("xpath", el.shop_cartInfo)
            dr.until("xpath", el.shop_select_area)
            # 结算页-选中地址
            dr.click("xpath", el.shop_select_area)
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