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
        self.dr.open(setting.web_register)
        #窗口最大化
        self.dr.max_window()
    def test_login(self):
        dr = self.dr
        dr.send_keys("xpath","//*[@id='Email']",u"gfdhgtfhfj@qq.com")
        dr.send_keys("xpath","//*[@id='loginId']",u"fgfdhtfg45")
        dr.send_keys("xpath","//*[@id='password']",u"111111qq")
        dr.send_keys("xpath","//*[@id='password2']",u"111111qq")
        dr.send_keys("xpath","//*[@id='validateCode']",u"12DB5E66249392F9392C7821A54902F8")
        dr.click("xpath","//*[@id='submitBtn']")
        time.sleep(2)
        message = dr.get_text("xpath","/html/body/div[2]/div/div[1]/h3")
        self.assertEquals("恭喜您，荣登会员！手机下单，独享特惠哦！",message,"success")

    def tearDown(self):
        pass
        # self.dr.close()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testcase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)