# coding=utf-8
import unittest
# 引入主框架文件
import comall
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.xuxiaoqing import el
from setting.xuxiaoqing import setting
from setting.xuxiaoqing.data import TestData as dt
import time

class TestCase(unittest.TestCase):
    #谷歌打开淘宝
    def setUp(self):
        # 启动浏览器
        self.dr = comall.Comall("chrome")
        #打开我买网
        self.dr.open(setting.web_url)
        #窗口最大化
        self.dr.max_window()

    def test_tt(self):
        dr = self.dr
        # dr.click("xpath", el.womai_index_topbtn_login_a)
        dr.send_keys("xpath", "//*[@id='topKeywords']", u"方便面")
        dr.click("xpath", "//*[@id='searchform']/div/div[1]/div[2]/button")
        first_name = dr.get_text("xpath", "//*[@id='_gatrack_productlist_listtitle_501498']/p/a")
        self.assertEqual("方便面", first_name, "搜对了")

    def tearDown(self):
        pass
        #self.dr.close()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)