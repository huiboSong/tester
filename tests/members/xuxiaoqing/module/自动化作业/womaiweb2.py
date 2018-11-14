# coding=utf-8

import comall
import unittest
from setting.xuxiaoqing import setting
from setting.xuxiaoqing import data
from setting.xuxiaoqing import el
import time

class TestCase(unittest.TestCase):
    def setUp(self):
        self.dr = comall.Comall("chrome")
        self.dr.open(setting.wo_mai)
        self.dr.max_window()

    def test_login(self):
        dr = self.dr
        dr.click("xpath",el.product_floorproduct) #打开首页的一个商品
        dr.switch_next_window() #打开新窗口
        dr.click("xpath",el.button_buy) #单击抢购
        time.sleep(2)
        dr.click("xpath",el.showIncludeCart)
        dr.click("xpath",el.cofcocheck2)
        time.sleep(2)
        dr.switch_to_frame(4)
        dr.send_keys("xpath", el.cartLoginId1, "testqingqing")
        dr.send_keys("xpath", el.cartPassword1, "111111qq")
        dr.click("xpath", el.login_submit_btn_real1)
        dr.click("xpath", el.cofcocheck2)
        dr.click("xpath",el.nextStep)
        time.sleep(2)
        dr.click("xpath",el.alert)
        time.sleep(2)
        dr.click("xpath",el.submitOrder)
        message = dr.get_text("xpath",el.notice)
        self.assertEquals(u"请选择支付方式完成付款。1小时内未完成付款，订单将被自动取消。",message,"success")
        dr.until_page_load()





    def tearDown(self):
        pass
         #self.dr.close()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testcase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)