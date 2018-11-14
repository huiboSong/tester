# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting

class panicbuying(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)

    def test_first_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_panicbuying)

        #新增促销价规则
        dr.switch_to_frame()
        dr.click("xpath", el.bg_panicbuying_newbtn)
        #规则名称
        dr.send_keys("xpath", el.bg_panicbuying_nameZn, u"自动化测试抢购")
        #规则名称(英)
        dr.send_keys("xpath", el.bg_panicbuying_nameEN, "panicbuyingtest")
        #限购方式
        dr.click("xpath", el.bg_panicbuying_protype)
        dr.click("xpath", el.bg_panicbuying_protypemore)
        dr.click("xpath", el.bg_panicbuying_promode)
        dr.click("xpath", el.bg_panicbuying_promode2)
        #件数
        dr.send_keys("xpath", el.bg_panicbuying_limitnum, "1")
        #开始时间
        dr.js("$('#txt_fromTime').attr('value', '2016-10-15 00:00:00')")
        dr.js("$('#hid_fromTime').val('2016-10-15 00:00:00')")
        #结束时间
        dr.js("$('#txt_thruTime').attr('value', '2016-11-15 00:00:00')")
        dr.js("$('#hid_thruTime').val('2016-11-15 00:00))')")

        #点击选择抢购款式
        dr.click("xpath", el.bg_panicbuying_prostyle)
        #输入商品名称
        dr.send_keys("xpath", el.bg_panicbuying_proname, u"赫凡赛城堡红葡萄酒")
        #筛选
        dr.click("xpath", el.bg_panicbuying_searchbtn)
        time.sleep(3)
        #勾选商品
        #dr.js("$('[value=赫凡赛城堡红葡萄酒]').parent().attr('class', 'checked')")
        dr.js("$('[value=赫凡赛城堡红葡萄酒]').prop('checked', 'checked')")
        #点击确定
        dr.click("xpath", el.bg_panicbuying_comfirebtn)

        #选择分站
        dr.click("xpath", el.bg_panicbuying_subsite)
        dr.click("xpath", el.bg_panicbuying_subsite0)
        #选择商品
        dr.click("xpath", el.bg_panicbuying_barcode)
        dr.click("xpath", el.bg_panicbuying_barcode0)
        #点击生成抢购货品数据按钮
        dr.click("xpath", el.bg_panicbuying_add)

        #抢购价
        dr.send_keys("xpath", el.bg_panicbuying_limitprice0, "0.01")
        #抢购数量调整
        dr.send_keys("xpath", el.bg_panicbuying_changestock, "10")
        #勾选启用
        dr.click("xpath", el.bg_panicbuying_status)

        #提交
        dr.click("xpath", el.bg_panicbuying_save)

    def tearDown(self):
        dr = self.dr
        dr.quit()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(panicbuying)
    result = unittest.TextTestRunner(verbosity=2).run(suite)







