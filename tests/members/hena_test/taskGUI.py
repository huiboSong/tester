# coding=utf-8

__author__ = 'hena'

import comall
import unittest
import os,time
from ddt import ddt, unpack, data
from setting.hena_test import data as d
from setting.hena_test import el
from setting.hena_test import setting


@ddt
class HenaTest(unittest.TestCase):
    """从家乐福测试后台新增系统用户成功"""

    # 获得测试数据
    my_data = d.TestData().get("he_task")

    # 初始化方法，打开浏览器
    def setUp(self):
        # 打开一个浏览器，使用的是guosetting2里面设置的
        self.dr = comall.Comall(setting.driver_type)
        # 最大化浏览器
        self.dr.max_window()

    @data(my_data[0],my_data[1])
    @unpack
    def test_001(self, data_id, username, password, add_name, add_username, page_equal,
                 addpage_password, addpage_telephone_number, addpage_email,  error_message1, error_message2):
        """家乐福后台新增系统用户的测试"""
        # 获得driver浏览器对象
        dr = self.dr
        # 打开一个网址，hena_test\setting里面设置的url
        self.dr.open(setting.carrefour_url)
        # 在用户名输入框里输入一个值
        dr.send_keys(el.c__text_type, el.c_login_username_input, username)
        # 在密码输入框里输入一个值
        dr.send_keys(el.c__text_type, el.c_login_password_input, password)
        # 点击登录按钮
        dr.click(el.c_el_type, el.login_button)
        # 点击系统按钮

        if dr.is_display(el.c__text_type,el.system_title_iframe2):
            # 点击系统用户管理按钮
            dr.click(el.c__text_type, el.system_title_iframe2)
        else:
            # 点击系统按钮
            dr.click(el.c__text_type, el.system_title_iframe1)
            # 点击系统用户管理按钮
            dr.click(el.c__text_type, el.system_title_iframe2)

        # 进入框架
        dr.switch_to_frame()
        # 获得一个系统用户管理页面的“系统用户管理”
        system_name_management = dr.get_text(el.c__text_type, el.system_title_iframe3)
        # 判断是否获得文本和我们期望的一样，测试是否成功或失败
        self.assertEqual(page_equal, system_name_management, error_message1)


        # 点击新增系统用户管理按钮
        dr.click(el.c_el_type, el.add_button)
        # 新增页面里输入数据
        # 在姓名输入框里输入一个值
        dr.send_keys(el.c__text_type, el.add_name_input, add_name)
        time.sleep(2)
        # 在登录名输入框里输入一个值
        dr.send_keys(el.c__text_type, el.add_username_input, add_username)
        time.sleep(2)
        # 在密码输入框里输入一个值
        dr.send_keys(el.c__text_type, el.add_password_input, addpage_password)
        time.sleep(2)
        # 在手机号输入框里输入一个值
        dr.send_keys(el.c__text_type, el.add_PhNumer_input, addpage_telephone_number)
        time.sleep(2)
        # 在邮箱输入框里输入一个值
        dr.send_keys(el.c__text_type, el.add_email_input, addpage_email)
        time.sleep(2)
        # 点击失效时间下拉框
        dr.click(el.c__text_type, el.add_abate_input)
        time.sleep(2)
        # 点击选择6月30号
        dr.click(el.c__text_type, el.add_abate_month_input)
        time.sleep(2)
        # 字符串判断这样写
        if cmp(data_id, '1') == 0:
            # 点击系统角色选择按钮
            dr.click(el.c__text_type, el.auto_member_selected)
            time.sleep(2)
            # 点击新增分站按钮
            dr.click(el.c__text_type, el.taiwan_area_selected)
            time.sleep(2)
        else:
            # 点击系统角色选择按钮
            dr.click(el.c__text_type, el.nomal_member_selected)
            time.sleep(2)
            # 点击新增分站按钮
            dr.click(el.c__text_type, el.baoli_area_selected)
            time.sleep(2)
        # 点击提交按钮
        dr.click(el.c_el_type, el.submit_button)
        # 等待页面加载5秒钟
        time.sleep(5)

        # 跳出ifram页面
        dr.switch_to_frame_out()
        # 将滚动条拉倒最上端
        dr.js("window.scroll(500,0);")
        # 跳进ifram页面
        dr.switch_to_frame()
        time.sleep(2)

        # 点击在列表页搜索下拉菜单
        dr.click(el.c__text_type, el.search_list)
        # 点击在列表页搜索下拉菜单里的登录名
        dr.click(el.c__text_type, el.search_list_loginName)
        # 在列表页搜索输入框里输入一个值
        dr.send_keys(el.c__text_type, el.search_Content, add_username)
        # 点击列表页搜索按钮
        dr.click(el.c_el_type, el.search_button)
        # 等待页面加载8秒钟
        time.sleep(8)

        # 获得一个查询结果页面的登录名的xpath值
        SearchAddName = dr.get_text(el.c__text_type, el.search_add_loginName)
        # 判断是否获得输出结果与期望一致，否则抛出错误信息
        self.assertEqual(add_username, SearchAddName, error_message2)


    def tearDown(self):
        dr = self.dr
        # 关闭浏览器
        dr.close()



