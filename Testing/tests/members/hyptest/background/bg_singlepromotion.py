# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting

class singlepromotion(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)

    #买任意商品-无条件-赠赠品
    def test_first_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(5)
        #dr.click("xpath", el.bg_protuctType1)
        dr.js("$('#productType0').parent().prop('class','checked')")
        #条件类型
        #dr.click("xpath", el.bg_conditionType1)
        dr.js("$('#conditionType1').parent().prop('class','checked')")
        #奖励类型
        #dr.click("xpath", el.bg_awardType1)
        dr.js("$('#awardType1').parent().prop('class','checked')")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买任意商品-无条件-赠赠品")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion1")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "1452")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)
        #输入赠品数量
        dr.send_keys("xpath", el.bg_gift_num, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_selectbtn)
        #输入赠品名称
        dr.send_keys("xpath", el.bg_single_gift_name, u"亮碟洗碗机专用洗涤块（自动化误动）")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_gift_btn)
        #选择赠品
        dr.js("$('#uniform-250122220').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_surebtn)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买任意商品-金额满-选加价购
    def test_second_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(5)
        dr.js("$('#productType0').parent().prop('class','checked')")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#awardType2').parent().attr('class','checked')")
        dr.js("$('#awardType2').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中选加价购
        dr.js("$('#conditionType2').parent().attr('class','checked')")
        dr.js("$('#conditionType2').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买任意商品-金额满-选加价购")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion2")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9995")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始金额
        dr.send_keys("xpath", el.bg_single_startCount1, "0")
        #输入结束金额
        dr.send_keys("xpath", el.bg_single_upperCount1, "100")
        #输入加价购数量
        dr.send_keys("xpath", el.bg_single_rewardValue1, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_addPriceTab1)
        #输入加价购商品名称
        dr.send_keys("xpath", el.bg_single_searchContent1, u"百威啤酒500ml 罐装")
        #点击搜索
        dr.click("xpath", el.bg_single_searchContent1_btn)
        #选择加价购
        time.sleep(3)
        dr.js("$('#uniform-250000214').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_addPriceTab1_confirmBtn)
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围金额
        dr.send_keys("xpath", el.bg_single_startCount2, "100")
        #输入加价购数量
        dr.send_keys("xpath", el.bg_single_rewardValue2, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_addPriceTab2)
        #输入加价购商品名称
        dr.send_keys("xpath", el.bg_single_searchContent2, u"汇源1L100%橙汁")
        #点击搜索
        dr.click("xpath", el.bg_single_searchContent2_btn)
        #选择加价购
        time.sleep(3)
        dr.js("$('#uniform-250000216').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_addPriceTab2_confirmBtn)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买任意商品-重量满-赠优惠券
    def test_third_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(5)
        dr.js("$('#productType0').parent().prop('class','checked')")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中重量满
        dr.js("$('#awardType3').parent().attr('class','checked')")
        dr.js("$('#awardType3').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中赠优惠券
        dr.js("$('#conditionType3').parent().attr('class','checked')")
        dr.js("$('#conditionType3').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买任意商品-重量满-赠优惠券")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion3")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9996")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_Coupon_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_coupon_assreward)
        #输入超范围重量
        dr.send_keys("xpath", el.bg_single_coupon_startCount1, "2000")
        #点击选择优惠券框
        dr.click("xpath", el.bg_single_select_coupon)
        #选择第一个优惠券
        dr.js("$('#uniform-250122220').find('input').click()")
        dr.click("xpath", el.bg_single_coupon1)
        dr.click_body()
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #指定标准分类-金额满-赠赠品
    def test_four_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #商品类型
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定标准品类商品
        dr.js("$('#productType1').parent().attr('class','checked')")
        dr.js("$('#productType1').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#conditionType2').parent().attr('class','checked')")
        dr.js("$('#conditionType2').prop('checked',true)")
        #奖励类型
        dr.js("$('#awardType1').parent().prop('class','checked')")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"指定标准分类-金额满-赠赠品")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion4")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9994")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #标准分类列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_category)
        #输入标准名称
        dr.send_keys("xpath", el.bg_single_category_search, u"家用电器")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_category_btn)
        #选中品牌
        dr.js("$('#uniform-250020986').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_category_confirmBtn)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始件数
        dr.send_keys("xpath", el.bg_single_startCount1, "1")
        #输入结束件数
        dr.send_keys("xpath", el.bg_single_upperCount1, "5")
        #输入赠品数量
        dr.send_keys("xpath", el.bg_single_rewardValue1, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_gift_addPriceTab1)
        #输入赠品商品名称
        dr.send_keys("xpath", el.bg_single_gift_content1, u"亮碟洗碗机专用洗涤块（自动化误动）")
        #点击搜索
        dr.click("xpath", el.bg_single_gift_search_btn1)
        #选择赠品
        time.sleep(3)
        dr.js("$('#uniform-250122220').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_gift_search_confirmbtn1)
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围数量
        dr.send_keys("xpath", el.bg_single_startCount2, "5")
        #输入
        dr.send_keys("xpath", el.bg_single_rewardValue2, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_gift_addPriceTab2)
        #输入赠品商品名称
        dr.send_keys("xpath", el.bg_single_gift_content2, u"麒麟法式香草风味咖啡")
        #点击搜索
        dr.click("xpath", el.bg_single_gift_search_btn2)
        #选择赠品
        time.sleep(3)
        dr.js("$('#uniform-250120218').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_gift_search_confirmbtn2)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #指定标准分类-重量满-选加价购
    def test_five_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #商品类型
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定标准品类商品
        dr.js("$('#productType1').parent().attr('class','checked')")
        dr.js("$('#productType1').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中重量满
        dr.js("$('#conditionType3').parent().attr('class','checked')")
        dr.js("$('#conditionType3').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选择加价购
        dr.js("$('#awardType2').parent().attr('class','checked')")
        dr.js("$('#awardType2').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"指定标准分类-重量满-选加价购")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion5")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9986")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #标准分类列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_category)
        #输入标准名称
        dr.send_keys("xpath", el.bg_single_category_search, u"家用电器")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_category_btn)
        #选中品牌
        dr.js("$('#uniform-250020986').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_category_confirmBtn)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始金额
        dr.send_keys("xpath", el.bg_single_startCount1, "0")
        #输入结束金额
        dr.send_keys("xpath", el.bg_single_upperCount1, "100")
        #输入加价购数量
        dr.send_keys("xpath", el.bg_single_rewardValue1, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_addPriceTab1)
        #输入加价购商品名称
        dr.send_keys("xpath", el.bg_single_searchContent1, u"百威啤酒500ml 罐装")
        #点击搜索
        dr.click("xpath", el.bg_single_searchContent1_btn)
        #选择加价购
        time.sleep(3)
        dr.js("$('#uniform-250000214').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_addPriceTab1_confirmBtn)
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围金额
        dr.send_keys("xpath", el.bg_single_startCount2, "100")
        #输入加价购数量
        dr.send_keys("xpath", el.bg_single_rewardValue2, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_addPriceTab2)
        #输入加价购商品名称
        dr.send_keys("xpath", el.bg_single_searchContent2, u"汇源1L100%橙汁")
        #点击搜索
        dr.click("xpath", el.bg_single_searchContent2_btn)
        #选择加价购
        time.sleep(3)
        dr.js("$('#uniform-250000216').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_addPriceTab2_confirmBtn)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)


    #指定标准分类-件数满-赠优惠券
    def test_six_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #商品类型
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定标准品类商品
        dr.js("$('#productType1').parent().attr('class','checked')")
        dr.js("$('#productType1').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中件数满
        dr.js("$('#conditionType4').parent().attr('class','checked')")
        dr.js("$('#conditionType4').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选择赠优惠券
        dr.js("$('#awardType3').parent().attr('class','checked')")
        dr.js("$('#awardType3').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"指定标准分类-件数满-赠优惠券")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion6")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9982")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #标准分类列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_category)
        #输入标准名称
        dr.send_keys("xpath", el.bg_single_category_search, u"家用电器")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_category_btn)
        #选中品牌
        dr.js("$('#uniform-250020986').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_category_confirmBtn)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_Coupon_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_coupon_assreward)
        #输入超范围件数
        dr.send_keys("xpath", el.bg_single_coupon_startCount1, "2")
        #点击选择优惠券框
        dr.click("xpath", el.bg_single_select_coupon)
        #选择第一个优惠券
        dr.js("$('#uniform-250122220').find('input').click()")
        dr.click("xpath", el.bg_single_coupon1)
        dr.click_body()
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #指定虚拟分类-重量满-赠赠品
    def test_seven_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #商品类型
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定虚拟分类商品
        dr.js("$('#productType2').parent().attr('class','checked')")
        dr.js("$('#productType2').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中重量满
        dr.js("$('#conditionType3').parent().attr('class','checked')")
        dr.js("$('#conditionType3').prop('checked',true)")
        #奖励类型
        dr.js("$('#awardType1').parent().prop('class','checked')")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"指定虚拟分类-重量满-赠赠品")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion7")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9980")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #虚拟分类列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_VirtualCategory)
        #输入标准名称
        dr.send_keys("xpath", el.bg_single_VirtualCategory_search, u"洗护清洁")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_VirtualCategory_btn)
        #选中品牌
        dr.js("$('#uniform-250020095').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_VirtualCategory_confirmBtn)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始重量
        dr.send_keys("xpath", el.bg_single_startCount1, "0")
        #输入结束重量
        dr.send_keys("xpath", el.bg_single_upperCount1, "5000")
        #输入赠品数量
        dr.send_keys("xpath", el.bg_single_rewardValue1, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_gift_addPriceTab1)
        #输入赠品商品名称
        dr.send_keys("xpath", el.bg_single_gift_content1, u"亮碟洗碗机专用洗涤块（自动化误动）")
        #点击搜索
        dr.click("xpath", el.bg_single_gift_search_btn1)
        #选择赠品
        time.sleep(3)
        dr.js("$('#uniform-250122220').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_gift_search_confirmbtn1)
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围数量
        dr.send_keys("xpath", el.bg_single_startCount2, "5000")
        #输入
        dr.send_keys("xpath", el.bg_single_rewardValue2, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_gift_addPriceTab2)
        #输入赠品商品名称
        dr.send_keys("xpath", el.bg_single_gift_content2, u"麒麟法式香草风味咖啡")
        #点击搜索
        dr.click("xpath", el.bg_single_gift_search_btn2)
        #选择赠品
        time.sleep(3)
        dr.js("$('#uniform-250120218').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_gift_search_confirmbtn2)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #指定虚拟分类-件数满-选加价购
    def test_eight_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #商品类型
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定虚拟分类商品
        dr.js("$('#productType2').parent().attr('class','checked')")
        dr.js("$('#productType2').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中重量满
        dr.js("$('#conditionType4').parent().attr('class','checked')")
        dr.js("$('#conditionType4').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中加价购
        dr.js("$('#awardType2').parent().attr('class','checked')")
        dr.js("$('#awardType2').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"指定虚拟分类-件数满-选加价购")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion8")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9978")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #虚拟分类列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_VirtualCategory)
        #输入标准名称
        dr.send_keys("xpath", el.bg_single_VirtualCategory_search, u"洗护清洁")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_VirtualCategory_btn)
        #选中品牌
        dr.js("$('#uniform-250020095').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_VirtualCategory_confirmBtn)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始件数
        dr.send_keys("xpath", el.bg_single_startCount1, "0")
        #输入结束件数
        dr.send_keys("xpath", el.bg_single_upperCount1, "5")
        #输入加价购数量
        dr.send_keys("xpath", el.bg_single_rewardValue1, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_addPriceTab1)
        #输入加价购商品名称
        dr.send_keys("xpath", el.bg_single_searchContent1, u"百威啤酒500ml 罐装")
        #点击搜索
        dr.click("xpath", el.bg_single_searchContent1_btn)
        #选择加价购
        time.sleep(3)
        dr.js("$('#uniform-250000214').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_addPriceTab1_confirmBtn)
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围件数
        dr.send_keys("xpath", el.bg_single_startCount2, "5")
        #输入加价购数量
        dr.send_keys("xpath", el.bg_single_rewardValue2, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_addPriceTab2)
        #输入加价购商品名称
        dr.send_keys("xpath", el.bg_single_searchContent2, u"汇源1L100%橙汁")
        #点击搜索
        dr.click("xpath", el.bg_single_searchContent2_btn)
        #选择加价购
        time.sleep(3)
        dr.js("$('#uniform-250000216').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_addPriceTab2_confirmBtn)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买指定品牌商品-无条件-减商品金额
    def test_nine_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定品牌商品
        dr.js("$('#productType3').parent().attr('class','checked')")
        dr.js("$('#productType3').prop('checked',true)")
        #条件类型
        dr.js("$('#conditionType1').parent().prop('class','checked')")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中选加价购
        dr.js("$('#awardType5').parent().attr('class','checked')")
        dr.js("$('#awardType5').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买指定品牌-无条件-减商品金额")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion9")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9992")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #品牌列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_brand)
        #输入品牌名称
        dr.send_keys("xpath", el.bg_single_brand_search, u"雅诗兰黛")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_brand_search_btn)
        #选中品牌
        dr.js("$('#uniform-250001383').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_brand_search_confirmBtn)
        #点击选择优惠金额框
        dr.send_keys("xpath", el.bg_single_val, "5")
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买指定品牌商品-金额满-减运费金额
    def test_ten_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定品牌商品
        dr.js("$('#productType3').parent().attr('class','checked')")
        dr.js("$('#productType3').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#conditionType2').parent().attr('class','checked')")
        dr.js("$('#conditionType2').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中选加价购
        dr.js("$('#awardType6').parent().attr('class','checked')")
        dr.js("$('#awardType6').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买指定品牌商品-金额满-减运费金额")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion10")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9990")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #品牌列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_brand)
        #输入品牌名称
        dr.send_keys("xpath", el.bg_single_brand_search, u"雅诗兰黛")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_brand_search_btn)
        #选中品牌
        dr.js("$('#uniform-250001383').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_brand_search_confirmBtn)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始金额
        dr.send_keys("xpath", el.bg_single_startCount1, "0")
        #输入结束金额
        dr.send_keys("xpath", el.bg_single_upperCount1, "100")
        #输入加价购数量
        dr.send_keys("xpath", el.bg_single_rewardValue1, "1")
        #减运费N元
        dr.send_keys("xpath", el.bg_single_freight_fee1, "5")
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围金额
        dr.send_keys("xpath", el.bg_single_startCount2, "100")
        #选择全免
        dr.click("xpath", el.bg_single_freight_fee_type)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买指定品牌商品-件数满-赠赠品
    def test_eleven_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定品牌商品
        dr.js("$('#productType3').parent().attr('class','checked')")
        dr.js("$('#productType3').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#conditionType4').parent().attr('class','checked')")
        dr.js("$('#conditionType4').prop('checked',true)")
        #奖励类型
        #选中赠赠品
        dr.js("$('#awardType1').parent().prop('class','checked')")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买指定品牌商品-件数满-赠赠品")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion11")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9988")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #品牌列表
        #点击下拉框
        dr.click("xpath", el.bg_single_click_brand)
        #输入品牌名称
        dr.send_keys("xpath", el.bg_single_brand_search, u"雅诗兰黛")
        #点击搜索按钮
        dr.click("xpath", el.bg_single_brand_search_btn)
        #选中品牌
        dr.js("$('#uniform-250001383').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_brand_search_confirmBtn)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始件数
        dr.send_keys("xpath", el.bg_single_startCount1, "1")
        #输入结束件数
        dr.send_keys("xpath", el.bg_single_upperCount1, "5")
        #输入赠品数量
        dr.send_keys("xpath", el.bg_single_rewardValue1, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_gift_addPriceTab1)
        #输入赠品商品名称
        dr.send_keys("xpath", el.bg_single_gift_content1, u"亮碟洗碗机专用洗涤块（自动化误动）")
        #点击搜索
        dr.click("xpath", el.bg_single_gift_search_btn1)
        #选择赠品
        time.sleep(3)
        dr.js("$('#uniform-250122220').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_gift_search_confirmbtn1)
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围数量
        dr.send_keys("xpath", el.bg_single_startCount2, "5")
        #输入
        dr.send_keys("xpath", el.bg_single_rewardValue2, "1")
        #点击请选择
        dr.click("xpath", el.bg_single_gift_addPriceTab2)
        #输入赠品商品名称
        dr.send_keys("xpath", el.bg_single_gift_content2, u"麒麟法式香草风味咖啡")
        #点击搜索
        dr.click("xpath", el.bg_single_gift_search_btn2)
        #选择赠品
        time.sleep(3)
        dr.js("$('#uniform-250120218').find('input').click()")
        #点击确认
        dr.click("xpath", el.bg_single_gift_search_confirmbtn2)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买指定商品-金额满-减商品金额
    def test_twelve_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定品牌商品
        dr.js("$('#productType4').parent().attr('class','checked')")
        dr.js("$('#productType4').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#conditionType2').parent().attr('class','checked')")
        dr.js("$('#conditionType2').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#awardType5').parent().attr('class','checked')")
        dr.js("$('#awardType5').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买指定商品-金额满-减商品金额")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion12")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9988")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #商品列表
        #点击商品输入框
        dr.send_keys("xpath", el.bg_single_click_product, "10671047")
        #点击导入按钮
        dr.click("xpath", el.bg_single_importproduct)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始金额
        dr.send_keys("xpath", el.bg_single_startCount1, "0")
        #输入结束金额
        dr.send_keys("xpath", el.bg_single_upperCount1, "100")
        #输入优惠金额
        dr.send_keys("xpath", el.bg_single_discountamount1, "5")
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围数量
        dr.send_keys("xpath", el.bg_single_startCount2, "100")
        #输入
        dr.send_keys("xpath", el.bg_single_discountamount2, "8.8")
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买指定商品-重量满-减运费金额
    def test_thirteen_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定品牌商品
        dr.js("$('#productType4').parent().attr('class','checked')")
        dr.js("$('#productType4').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#conditionType3').parent().attr('class','checked')")
        dr.js("$('#conditionType3').prop('checked',true)")
        #奖励类型
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#awardType6').parent().attr('class','checked')")
        dr.js("$('#awardType6').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买指定商品-重量满-减运费金额")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion13")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9986")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #商品列表
        #点击商品输入框
        dr.send_keys("xpath", el.bg_single_click_product, "10671047")
        #点击导入按钮
        dr.click("xpath", el.bg_single_importproduct)

        #奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择范围内奖励
        dr.click("xpath", el.bg_single_areaaddreward1)
        #输入起始重量
        dr.send_keys("xpath", el.bg_single_startCount1, "0")
        #输入结束重量
        dr.send_keys("xpath", el.bg_single_upperCount1, "1000")
        #减运费N元
        dr.send_keys("xpath", el.bg_single_freight_fee1, "5")
        #选择超范围奖励
        #点击新增一条
        dr.click("xpath", el.bg_single_addnewone)
        #选择超范围奖励
        dr.click("xpath", el.bg_single_areaaddreward2)
        #输入超范围金额
        dr.send_keys("xpath", el.bg_single_startCount2, "1000")
        #选择全免
        dr.click("xpath", el.bg_single_freight_fee_type)
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    #买指定商品-件数满-第N件优惠
    def test_fourteen_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_promotion)
        time.sleep(3)
        dr.click("xpath", el.bg_single_promotion)
        #新增
        dr.switch_to_frame()
        time.sleep(3)
        dr.click("xpath", el.bg_addPromotion_button)
        #选择商品类型
        time.sleep(3)
        #取消买任意商品的默认选中
        dr.js("$('#productType0').removeAttr('checked')")
        dr.js("$('#productType0').parent().prop('class','')")
        #选中买指定品牌商品
        dr.js("$('#productType4').parent().attr('class','checked')")
        dr.js("$('#productType4').prop('checked',true)")
        #条件类型
        #取消无条件的默认选中
        dr.js("$('#conditionType1').removeAttr('checked')")
        dr.js("$('#conditionType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#conditionType4').parent().attr('class','checked')")
        dr.js("$('#conditionType4').prop('checked',true)")
        #奖励类型
        time.sleep(3)
        #取消赠赠品的默认选中
        dr.js("$('#awardType1').removeAttr('checked')")
        dr.js("$('#awardType1').parent().prop('class','')")
        #选中金额满
        dr.js("$('#awardType7').parent().attr('class','checked')")
        dr.js("$('#awardType7').prop('checked',true)")
        #下一步
        dr.click("xpath", el.bg_gotoAdd)
        #规则名称
        dr.send_keys("xpath", el.bg_promotion_name, u"买指定商品-件数满-第N件优惠")
        dr.send_keys("xpath", el.bg_promotion_nameen, u"single promotion14")
        #开始时间
        time.sleep(3)
        dr.click("xpath", el.bg_fromTime)
        #填写时间js
        dr.js("$('#txt_fromTime').attr('value','2016-11-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #结束时间
        time.sleep(3)
        dr.click("xpath", el.bg_thruTime)
        #填写时间js
        dr.js("$('#txt_thruTime').attr('value','2016-12-30 00:00')")
        #关闭时间插件js
        dr.js("$('.datetimepicker').attr('style', 'display:none')")
        #选择分站
        dr.click("xpath", el.bg_subsite1)
        dr.click("xpath", el.bg_subsite2)
        dr.click("xpath", el.bg_subsite3)
        dr.click("xpath", el.bg_subsite4)
        #取消选择渠道
        dr.click("xpath", el.bg_channel4)
        #优先级
        dr.send_keys("xpath", el.bg_sequence, "9984")
        #支持的条件标记
        dr.click("xpath", el.bg_single_markTypeProduct1)
        dr.click("xpath", el.bg_single_markTypeProduct2)
        dr.click("xpath", el.bg_single_markTypeSignle1)
        dr.click("xpath", el.bg_single_markTypeSignle2)
        dr.click("xpath", el.bg_single_markTypeSignle3)
        dr.click("xpath", el.bg_single_markTypeSignle4)
        dr.click("xpath", el.bg_single_markTypeSignle5)
        dr.click("xpath", el.bg_single_markTypeSignle6)
        dr.click("xpath", el.bg_single_markTypeSignle7)

        #商品列表
        #点击商品输入框
        dr.send_keys("xpath", el.bg_single_click_product, "10671047")
        #点击导入按钮
        dr.click("xpath", el.bg_single_importproduct)

        #奖励
        dr.switch_to_frame_out()
        dr.js('window.scrollTo(0,0);')
        dr.switch_to_frame()
        #点击新增一条
        dr.click("xpath", el.bg_single_addNthReward_addnewone)
        #选择第N件优惠
        dr.click("xpath", el.bg_single_addNthReward1)
        #选择第N件优惠
        dr.switch_to_frame_out()
        dr.js('window.scrollTo(0,0);')
        dr.switch_to_frame()
        dr.send_keys("xpath", el.bg_single_addrewardprice1, "1")
        dr.send_keys("xpath", el.bg_single_rewardprice1, "9")
        #点击新增一条
        dr.click("xpath", el.bg_single_addNthReward_addnewone)
        #选择第N件超范围阶梯优惠
        dr.click("xpath", el.bg_single_addNthReward2)
        dr.send_keys("xpath", el.bg_single_rewardCount2, "2")
        dr.send_keys("xpath", el.bg_single_addRewardCount2, "2")
        dr.send_keys("xpath", el.bg_single_addrewardprice2, "1")
        dr.send_keys("xpath", el.bg_single_rewardprice2, "8.8")
        #提交
        dr.click("xpath", el.bg_single_submitbtn)
        time.sleep(5)

    def tearDown(self):
        dr = self.dr
        dr.quit()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(singlepromotion)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
