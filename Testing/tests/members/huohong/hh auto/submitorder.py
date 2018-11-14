# coding=utf-8

import unittest
import time
import comall
from setting.huohong import el
from setting.huohong import setting
from setting.huohong.data import TestData
from ddt import ddt, data, unpack


@ddt
class Login(unittest.TestCase):

    d = TestData().get("user_login_success")
    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        self.dr.open(setting.productinfo_url)
        time.sleep(1)

    @data(d[0])
    @unpack
    def test_login_success(self,login_name, pw,message):
        dr = self.dr
        # 检查并点击加入购物车
        dr.until("xpath", el.womai_pro_addtocart_btn)
        dr.click("xpath", el.womai_pro_addtocart_btn)
        # 检查并点击去购物车结算
        dr.until("xpath", el.womai_gotocart_btn)
        dr.click("xpath", el.womai_gotocart_btn)
        time.sleep(2)
        # 检查并点击去购物车结算
        dr.until("xpath", el.womai_cofcocheck_btn)
        dr.click("xpath", el.womai_cofcocheck_btn)
        time.sleep(2)
        dr.switch_to_frame(4)
        # 输入用户名密码
        dr.send_keys("xpath", el.womai_name_inoput_login_t,login_name)
        dr.send_keys("xpath", el.womai_pwd_inoput_login_t, pw)
        # 点击登录按钮
        dr.click("xpath", el.womai_info_submit_login_btn)
        # 检查并点击去购物车结算
        dr.until("xpath", el.womai_cofcocheck_btn)
        dr.click("xpath", el.womai_cofcocheck_btn)
        time.sleep(2)
        # 下一步
        dr.until("xpath", el.womai_nextStep_btn)
        dr.click("xpath", el.womai_nextStep_btn)
        # 检查卡券
        #dr.until("xpath", el.womai_jump_a)
        #dr.click("xpath", el.womai_jump_a)
        time.sleep(2)
        # 提交订单
        dr.until("xpath", el.womai_submitorder_btn)
        dr.click("xpath", el.womai_submitorder_btn)

        #message = dr.get_text("xpath", el.womai_myorder_t)
        #self.assertEquals(u"您的订单号：", message, "下单成功")

    def tearDown(self):
       pass




if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
