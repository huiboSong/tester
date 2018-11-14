# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting
from setting.hyptest.data_register import TestData
from ddt import ddt, data, unpack

@ddt
class selfpick(unittest.TestCase):

    d = TestData().get("selfpick_success")
    time1 = time.strftime("%d%H%M%S")
    print time1

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)

    @data(d[0],d[1],d[2],d[3])
    @unpack
    def test_first_case(self,name_ch,name_En,order):
        dr = self.dr
        dr.click("xpath", el.bg_website)
        time.sleep(3)
        dr.click("xpath", el.bg_selfpick)

        dr.switch_to_frame()
        #新增
        dr.click("xpath", el.bg_cpupon_new)
        time.sleep(3)
        #选择自提点分站
        dr.click("xpath", el.bg_selfpick_subsite)
        #选择古北店
        dr.click("xpath", el.bg_selfpick_subsite1)
        #选择一级地址
        dr.click("xpath", el.bg_selfpick_region_1)
        #选择上海
        dr.click("xpath", el.bg_selfpick_region_1_1)
        #选择二级地址
        dr.click("xpath", el.bg_selfpick_region_2)
        #选择上海市
        dr.click("xpath", el.bg_selfpick_region_2_1)
        #选择三级地址
        dr.click("xpath", el.bg_selfpick_region_3)
        #选择长宁区
        dr.click("xpath", el.bg_selfpick_region_3_1)
        #选择四级地址
        dr.click("xpath", el.bg_selfpick_region_4)
        #选择-周家桥街道
        dr.click("xpath", el.bg_selfpick_region_4_1)
        #自提点详细地址(中文)
        dr.send_keys("xpath", el.bg_selfpick_detailed_address_ch, u"[自提]品尊国际大厦 999号")
        #自提点详细地址(英文)
        dr.send_keys("xpath", el.bg_selfpick_detailed_address_En, "[Easy]PinZhunInternational dasha No.999")
        #自提点名称(中文)
        dr.send_keys("xpath", el.bg_selfpick_detailed_name_ch, name_ch + str(self.time1))
        #自提点名称(英文)
        dr.send_keys("xpath", el.bg_selfpick_detailed_name_En, name_En + str(self.time1))
        #自提柜数量
        dr.send_keys("xpath", el.bg_selfpick_detailed_num, "10")
        #排序
        dr.send_keys("xpath", el.bg_selfpick_detailed_order, order)
        #支持配送区域
        dr.js("$('#_selectedRegions').val('250004532,250004524,250004523,250004520,646,250000018,250000019,')")
        #负责人手机号
        dr.send_keys("xpath", el.bg_selfpick_per_num, "13488885205")
        #负责人邮箱
        dr.send_keys("xpath", el.bg_selfpick_per_email, "914446879@qq.com")
        #勾选准时达
        dr.click("xpath", el.bg_selfpick_online)
        #点击提交按钮
        dr.click("xpath", el.bg_selfpick_submit)

    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(selfpick)
    result = unittest.TextTestRunner(verbosity=2).run(suite)




