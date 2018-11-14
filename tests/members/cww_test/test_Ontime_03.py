# coding=utf-8
import unittest
import time

import comall
from logs.tests.members.cww_test import Login
from setting.cww_test import test_el
from setting.cww_test import setting


class OntimeTest(unittest.TestCase):

    # 初始化方法 打开浏览器
    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)                          # 打开一个浏览器 setting里设置的Driver_type
        self.dr.open(setting.login_page)
        self.dr.max_window()                                                  # 浏览器最大化
        time.sleep(5)
        Login.test_login(self.dr, self)                                       # 调用Login中的test_login

    def test_Otime(self):
        ww = self.dr
        ww.click("xpath", test_el.XsubMenu)                                    # 点击网站
        ww.move_to_element("xpath", test_el.XsubMenu)
        time.sleep(5)

        ww.click("xpath", test_el.Xontime)                                     # 点击准时达
        ww.switch_to_frame(0)

        time.sleep(5)
        ww.click("xpath", test_el.XaddDeliveryOntimeServer)                    # 点击新增准时达按钮
        ww.send_keys("xpath", test_el.ontime_Xadd_baseinfo_name,  u"输入规则")   # 输入规则名称
        ww.click("xpath", test_el.ontime_Xadd_baseinfo_subsite_select_show)    # 展示生效分站
        ww.click("xpath", test_el.ontime_Xadd_baseinfo_subsite_select)         # 生效分站-选择
        time.sleep(2)
        ww.click("xpath", test_el.ontime_Xadd_baseinfo_provide_type_show)      # 展示配送方式
        ww.click("xpath", test_el.ontime_Xadd_baseinfo_provide_type_select_first)     # 选择第一个配送方式A
        time.sleep(2)
        ww.move_to_element("xpath", test_el.ontime_Xadd_baseinfo_area_select_chengdu)
        ww.click("xpath", test_el.ontime_Xadd_baseinfo_area_select_chengdu)    # 配送区域选择成都
        ww.click("xpath", test_el.ontime_Xadd_baseinfo_area_select_chengdu_chengducity)    # 配送区域-成都-成都市

        ww.click("xpath", test_el.ontime_Xadd_baseinfo_area_select_chengdu_chengducity_4)  # 配送区域-成都-成都市-测试四
        ww.js('window.scrollTo(800,800);')
        ww.send_keys("xpath", test_el.ontime_Xadd_baseinfo_availableDay, 10)     # 可预约天数输入3
        ww.click("xpath", test_el.ontime_Xadd_next_step_btn)                    # 下一步
        ww.js('window.scrollTo(0, -300)')
        ww.click("xpath", test_el.ontime_Xadd_timeset_Xadd_btn)                 # 可预约时间段设置-新增按钮
        ww.click("xpath", test_el.ontime_Xadd_timeset_timestart_show)           # 点击预约时间开始按钮
        ww.click("xpath", test_el.ontime_Xadd_timeset_timestart_select)         # 点击7.31-08:00
        ww.click("xpath", test_el.ontime_Xadd_timeset_timeend_show)             # 点击预约结束时间按钮
        ww.click("xpath", test_el.ontime_Xadd_timeset_timeend_select)           # 点击7.31-23:00
        ww.send_keys("xpath", test_el.ontime_Xadd_timeset_num_input, 5)         # 输入周内可预约最大值（周一至周五）5
        ww.send_keys("xpath", test_el.ontime_Xadd_timeset_num_weekend_input, 15)  # 输入周末可预约最大值（周六日）15
        ww.send_keys("xpath", test_el.ontime_Xadd_timeset_price_input, 30)      # 输入服务费 30
        ww.click("xpath", test_el.ontime_Xadd_next_step1)                       # 点击下一步
        #  新增节假日
        # ww.switch_to_frame_out()
        # ww.js('window.scrollTo(0, -300)')
        # ww.switch_to_frame(0)
        # time.sleep(3)

        ww.click("xpath", "//*[@id='btn_addHoliday']")  # 新增
        time.sleep(3)

        # tc=ww.get_element('xpath','//*[@id="pnl_tabContent"]')
        # iframe=tc.find_elements_by_tag_name('iframe')[0]

        # time.sleep(3)

        # ww.click('xpath','//*[@id="div_holidaystatus"]/button[2]')
        tw=ww.get_elements('xpath','//*[@id="frm_holiday"]/div[1]/div[1]')[1].click()

        # ww.click('xpath','//*[@id="frm_holiday"]/div[1]/div[1]')
        #ww.click('xpath','/html/body/div[5]/div[3]/table/tbody/tr[2]/td[4]')

        # ww.click('xpath','//*[@id="frm_holiday"]/div[1]/div[1]')
        # ww.click('xpath','/html/body/div[5]/div[3]/table/tbody/tr[2]/td[4]')



        # ww.js("$('#holiday_from1').attr('value','2017-08-01')")
        # time.sleep(3)
        # ww.js("$('.datetimepicker').attr('style', 'display:none')")
        # time.sleep(3)
        # ww.click("xpath", "//*[@id='holiday_end']")
        # time.sleep(3)
        # ww.js("$('#holiday_end').attr('value','2017-08-02')")
        # time.sleep(3)
        # ww.js("$('.datetimepicker').attr('style', 'display:none')")
        # time.sleep(3)

        ww.click("xpath", "//*[@id='7b4fc7db-2066-4012-8cb4-645e58a3c6ab']")

        # ww.click("xpath", "/html/body/div[6]/div[3]/table/tfoot/tr/th")
        # ww.click("xpath", "//*[@id='div_holidaystatus']/button[1]")
        # ww.click("xpath", "//*[@id='txt_holiday_num0']")
        # ww.click("xpath", "//*[@id='txt_holiday_serverFee0']")
        # ww.click("xpath", "//*[@id='2d1a0450-38f4-48b7-99d7-6c014f676e38']")

        ww.click("xpath", test_el.ontime_Xadd_next_step2)                      # 点击下一步
        ww.click("xpath", test_el.ontime_Xadd_timeset_btn)                     # 点击新增规则
        ww.click("xpath", test_el.ontime_Xadd_orderStartTime)                  # 点击下单开始时间
        ww.click("xpath", test_el.ontime_Xadd_orderStartTime_hours)            # 点击0时
        ww.click("xpath", test_el.ontime_Xadd_orderStartTime_minutes)          # 点击7.31-00:00
        ww.click("xpath", test_el.ontime_Xadd_orderEndTime)                    # 点击下单截止时间
        ww.click("xpath", test_el.ontime_Xadd_orderEndTime_nextday)            # 点击下一天
        ww.click("xpath", test_el.ontime_Xadd_orderEndTime_hours)              # 点击下一天11点
        ww.click("xpath", test_el.ontime_Xadd_orderEndTime_minutes)            # 点击08/01-11：59
        ww.js('window.scrollTo(0,800);')
        ww.click("xpath", test_el.ontime_Xadd_info_sublime)                    # 点击提交
        time.sleep(5)
        # 搜索验证
        ww.js('window.scrollTo(0,-1000)')                                      # 退出+滑动
        ww.switch_to_frame_out()
        ww.js('window.scrollTo(0,-1000)')
        time.sleep(5)
        ww.switch_to_frame(0)
        ww.send_keys("xpath", test_el.ontime_Xadd_search_input, u"输入规则")     # 输入名称-输入规则
        time.sleep(5)
        ww.click("xpath", test_el.ontime_Xadd_search_btn)                       # 点击搜索
        time.sleep(5)

    def tearDown(self):
        # self.dr.close()
        pass