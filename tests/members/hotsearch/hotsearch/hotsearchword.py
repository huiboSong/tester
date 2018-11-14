# coding=utf-8

import unittest
import time

from ddt import ddt, data, unpack

# 引入主框架文件
import comall

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hotsearch import el
from setting.hotsearch import setting
from setting.hotsearch.data import TestData as dt
import sys
from logs.tests.members.hotsearch.hotsearch import login

reload(sys)
sys.setdefaultencoding("utf-8")

@ddt
class TeseCase(unittest.TestCase):
    #后台-界面-新增搜索热词
    d = dt().get("search_word")

    def setUp(self):
        self.dr=comall.Comall(setting.driver_type)
        self.dr.max_window()
        login.login_success(self.dr, self)

    @unpack
    @data(d[0])
    def test_hostword_add(self,type,chname,egname,linkaddr,seq,returnmsg,delmsg,frontmsg):
        dr = self.dr
        dr.click("xpath",el.item_ui)
        dr.click("xpath",el.item_ui_searchword)
        time.sleep(1)
        dr.js("window.scrollTo(0,0)")
        dr.switch_to_frame()
        dr.until("xpath",el.item_ui_addword)
        dr.click("xpath",el.item_ui_addword)
        time.sleep(1)
        dr.send_keys("xpath",el.item_ui_chinesetext,chname)
        dr.send_keys("xpath",el.item_ui_englishtext,egname)
        dr.send_keys("xpath",el.item_ui_linkaddress,linkaddr)
        dr.send_keys("xpath",el.item_ui_sequence,seq)
        dr.click("xpath",el.item_ui_btn)
        dr.until_page_load()
        #验证列表添加成功
        dr.until("xpath",el.item_ui_name)
        text=dr.get_text("xpath",el.item_ui_name)
        self.assertEqual(chname,text,returnmsg)
        text2=dr.get_text("xpath",el.item_ui_name2)

        #验证删除
        if(type=="delete"):
            dr.click("xpath",el.item_ui_delete)
            dr.until("xpath",el.item_ui_asssertdelete)
            dr.click("xpath",el.item_ui_asssertdelete)
            time.sleep(5)
            dr.until("xpath",el.item_ui_name)
            text1=dr.get_text("xpath",el.item_ui_name)
            self.assertEqual(text2,text1,delmsg)

            #验证前台展示
            dr.open(setting.front_page)
            login.area_select(dr)
            time.sleep(5)
            dr.until_page_load()
            fronttext=dr.get_text("xpath",el.item_front_word)
            self.assertEqual(text1,fronttext,frontmsg)




    def tearDown(self):
        dr = self.dr
        dr.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TeseCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)