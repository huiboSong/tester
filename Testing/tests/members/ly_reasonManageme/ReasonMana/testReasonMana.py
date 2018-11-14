# coding=utf-8

import unittest
import time

from ddt import ddt, data, unpack

# 引入主框架文件
import comall

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.ly_reasonManageme import el
from setting.ly_reasonManageme import setting
from setting.ly_reasonManageme.data import TestData as dt
from logs.tests.members.ly_reasonManageme.ReasonMana import testlogin

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

@ddt
class TeseCase(unittest.TestCase):
    #后台-会员-原因管理
    d = dt().get("member")

    def setUp(self):
        self.dr=comall.Comall(setting.driver_type)
        self.dr.max_window()
        testlogin.login_success(self.dr, self)

#self.dr,self  unittest.TestCase
    @unpack
    @data(d[0])
    def test_reason_add(self,chinesename,englishname,sort,returnmsg,delmsg):
        dr = self.dr
        #后台-会员
        dr.click("xpath",el.member_ui)
        #原因管理
        dr.click("xpath",el.member_reasonmana)
        time.sleep(1)
        dr.js("window.scrollTo(0,0)")
        dr.switch_to_frame()
        #新增原因
        dr.until("xpath",el.member_addreason)
        dr.click("xpath",el.member_addreason)
        time.sleep(1)
        #输入中文名称
        dr.send_keys("xpath",el.member_chinesetext,chinesename)
        #输入英文名称
        dr.send_keys("xpath",el.member_englishtext,englishname)
        #输入顺序
        dr.send_keys("xpath",el.member_sort,sort)
        #点击保存按钮
        dr.click("xpath",el.member_submit)
        dr.until_page_load()
        #验证列表添加成功
        dr.until("xpath",el.member_ui_name)
        #获取第一列中文名称
        text=dr.get_text("xpath",el.member_ui_name)
        self.assertEqual(chinesename,text,returnmsg)
        #删除
        dr.click("xpath",el.member_ui_delete)
        dr.until("xpath",el.member_ui_asssertdelete)
        dr.click("xpath",el.member_ui_asssertdelete)
        time.sleep(2)
        #验证删除
        if(type=="delete"):
            dr.until("xpath",el.member_ui_name)
            #获取第一列中文名称
            text1=dr.get_text("xpath",el.member_ui_name)
            self.assertEqual(text1,text,delmsg)


    def tearDown(self):
        dr = self.dr
        dr.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TeseCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)