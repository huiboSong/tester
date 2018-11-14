#coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting

class couponbatch(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)

    def test_first_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_couponbatch)

        #新增
        dr.switch_to_frame()
        dr.click("xpath", el.bg_couponbatch_add)

        #选择优惠券
        dr.click("xpath", el.bg_couponbatch_sel)
        #输入优惠券名称
        dr.send_keys("xpath", el.bg_couponbatch_searchcontent, u"自动化测试优惠券")
        #搜索按钮
        dr.click("xpath", el.bg_couponbatch_searchbtn)
        #选择优惠券
        dr.click("xpath", el.bg_couponbatch_choose)
        #点击确认
        dr.click("xpath", el.bg_couponbatch_confirmbtn)
        #输入数量
        dr.send_keys("xpath", el.bg_couponbatch_num, "100")
        #是否排队-选择是
        dr.click("xpath", el.bg_couponbatch_queue)
        time.sleep(1)
        #是否插队-选择是
        dr.click("xpath", el.bg_couponbatch_cuttingsign)
        #保存
        dr.click("xpath", el.bg_couponbatch_save)

    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(couponbatch)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

