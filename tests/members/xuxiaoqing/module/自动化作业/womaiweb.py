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
        time.sleep(2)
        self.dr.max_window()
        time.sleep(2)

    def test_login(self):
        dr = self.dr
        time.sleep(2)
        dr.click("xpath",el.mycount_btn)
        time.sleep(2)
        dr.switch_next_window()
        dr.send_keys("xpath",el.cartLoginId,u"testqingqing")
        dr.send_keys("xpath",el.cartPassword,u"111111qq")
        dr.click("xpath",el.login_submit_btn_real)
        time.sleep(2)
        dr.click("xpath",el.mem_left)
        dr.switch_to_frame()
        dr.send_keys("xpath",el.title,"qingqing")
        dr.click("xpath",el.userForm)
        #dr.accept_alert("确定")
        dr.switch_to_frame_out()
        message = dr.get_text("xpath",el.confirm)
        self.assertEquals(u"确",message,"success")




    def tearDown(self):
        pass
         # self.dr.close()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testcase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)