# coding=utf-8
import unittest
import time
import random

import comall
from logs.tests.members.cww_test import Login
from setting.cww_test import test_el
from setting.cww_test import setting


class CouponsTest1(unittest.TestCase):
    # 初始化方法 打开浏览器
    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)  # 打开一个浏览器 setting里设置的Driver_type
        self.dr.open(setting.login_page)
        self.dr.max_window()                          # 浏览器最大化
        time.sleep(5)
        Login.test_login(self.dr, self)                     # 调用Login中的test_login

    def test_Coupons1(self):
        ww = self.dr
        ww.click("xpath", test_el.Xpromotion)                                       # 点击促销
        ww.click("xpath", test_el.Xcoupons)                                         # 点击优惠券定义
        ww.switch_to_frame(0)                                                       # 进入frame0
        ww.click("xpath", test_el.coupons_Xadd)                                     # 点击新增按钮
        ww.click("xpath", test_el.coupons_XCommodity_coupons)                       # 1.点击商品优惠券
        ww.click("xpath", test_el.coupons_XEveryOrder)                              # 2.点击任意的订单
        ww.click("xpath", test_el.coupons_XEveryProduct)                            # 3.点击买任意的商品
        ww.click("xpath", test_el.coupons_Xunconditional)                           # 4.点击无条件
        ww.click("xpath", test_el.coupons_XreductionMoney)                          # 5.点击减商品金额
        ww.click("xpath", test_el.coupons_Xnext)                                    # 点击下一步
        ww.click("xpath", test_el.coupon_Xadd_body_text)                            # 点击文字
        ww.js('window.scrollTo(0,0);')                                              # 滚动屏frame0
        ww.switch_to_frame_out()                                                    # 退出frame
        ww.js('window.scrollTo(0,0);')
        ww.switch_to_frame(0)                                                       # 进入frame0
        ww.send_keys("xpath", test_el.coupon_Xadd_name_input, 'mainName')           # 新增-优惠券名称
        ww.send_keys("xpath", test_el.coupon_Xadd_nameEN_input, 'EnglishName')      # 新增-优惠券名称英文
        ww.send_keys("xpath", test_el.coupon_Xadd_rule_name_input, 'ruleName')      # 新增-规则名称
        ww.send_keys("xpath", test_el.coupon_Xadd_rule_nameEN_input, 'ruleEnglish') # 新增-规则名称英文
        ww.click("xpath", test_el.coupon_Xadd_startTime_show)                       # 点击选择开始时间按钮
        ww.click("xpath", test_el.coupon_Xadd_startTime_today)                      # 点击今天
        ww.click("xpath", test_el.coupon_Xadd_endTime_show)                         # 点击结束时间按钮
        ww.click("xpath", test_el.coupon_Xadd_endTime_nextM)                        # 点击下一个月
        ww.click("xpath", test_el.coupon_Xadd_endTime_day)                          # 选择结束时间-日
        ww.click("xpath", test_el.coupon_Xadd_endTime_hour)                         # 选择结束时间-时
        ww.click("xpath", test_el.coupon_Xadd_endTime_minute)                       # 选择结束时间-分
        ww.js('window.scrollTo(0,300)')                                             # 向下滑动
        ww.click("xpath", test_el.coupon_Xadd_substation)                           # 关联分站-南京-大华店
        ww.click("xpath", test_el.coupon_Xadd_substation_global)                    # 全球购台湾店
        ww.js('window.scrollTo(0,600)')                                             # 向下滑动
        ww.click("xpath", test_el.coupon_Xadd_channel)                              # 支持渠道-取消网页端
        ww.js('window.scrollTo(0,800)')                                             # 向下滑动
        ww.send_keys("xpath", test_el.coupon_Xadd_VolumeSize,  random.randint(1000, 9999))  # 生成随机四位数卷编码
        ww.send_keys("xpath", test_el.coupon_Xadd_linkAddress, test_el.coupon_Xadd_linkAddressData)  # 绑定链接地址
        ww.js('window.scrollTo(0,1200)')                                            # 向下滑动
        ww.js("$('#form_addPromotion').prop('checked',true)")                       # 点击上传图片按钮
        ww.file_upload_windows(test_el.coupon_Xadd_picAdd, ".png")                  # 上传图片
        ww.js('window.scrollTo(0,1600)')                                            # 向下滑动
        ww.send_keys("xpath", test_el.coupon_Xadd_limitMember, "3")                 # 单一会员绑定数量限制为3
        ww.send_keys("xpath", test_el.coupon_Xadd_limitOrder, "3")                  # 订单使用数量限制为3
        ww.click("xpath", test_el.coupon_Xadd_Address_tianjian)                     # 配送区域-天津
        ww.click("xpath", test_el.coupon_Xadd_Address_tianjianshi)                  # 配送区域-天津-天津市
        ww.js('window.scrollTo(0,1900)')                                            # 向下滑动
        ww.click("xpath", test_el.coupon_Xadd_tag_Promotion_price)                  # 商品标记-促销价
        ww.click("xpath", test_el.coupon_Xadd_tag_Promotion_single)                 # 单品促销标记-单品满赠赠品
        ww.click("xpath", test_el.coupon_Xadd_tag_Promotion_many)                   # 多品促销标记-多品满赠积分
        ww.click("xpath", test_el.coupon_Xadd_tag_Promotion_coupons)                # 优惠券标记-优惠券多品满减商品消费
        ww.click("xpath", test_el.coupon_Xadd_Exclusion_rules)                      # 点击排斥的规则
        ww.click("xpath", test_el.coupon_Xadd_Exclusion)                            # 排斥的规则90-55上海
        ww.click("xpath", test_el.couonn_Xadd_bodys)                                # 点击body
        ww.js('window.scrollTo(0,2200)')                                            # 向下滑动
        ww.click("xpath", test_el.coupon_Xadd_extra_btn)                            # 新增-例外的商品
        ww.click("xpath", test_el.coupon_Xadd_extra_bzfl)                           # 新增例外的商品-标准分类
        ww.click("xpath", test_el.coupon_Xadd_extra_chose)                          # 新增-选择分站
        ww.click("xpath", test_el.couonn_Xadd_extra_choseAll)                       # 新增-选择全部分站
        ww.click("xpath", test_el.couonn_Xadd_extra_choseList)                      # 新增-选择列表
        ww.js('window.scrollTo(0,2700)')
        ww.js("$('#uniform-330295029').find('input').click()")                      # 点击选择aa
        ww.click("xpath", test_el.coupon_Xadd_extra_sublime)                        # 确定选择的例外商品
        # ww.js("$('#selException1').parent().prop('class','checked')")
        ww.click("xpath", test_el.coupon_Xadd_RewardButton)                         # 新增一条奖励
        ww.click("xpath", test_el.coupon_Xadd_Rewards)                              # 新增-范围内奖励
        ww.send_keys("xpath", test_el.coupon_Xadd_startCount1, "2")                 # 输入范围2-
        ww.send_keys("xpath", test_el.coupon_Xadd_upperCount1,  "50")               # 输入范围-50
        ww.send_keys("xpath", test_el.coupon_Xadd_RewardValue, "50")                # 输入奖励金额 50
        ww.click("xpath", test_el.coupon_Xadd_statusButton)                         # 点击启用
        ww.send_keys("xpath", test_el.coupon_Xadd_remark, "lalala")                 # 输入备注
        ww.js('window.scrollTo(0,2900)')
        ww.send_keys("xpath", test_el.coupon_Xadd_detailsChinese, "lalala")         # 输入规则说明（中文）
        ww.send_keys("xpath", test_el.coupon_Xadd_detailsEnglish, "lalala")         # 输入规则说明（英文）
        ww.click("xpath", test_el.coupon_Xadd_sublime)                              # 点击提交
        time.sleep(5)
        # ww.click("xpath", "")
        ww.js('window.scrollTo(0,-1000)')                                           # 退出+滑动
        ww.switch_to_frame_out()
        ww.js('window.scrollTo(0,-1000)')
        time.sleep(5)
        # 搜索验证
        ww.switch_to_frame(0)
        ww.send_keys("xpath", test_el.coupon_Xadd_searchInput, "rule")             # 输入名称rule
        time.sleep(5)
        ww.click("xpath", test_el.coupon_Xadd_searchButton)                        # 点击搜索
        time.sleep(5)

    def tearDown(self):
        self.dr.close()
        pass

