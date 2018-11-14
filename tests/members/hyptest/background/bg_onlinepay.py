# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting

class onlinepay(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)

    def test_first_case(self):
        dr = self.dr
        #点击列表左侧-网站
        dr.click("xpath", el.bg_website)
        time.sleep(1)
        dr.click("xpath", el.bg_onlinepay)
        # #划到页面底部
        # dr.js('document.body.scrollTop=100000')
        # #点击准时达服务管理
        # time.sleep(3)
        # dr.click("xpath", el.bg_onlinepay)
        #dr.js('document.body.scrollDown=100000')
        # 点击新增按钮
        dr.switch_to_frame()
        dr.until("xpath", el.bg_addDeliveryOntimeServer)
        time.sleep(3)
        dr.click("xpath", el.bg_addDeliveryOntimeServer)
        #基础信息设置-规则名称
        time.sleep(3)
        dr.until("xpath", el.bg_txt_name)
        dr.send_keys("xpath", el.bg_txt_name, u"成都站准时达")
        #基础信息设置-生效分站
        dr.until("xpath", el.bg_Substation)
        dr.click("xpath", el.bg_Substation)
        dr.click("xpath", el.bg_choose_substation)
        #基础信息设置-配送方案
        dr.until("xpath", el.bg_Distribution_mode)
        dr.click("xpath", el.bg_Distribution_mode)
        dr.click("xpath", el.bg_choose_mode)
        #基础信息设置-选择区域
        dr.click("xpath", el.bg_choose_place)
        dr.click("xpath", el.bg_choose_place2)
        #基础信息设置-选择可预约天数
        dr.until("xpath", el.bg_txt_availableDay)
        dr.send_keys("xpath", el.bg_txt_availableDay, "8")
        #基础信息设置-点击禁用
        dr.click("xpath", el.bg_disable)
        #基础信息设置-点击下一步
        dr.click("xpath", el.bg_next_step)
        #可预约时间段设置-点击新增可预约时间按钮(0:00~12:00)
        dr.switch_to_frame_out()
        dr.js('window.scrollTo(0,0);')
        dr.switch_to_frame()
        dr.click("xpath", el.bg_addItem2)
        #可预约时间段设置-点击新增可预约时间段
        dr.click("xpath", el.bg_fromtime)
        dr.click("xpath", el.bg_time1)
        #可预约时间段设置-点击增加预约截止时间
        dr.click("xpath", el.bg_endtime)
        dr.click("xpath", el.bg_time3)
        #可预约时间段设置-增加周内可预约最大数
        dr.send_keys("xpath", el.bg_delivernum, "88")
        #dr.js("$(\"#txt_deliveryNumber1\")[0].value = 555")
        #可预约时间段设置-增加周末可预约最大数
        dr.send_keys("xpath", el.bg_delivernum2, "123")
        #dr.js("$(\"#txt_weekendNumber1\")[0].value = 123")
        #可预约时间段设置-服务费
        dr.send_keys("xpath", el.bg_fee, "2")
        #可预约时间段设置-点击新增可预约时间按钮(12:00~24:00)
        dr.click("xpath", el.bg_addItem2)
        #可预约时间段设置-点击新增可预约时间段
        dr.click("xpath", el.bg_fromtime2)
        dr.click("xpath", el.bg_time4)
        #可预约时间段设置-点击增加预约截止时间
        dr.click("xpath", el.bg_endtime2)
        dr.click("xpath", el.bg_time5)
        #可预约时间段设置-增加周内可预约最大数
        dr.send_keys("xpath", el.bg_delivernum3, "77")
        #dr.js("$(\"#txt_deliveryNumber1\")[0].value = 555")
        #可预约时间段设置-增加周末可预约最大数
        dr.send_keys("xpath", el.bg_delivernum4, "66")
        #dr.js("$(\"#txt_weekendNumber1\")[0].value = 123")
        #可预约时间段设置-服务费
        dr.send_keys("xpath", el.bg_fee2, "1")
        #可预约时间段设置-下一步
        dr.click("xpath", el.bg_next_step2)
        #特殊节假日设置--新增按钮
        dr.click("xpath", el.bg_addHoliday)
        #特殊节假日设置-选择开始日期
        time.sleep(3)
        dr.click("xpath", el.bg_holiday_from)
        dr.js("$('.bootstrap-dialog-message').find('#holiday_from').val('2016-09-30')")
        #dr.click("xpath", el.bg_beginday)
        #特殊节假日设置-选择结束日期
        dr.click("xpath", el.bg_holiday_end)
        #dr.click("xpath", el.bg_next_month)
        dr.js("$('.bootstrap-dialog-message').find('#holiday_end').val('2016-10-30')")
        #dr.click("xpath", el.bg_endday)
        #特殊节假日-可预约最大量(单)/服务费(元)
        dr.send_keys("xpath", el.bg_maxnum1, "33")
        dr.send_keys("xpath", el.bg_special_fee1, "0")
        #特殊节假日-可预约最大量(单)/服务费(元)
        dr.send_keys("xpath", el.bg_maxnum2, "44")
        dr.send_keys("xpath", el.bg_special_fee2, "10")
        #特殊节假日-点击确认按钮
        dr.click("xpath", el.bg_special_sure)
        #特殊节假日设置-下一步
        time.sleep(3)
        dr.click("xpath", el.bg_next_step3)
        #预约规则设置-新增规则按钮(00:00~12:00下单)
        dr.until("xpath", el.bg_add_timeset)
        dr.click("xpath", el.bg_add_timeset)
        #预约规则设置-下单开始时间
        dr.click("xpath", el.bg_order_begin)
        dr.click("xpath", el.bg_begin1)
        dr.click("xpath", el.bg_begin2)
        #预约规则设置-下单截止时间
        dr.click("xpath", el.bg_order_end)
        dr.click("xpath", el.bg_end1)
        dr.click("xpath", el.bg_end2)
        #预约规则设置-新增规则按钮(12:00~24:00下单)
        dr.until("xpath", el.bg_add_timeset)
        dr.click("xpath", el.bg_add_timeset)
        #预约规则设置-下单开始时间
        dr.click("xpath", el.bg_order_begin2)
        dr.click("xpath", el.bg_begin3)
        dr.click("xpath", el.bg_begin4)
        #预约规则设置-下单截止时间
        dr.click("xpath", el.bg_order_end2)
        dr.click("xpath", el.bg_end3)
        dr.click("xpath", el.bg_end4)
        #设置第N天
        dr.send_keys("xpath", el.bg_delayday, "2")
        #最早可预约时间
        dr.click("xpath", el.bg_choose_timeset)
        time.sleep(1)
        dr.click("xpath", el.bg_choose_timeset2)
        #预约规则设置-点击提交
        dr.click("xpath", el.bg_submit)
        #筛选功能
        dr.send_keys("xpath", el.bg_search, u"成都站准时达")
        #点击搜索按钮
        dr.click("xpath", el.bg_search_btn)
        #启用上面生成的规则
        time.sleep(3)
        dr.click("xpath", el.bg_up_btn)
        #确认启用准时
        dr.click("xpath", el.bg_sure)
        #复制规则
        time.sleep(3)
        dr.click("xpath", el.bg_copy)
        dr.click("xpath", el.bg_copy_sure)


    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(onlinepay)
    result = unittest.TextTestRunner(verbosity=2).run(suite)



