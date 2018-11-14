#coding=utf-8
import pickle
import pprint
import unittest
import time

from ddt import ddt, unpack, data

import comall
from setting.zx_test import el, setting
from setting.zx_test.data import TestData
from logs.tests.members.zx_test.web_test.gui_test import common_login

__author__ = 'zhangxue'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

@ddt
class addUser(unittest.TestCase):

    d = TestData().get("adduser")


    def setUp(self):
        # self.dr为  comall的实例化对象，comall继承pyse类。
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()
        common_login.login(self.dr)
    #d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10], d[11], d[12], d[13], d[14]
    @unpack
    @data(d[0], )
    # @data(d[10])
    def test_add_user(self,type,name,mail,phone,card,mm,mm_r):
        # dr=self.dr
        self.dr.click("xpath",el.user_btn)
        self.dr.click('xpath',el.user_guanli)
        # self.dr.click('xpath',el.user_add)
        # 验证进入成功
        time.sleep(1)
        # self.dr.js("window.scrollTo(0,0)")
        # iframe网页内嵌套的网页的标签，不能直接找到所嵌入的网站。
        self.dr.switch_to_frame()
        title = self.dr.get_text("xpath", el.page_title)
        self.assertEqual("会员管理", title)

        self.dr.click('xpath',el.user_add)



        try:
            pkl_file = open('data.pkl', 'rb')
            data = pickle.load(pkl_file)

        except IOError:
            print "Error 文件读取错误"
        else:
            pprint.pprint(data)
            name_re = data['name']
            email_re = data['mail']
            phone_re = data['phone']
            pkl_file.close()

        if type == 8:
            # 验证-邮箱输入重复提示
            self.dr.send_keys("xpath",el.add_user,name)
            self.dr.send_keys("xpath",el.add_mail,email_re)
            self.dr.send_keys("xpath",el.add_phone,phone)
        elif type == 9:
            # 验证-手机号输入重复提示
            self.dr.send_keys("xpath",el.add_user,name)
            self.dr.send_keys("xpath",el.add_mail,mail)
            self.dr.send_keys("xpath",el.add_phone,phone_re)

        elif type==10:
            #验证-用户名输入重复提示
            self.dr.send_keys("xpath",el.add_user,name_re)
            self.dr.send_keys("xpath",el.add_mail,mail)
            self.dr.send_keys("xpath",el.add_phone,phone)

        else:
            self.dr.send_keys("xpath",el.add_user,name)
            self.dr.send_keys("xpath",el.add_mail,mail)
            self.dr.send_keys("xpath",el.add_phone,phone)

        self.dr.send_keys("xpath",el.add_card,card)
        self.dr.send_keys("xpath",el.add_mm,mm)
        if mm_r == '':
            self.dr.send_keys("xpath",el.add_mm_r,mm)
        else:
            self.dr.send_keys("xpath",el.add_mm_r,mm_r)

        self.dr.click("xpath",el.user_level)
        self.dr.click("xpath",el.user_level_selet)
        self.dr.click("xpath",el.user_lan)
        self.dr.click("xpath",el.user_lan_selet)

        if type == 7:
            pass
        else:
            self.dr.click("xpath",el.user_address)
            self.dr.click("xpath",el.user_address_selet)


        # t=threading.Thread(target=self.getText,args=())
        # t.setDaemon(True)
        # t.start()

        self.dr.click('xpath',el.user_commit)


        # time.sleep(2)

        if type == 0:
            # 验证-密码长度是否一致
            text = self.dr.get_text("xpath", el.user_mm_error)
            self.assertEqual(text, "密码由6-20位数字、字母或符号组成","密码长度验证")
        elif type == 1:
            # 验证用户名输入空格验证
            text = self.dr.get_text("xpath", el.user_nemaspace_error)
            self.assertEqual(text, "第一个字符和最后一个字符不能为空格！","用户名输入空格验证")
        elif type == 2:
            # 验证邮箱格式
            text = self.dr.get_text("xpath", el.user_email_error)
            self.assertEqual(text, "邮箱格式不正确","邮箱格式验证")
        elif type == 3:
            # 手机号格式验证
            text = self.dr.get_text("xpath", el.user_phone_error)
            self.assertEqual(text, "手机号格式不正确","手机号格式验证")
        elif type == 4:
            # 验证密码输入不一致
            text = self.dr.get_text("xpath", el.user_mm_re_error)
            self.assertEqual(text, "密码确认与密码不一致","密码与确认密码输入不一致没有正确提示")
        elif type == 5:
            time.sleep(2)
            # 验证是否添加成功
            data1 = {'name': name,
                     'mail': mail,
                     'phone': phone}
            output = open('data.pkl', 'wb')
            pickle.dump(data1, output)
            output.close()

            title_get = self.dr.get_text("xpath", el.user_list_first)
            self.assertEqual(title_get, str(phone),"添加会员失败")
        elif type == 6:
            # text=self.dr.js('$(cldToastMsg).attr("msg")')
            # print text
            self.dr.switch_to_frame_out()
            text = self.dr.get_text("xpath", el.name_email_address_error)
            self.assertEqual(text, "邮箱和手机不能都为空","验证邮箱和手机均没填是系统提示")
        elif type == 7:
            # 验证-区域没有选择提示
            self.dr.switch_to_frame_out()
            text = self.dr.get_text("xpath", el.name_email_address_error)
            self.assertEqual(text, "请选择属在城市","验证地址没选系统提示")
        elif type == 8:
            # 验证-邮箱输入重复提示
            text = self.dr.get_text("xpath", el.user_email_error)
            self.assertEqual(text, "该邮箱已存在","邮箱输入重复提示")
        elif type == 9:
            # 验证-手机号输入重复提示
            text = self.dr.get_text("xpath", el.user_phone_error)
            self.assertEqual(text, "该手机号已存在","手机号输入重复提示")
        elif type == 10:
            # 验证-用户名输入重复提示
            text = self.dr.get_text("xpath", el.user_name_error)
            self.assertEqual(text, "该用户名已存在","用户名输入重复提示")

        # #验证重复输入
        # name_re = dr.get_text("xpath", el.user_name_error)
        # self.assertEqual(name_re, "该用户名已存在")




    # def getText(self):
    #
    #     while True:
    #         textMsg = self.dr.get_text_shake("xpath", el.name_email_address_error)
    #         print textMsg


    def tearDown(self):
        dr=self.dr
        dr.quit()


if __name__=="__main__":
    suite=unittest.TestLoader.loadTestsFromTestCase(addUser)
    unittest.TextTestRunner(verbosity=2).run(suite)

