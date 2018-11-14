# coding:utf-8
__author__ = 'liuguijie'

import comall
import unittest
from setting.liuguijie import data as d
from setting.liuguijie import el
from setting.liuguijie import setting
from ddt import ddt, unpack, data

import time

@ddt
class LiuguijieTest(unittest.TestCase):
    my_data = d.TestData().get("liu_study")

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()

    @data(my_data[0], my_data[1])
    @unpack
    def test001(self, c_newuser_name_text, c_newuser_username_text, c_newuser_password_text, c_newuser_phone_text,
                c_newuser_mail_text, error_message):
        dr = self.dr
        self.dr.open(setting.carrefour)
        time.sleep(2)
        # 输入用户名
        dr.send_keys(el.c_login_username_type, el.c_login_username_input, el.c_login_username_text)
        # 输入密码
        dr.send_keys(el.c_login_password_type, el.c_login_password_input, el.c_login_password_text)
        # 点击登录
        dr.click(el.c_login_submit_type, el.c_login_submit_btn)
        # 判定（determine）界面是否有“系统用户管理”栏显示
        if not dr.is_display(el.c_homepage_mgmt_type, el.c_homepage_mgmt):
            # 如果不显示“系统用户管理”，→点击“系统”
            dr.click(el.c_homepage_system_type, el.c_homepage_system)
        # 点击“系统用户管理"
        dr.click(el.c_homepage_mgmt_type, el.c_homepage_mgmt)
        # 进入frame
        dr.switch_to_frame(0)
        # 获取“系统用户管理”2的text
        determine_mgmt2 = dr.get_text(el.c_mgmt_mgmt2_type, el.c_mgmt_mgmt2)
        self.assertEquals(u"系统用户管理", determine_mgmt2, u"失败")
        print determine_mgmt2
        # 点击"新增系统用户"
        dr.click(el.c_mgmt_create_user_type, el.c_mgmt_create_user_btn)
        # 输入姓名
        dr.send_keys(el.c_newuser_name_type, el.c_newuser_name_input, c_newuser_name_text)
        time.sleep(1)
        # 输入用户名
        dr.send_keys(el.c_newuser_username_type, el.c_newuser_username_input, c_newuser_username_text)
        time.sleep(1)
        # print el.c_newuser_username_text
        # 输入密码
        dr.send_keys(el.c_newuser_password_type, el.c_newuser_password_input, c_newuser_password_text)
        time.sleep(2)
        # 输入手机号
        dr.send_keys(el.c_newuser_phone_type, el.c_newuser_phone_input, c_newuser_phone_text)
        # 输入邮箱
        dr.send_keys(el.c_newuser_mail_type, el.c_newuser_mail_input, c_newuser_mail_text)
        # 选定角色
        dr.click(el.c_newuser_role01_type, el.c_newuser_role01)
        time.sleep(2)
        # 滑动第二下滑条
        dr.js("window.scrollTo(0,'1000')")
        # 选定分站
        dr.click(el.c_newuser_station02_type, el.c_newuser_station02)
        # 点击提交
        dr.click(el.c_newuser_submit_type, el.c_newuser_submit_btn)
        dr.switch_to_frame_out()
        dr.js("window.scrollTo(0,'0')")
        dr.switch_to_frame(0)
        time.sleep(3)
        # dr.switch_to_frame(0)
        # 点击类别“姓名”
        dr.click(el.c_mgmt_category_type, el.c_mgmt_category_btn)
        # 选择 “用户名”
        dr.click(el.c_mgmt_category_username_type, el.c_mgmt_category_username)
        # 输入
        dr.send_keys(el.c_mgmt_search_type, el.c_mgmt_search_input, c_newuser_username_text)

        time.sleep(1)
        # 点击“搜索”
        dr.click(el.c_mgmt_search_btn_type, el.c_mgmt_search_btn)
        time.sleep(5)

        # 获取已搜索的“登录名”的文本
        first_username = dr.get_text(el.c_mgmt_first_username_type, el.c_mgmt_first_username)
        print first_username
        self.assertEquals(c_newuser_username_text, first_username, error_message)
        time.sleep(5)

    # def tearDown(self):
        self.dr.close()


