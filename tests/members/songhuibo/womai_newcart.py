# coding=utf-8
import unittest
# 引入主框架文件
import time
import testgo
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.songhuibo import el
from setting.songhuibo import setting
from setting.songhuibo.data import TestData as dt
import time

class TestCase(unittest.TestCase):
    def setUp(self):
        # 启动浏览器
        self.dr = testgo.Hooli("chrome")
        self.dr.open(setting.womai_url)
        self.dr.max_window()
        time.sleep(3)

    def test_order(self):
        dr = self.dr
        dr.js("window.scrollTo(0,500)")
        dr.click("xpath", el.womai_productinfo)
        dr.switch_next_window()
        time.sleep(3)
        #dr.until_page_load()
        dr.click("xpath",el.womai_span_add)
        time.sleep(2)
        dr.click("xpath",el.womai_span_delete)
        dr.click("xpath", el.womai_newcart)
        #self.assertEqual()
        time.sleep(2)
        dr.click("xpath",el.womai_showIncludeCart)
        time.sleep(3)
        dr.click("xapth",el.womai_checkout)
        time.sleep(3)
        dr.switch_to_frame(self,4)
        dr.click("xapth","/html/body/div/div[1]/div[2]/ul/li[1]")
        dr.send_keys("xapth",el.womai_username,"13520843514")
        dr.send_keys("xapth",el.womai_cartpassword,"123456qq")
        dr.click("xapth",el.womai_login_submit)
        dr.click("xapth",el.womai_checkout)
        dr.js("window.scrollTo(0,500)")
        dr.click("xatph","//*[@id='nextStep']")
        dr.click("xapth","//*[@id='submitOrder']")

    # def test_jd(self):
    #     dr = self.dr
    #     time.sleep(3)
    #     dr.switch_next_window()
    #     dr.js(200,0)
    #     dr.click("xapth",el.jd_shortcut)
    #     dr.click("xapth",el.jd_login)
    #     time.sleep(3)
    #     dr.click("xapth",el.jd_content)
    #     dr.send_keys("xapth",el.jd_loginname,"13520843514")
    #     dr.send_keys("xapth",el.jd_nloginpwd,"songbo1220")
    #     dr.click("xapth",el.jd_loginsubmit)
    #     dr.click("xpath",el.jd_productlist)
    #     dr.switch_next_window()
    #     打开一个新窗口
    #     dr.js("window.scrollTo(0,200)")
    #     处理滚动条
    #     dr.click("xpath",el.jd_productinfo)
    #     dr.switch_next_window()
    #     time.sleep(3)
    #     dr.click("xpath",el.jd_add_choose)
    #     dr.click("id","choose-btns")
    #     time.sleep(3)
    #     dr.click("xpath",el.jd_delete_choose)
    #     dr.click("xpath",el.jd_newcard)
    #     dr.click("id","InitCartUrl")
    #
    #
    # def test_baidu(self):
    #     dr =  self.dr
    #     dr.click("xpath",el.baidu_ceshi)
    #     dr.send_keys("xpath","//*[@id='kw']",u"宋慧波")
    #     dr.click("id","su")
    #
    # def tearDown(self):
    #     pass
    #     self.dr.close()
    #$("iframe")(找网站iframe)

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)