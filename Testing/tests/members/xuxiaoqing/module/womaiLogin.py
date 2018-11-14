# coding=utf-8

import comall
import unittest
from setting.xuxiaoqing import setting
from setting.xuxiaoqing import data
from setting.xuxiaoqing import el
import time

class Testcase(unittest.TestCase):
    def setUp(self):
        # 启动浏览器
        self.dr = comall.Comall("chrome")
        #打开我买网
        self.dr.open(setting.womai_url)
        #窗口最大化
        self.dr.max_window()
    def test_login(self):
        dr = self.dr
        dr.send_keys("xpath","//*[@id='cartLoginId']",u"testqingqing")
        dr.send_keys("xpath","//*[@id='cartPassword']",u"111111qq")
        dr.click("xpath","//*[@id='login_submit_btn_real']")
        time.sleep(2)
        message = dr.get_text("xpath","//*[@id='top_login_span']/li[2]/a")
        self.assertEquals("退出",message,"success")

    def tearDown(self):
        pass
        # self.dr.close()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testcase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)