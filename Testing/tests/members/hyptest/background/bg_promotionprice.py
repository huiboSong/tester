# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting

class promotionprice(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)

    def test_first_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_promotionprice)

        #新增促销价规则
        dr.switch_to_frame()
        dr.click("xpath", el.bg_promotionpricebtn)
        time.sleep(3)

        #选择要编辑的款式
        dr.click("xpath", el.bg_choose_ProductStyle)
        #输入商品编码查询
        dr.send_keys("xpath", el.bg_productcode, "11074017")
        dr.click("xpath", el.bg_promotionprice_searchbtn)
        dr.click("xpath", el.bg_promotionprice_search_choose)
        #点击确认
        dr.click("xpath", el.bg_promotionprice_confirmBtn)

        #新增分站
        dr.click("xpath", el.bg_promotionprice_subsite)
        dr.click("xpath", el.bg_promotionprice_choose_subsite)

        #增加指定分站数据
        dr.click("xpath", el.bg_promotionprice_addSubsiteData)
        dr.js("$('#txt_fromTime0').val('2016-10-20 19:10')")
        dr.js("$('#txt_thruTime0').val('2016-11-20 19:10')")
        #促销价添加
        dr.send_keys("xpath", el.bg_promotionprice0, "10.10")
        dr.click("xpath", el.bg_promotionprice_checkall)

        #点击保存按钮
        dr.click("xpath", el.bg_promotionprice_save)

    def tearDown(self):
        dr = self.dr
        dr.quit()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(promotionprice)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

