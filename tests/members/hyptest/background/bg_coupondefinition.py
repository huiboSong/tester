# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common
import random

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting

class coupondefinition(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)

    def test_first_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_website)
        time.sleep(3)
        dr.click("xpath", el.bg_coupondef)

        dr.switch_to_frame()
        #点击新增按钮
        dr.click("xpath", el.bg_coupondef_addbtn)
        time.sleep(3)
        #优惠券类型
        dr.click("xpath", el.bg_coupontype1)
        #结算条件
        dr.click("xpath", el.bg_coupondef_checkouttype1)
        #商品类型
        dr.click("xpath", el.bg_coupondef_producttype1)
        #条件类型
        dr.click("xpath", el.bg_coupondef_conditiontype1)
        #奖励类型
        dr.click("xpath", el.bg_coupondef_awardtype1)
        #下一步
        dr.click("xpath", el.bg_coupondef_gotoadd)

        #优惠券名称
        dr.send_keys("xpath", el.bg_coupondef_nameCh, u"自动化测试优惠券")
        #优惠券名称英文
        dr.send_keys("xpath", el.bg_coupondef_nameEn, "testcoupondef")
        #规则名称
        dr.send_keys("xpath", el.bg_coupondef_ruleCh, u"自动化测试优惠券")
        #规则名称英文
        dr.send_keys("xpath", el.bg_coupondef_ruleEn, "testcoupondef")
        #开始时间
        dr.js("$('#txt_fromTime').val('2016-10-18 00:00:00')")
        dr.js("$('#hid_fromTime').val('2016-10-18 00:00:00')")
        #结束时间
        dr.js("$('#txt_thruTime').val('2016-11-18 00:00:00')")
        dr.js("$('#hid_thruTime').val('2016-11-18 00:00:00')")

        #选择分站(class是修改样式)
        #成都
        dr.js("$('#ztree_5_check').click()")
        #选择全渠道
        dr.js("$('#selectedAllChannels').parent().attr('class', 'checked')")

        #随机选取1000到9999
        val = random.randint(1000, 9999)
        print val
        #输入券编码
        dr.send_keys("xpath", el.bg_coupondef_batchNo, val)
        #点击旁白
        dr.click_body()
        #限制会员绑定数量
        dr.send_keys("xpath", el.bg_coupondef_memberLimitQuantity, "5")
        #限制会员使用数量
        dr.send_keys("xpath", el.bg_coupondef_orderLimitQuantity, "2")

        #选中条件标记
        dr.click("xpath", el.bg_coupondef_MarktypePro1)
        dr.click("xpath", el.bg_coupondef_MarktypePro2)
        dr.click("xpath", el.bg_coupondef_Marktypesingle1)
        dr.click("xpath", el.bg_coupondef_Marktypesingle2)
        dr.click("xpath", el.bg_coupondef_Marktypesingle3)
        dr.click("xpath", el.bg_coupondef_Marktypesingle4)
        dr.click("xpath", el.bg_coupondef_Marktypesingle5)
        dr.click("xpath", el.bg_coupondef_Marktypesingle6)
        dr.click("xpath", el.bg_coupondef_Marktypesingle7)
        dr.click("xpath", el.bg_coupondef_Marktypemulti1)
        dr.click("xpath", el.bg_coupondef_Marktypemulti2)
        dr.click("xpath", el.bg_coupondef_Marktypemulti3)
        dr.click("xpath", el.bg_coupondef_Marktypemulti4)
        dr.click("xpath", el.bg_coupondef_Marktypemulti5)
        dr.click("xpath", el.bg_coupondef_Marktypemulti6)
        dr.click("xpath", el.bg_coupondef_Marktypecoupon1)
        dr.click("xpath", el.bg_coupondef_Marktypecoupon2)
        dr.click("xpath", el.bg_coupondef_Marktypecoupon3)

        #奖励
        dr.click("xpath", el.bg_coupondef_addreward)
        dr.click("xpath", el.bg_coupondef_addreward2)
        time.sleep(1)
        dr.send_keys("xpath", el.bg_coupondef_startcount1, "10")
        dr.send_keys("xpath", el.bg_coupondef_rewardValue1, "5")

        #提交
        dr.click("xpath", el.bg_coupondef_submitbtn)

        #返回列表页
        time.sleep(3)
        dr.switch_to_frame_out()
        dr.js('window.scrollTo(0,0);')
        dr.switch_to_frame()

        #点击搜索
        dr.click("xpath", el.bg_coupondef_search)
        dr.send_keys("xpath", el.bg_coupondef_search, u"自动化测试优惠券")
        dr.click("xpath", el.bg_coupondef_searchbtn)
        time.sleep(1)
        #点击编辑
        dr.click("xpath", el.bg_coupondef_edit)

        time.sleep(3)
        #关联分站增加北京
        dr.js("$('#ztree_4_check').click()")
        #提交
        dr.click("xpath", el.bg_coupondef_submitbtn)


    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(coupondefinition)
    result = unittest.TextTestRunner(verbosity=2).run(suite)




