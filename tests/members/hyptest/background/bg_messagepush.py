# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall
from logs.tests.members.hyptest.background import bg_common

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting
from setting.hyptest.data_messagepush import TestData as dt
from ddt import ddt, data, unpack

@ddt
class messagepush(unittest.TestCase):
    d = dt().get("bg_message1")

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        time.sleep(1)
        bg_common.bg_login_success(self.dr, self)
    '''
    def first_case(self):
        dr = self.dr
        dr.click("xpath", el.bg_markering)
        time.sleep(3)
        dr.click("xpath", el.bg_messagepush)

        #新增
        dr.switch_to_frame()
        dr.until("xpath", el.bg_messagebtn)
        time.sleep(3)
        dr.click("xpath", el.bg_messagebtn)

        #新增页面
        time.sleep(3)
        #选择消息类型
        dr.click("xpath", el.bg_messagetype)
        #选择活动消息
        dr.click("xpath", el.bg_activitymessage)
        #标题中文
        dr.send_keys("xpath", el.bg_message_titleZn, u"贺艳萍测试")
        #标题英文
        dr.send_keys("xpath", el.bg_message_titleEn, "heyanpingtest")
        #内容中文
        dr.send_keys("xpath", el.bg_message_contentZn, u"贺艳萍测试")
        #内容英文
        dr.send_keys("xpath", el.bg_message_contentEn, "heyanpingtest")
        #点击选择图片中文
        #dr.click("xpath", el.bg_message_picZn)
        #dr.click("xpath", el.bg_message_picframe1)
        dr.send_keys("id", "picFile", "/Users/heyanping/Downloads/18981839_095218870000_2.jpg")
        #点击选择图片英文
        dr.click("xpath", el.bg_message_picEn)
        dr.send_keys("id", "picENFile", "/Users/heyanping/Downloads/18981839_095218870000_2.jpg")
        #目标页--文章
        dr.click("xpath", el.bg_message_target)
        dr.send_keys("xpath", el.bg_message_targetaddress, "www.baidu.com")
        #过期时间
        dr.click("xpath", el.bg_message_endtime)
        dr.js("$('txt_fromTime').attr('value','2016-09-30 00:00')")
    '''

    @data(d[0])
    @unpack
    def test_second_case(self, titlezn, titleen, contentzn, contenten, titleen2):
        dr = self.dr
        dr.click("xpath", el.bg_markering)
        time.sleep(3)
        dr.click("xpath", el.bg_messagepush)
        temp_name_111 = titlezn
        #新增
        dr.switch_to_frame()
        dr.until("xpath", el.bg_messagebtn)
        time.sleep(3)
        for i in range(1, 2):
            dr.click("xpath", el.bg_messagebtn)

            #新增页面
            time.sleep(3)
            #选择消息类型
            dr.click("xpath", el.bg_messagetype)
            #选择系统通知
            dr.click("xpath", el.bg_System_notification)
            #标题中文
            temp_name = dt.titleZn()
            dr.send_keys("xpath", el.bg_message_titleZn, temp_name)
            #标题英文
            dr.send_keys("xpath", el.bg_message_titleEn, titleen)
            #内容中文
            dr.send_keys("xpath", el.bg_message_contentZn, contentzn)
            #内容英文
            dr.send_keys("xpath", el.bg_message_contentEn, contenten)
            #目标页--文章
            dr.click("xpath", el.bg_message_target)
            dr.send_keys("xpath", el.bg_message_targetaddress, "250020081")
            #过期时间
            dr.click("xpath", el.bg_message_endtime)
            dr.js("$('#txt_thruTime').attr('value','2016-10-26 17:55:00')")

            #立即
            dr.click("xpath", el.bg_message_immediately)
            dr.js("document.body.scrollTop=100")
            #目标平台
            dr.js("$('[value=ios]').parent().attr('class','checker')")
            dr.js("$('[value=ios]').parent().attr('class','checked')")
            dr.js("$('[value=android]').parent().attr('class','checker')")
            dr.js("$('[value=android]').parent().attr('class','checked')")
            #目标语言
            dr.js("$('#language_zn').parent().attr('class','checker')")
            dr.js("$('#language_zn').parent().attr('class','checked')")
            dr.js("$('#language_en').parent().attr('class','checker')")
            #dr.js("$('#language_en').parent().attr('class','checked')")

            #目标城市
            dr.click("xpath", el.bg_message_bg)
            dr.click("xpath", el.bg_message_cd)
            dr.click("xpath", el.bg_message_sh)

            #定速推送勾选
            dr.js("$('[name=chk_sendSpeed]').parent().prop('class','checked')")
            dr.js("$('[name=chk_sendSpeed]').prop('checked','checked')")
            dr.js("$('#txt_sendSpeed').removeAttr('readonly')")
            dr.js("$('#txt_sendSpeed').val(10)")

            #通知标题
            dr.send_keys("xpath", el.bg_message_titleZn1, temp_name)
            dr.send_keys("xpath", el.bg_message_titleEn2, titleen2)

            #提交
            dr.click("xpath", el.bg_message_savebtn)

            time.sleep(3)
            dr.switch_to_frame_out()
            dr.js('window.scrollTo(0,0);')
            dr.switch_to_frame()

    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(messagepush)
    result = unittest.TextTestRunner(verbosity=2).run(suite)



