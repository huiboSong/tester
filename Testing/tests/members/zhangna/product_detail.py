# coding=utf-8
import unittest
# 引入主框架文件
import testgo
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.test_test import el
from setting.test_test import setting
from selenium.webdriver.common.action_chains import ActionChains as act
# from selenium.common.exceptions import TimeoutException
# from setting.zhangna.data import TestData as dt
import time

class TestCase(unittest.TestCase):

    def setUp(self):
        # 启动浏览器
        self.dr = testgo.Hooli("chrome")
        self.dr.max_window()
        self.dr.open(setting.womai_detail_url)
        self.dr.until_page_load()

    def test_tt(self):
        dr = self.dr
        dr.click("xpath", el.womai_detail_sum)
        time.sleep(5)
        dr.click("xpath", el.womai_detail_add)
        time.sleep(5)
        success_word = dr.get_text("xpath", "//*[@id='showIncludeCart']/div[4]/div[1]")
        print(success_word)
        self.assertEqual("此商品已成功放入购物车", success_word, "继续下一步")
        dr.click("xpath", el.womai_onlie_account)
        dr.click("xpath", el.womai_onlie_account_sum)
        time.sleep(5)
        dr.click("xpath", el.womai_onlie_account_jiesuan)
        time.sleep(5)
        dr.switch_to_frame(4)
        time.sleep(2)
        dr.send_keys("xpath", el.womai_online_account_login, "zntest")
        dr.send_keys("xpath", el.womai_online_account_password, "111111qq")
        dr.click("xpath", el.womai_online_account_s_login)
        success_word = dr.get_text("xpath", "//*[@id='top_login_span']/li[2]")
        print(success_word)
        self.assertEqual("退出", success_word, "登录失败")
        dr.click("xpath", el.womai_online_shopping_jiesuan)
        dr.click("xpath", el.womai_online_shopping_next)
        dr.click("xpath", el.womai_online_submitorder)
        success_word = dr.get_text("xpath", "/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/li[1]")
        print(success_word[0:6])
        self.assertEqual("您的订单号：", success_word[0:6], "提交订单失败")
        order_number = dr.get_text("xpath", el.womai_ol_order_cannel_ordernumber)
        print(order_number)
        dr.click("xpath", el.womai_online_ordernumber)
        dr.click("xpath", el.womai_online_cancelorder)
        dr.click("xpath", el.womai_online_cancelorder_reseaon)
        dr.click("xpath", el.womai_online_cancelorder_reseaon_submit)
        dr.until("xpath", el.womai_ol_order_cannel_msg)
        a = dr.get_text("xpath", el.womai_ol_order_cannel_msg)
        b = "尊敬的顾客您好，您的订单"+order_number+ "取消订单操作已成功，已支付款项预计在1-3个工作日退至您原支付账户/银行卡，小买欢迎您再次订购，谢谢！"
        self.assertEqual(a, b, "取消订单失败")
        dr.click("xpath", el.womai_online_cancelorder_confirm)




    def tearDown(self):
        pass
        self.dr.close()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
