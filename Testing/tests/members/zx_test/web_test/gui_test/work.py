# coding=utf-8
from ddt import ddt, unpack, data
import time
import xlrd
import comall
import config
from core import commonutils
from core.persistentdata import PersistentData
from setting.zx_test import setting
from setting.zx_test import el
from setting.zx_test.data import TestData

__author__ = 'zhangxue'

import unittest

'''
1、打开浏览器，登录家乐福测试环境后台 http://172.31.1.251:8080/login  （在家需要连接公司vpn才能连接）
2、使用登录账号（无需输入验证码）：autotester  密码：qwerty123
3、点击菜单【系统用户管理】，打开页面（iframe）
4、使用框架的switch to frame方法，进入iframe

5、断言判断进入的页面是菜单对应的页面

6、点击新增系统用户
7、输入新增信息，角色选择【autotester】，地区选择【全球购-台湾】
8、保存；返回列表页
9、在列表页查询刚才新建的用户，断言判断新增成功
10、重复创建一个新用户；角色选择【普通会员】，地区选择【深圳-保利店】，并到列表页验证新增成功
'''


@ddt
class MyTestCase(unittest.TestCase):
    # 添加用户数据
    work_data = TestData().get("work_data")
    data_user = TestData().get("work_user")

    def setUp(self):
        # 创建Comall对象
        self.dr = comall.Comall(setting.driver_type)
        # 最大化窗口
        self.dr.max_window()
        pass

    @data(work_data[0], work_data[1])
    @unpack
    def test_work(self, work_type, name, user, password, phone, mail):

        dr = self.dr
        # 打开家乐福登录页面
        dr.open(setting.login_page)
        # self.dr.assert_equal(name, 'zx', self.data_user[0][4],True,'zx111')
        # 输入用户名
        dr.send_keys(setting.el_xpath, el.input_et_user, self.data_user[0][0])
        # 输入秘密
        dr.send_keys(setting.el_xpath, el.input_et_pw, self.data_user[0][1])
        # 点击登录
        dr.click(setting.el_xpath, el.btn_login)
        time.sleep(5)
        # 判断系统用户管理是否显示
        if dr.is_display(setting.el_xpath, el.btn_system_user):
            pass
        else:
            # 没有显示点击系统按钮
            dr.click(setting.el_xpath, el.btn_system)
        time.sleep(3)
        # 点击系统用户管理
        dr.click(setting.el_xpath, el.btn_system_user)
        time.sleep(5)
        # 进入第一层ifame标签
        dr.switch_to_frame()
        # 获取标题栏名称
        text = dr.get_text(setting.el_xpath, el.text_system_user)
        # 断言判断进入的页面是菜单对应的页面
        self.assertEqual(text, self.data_user[0][2], self.data_user[0][3])
        # 点击新增系统用户
        dr.click(setting.el_xpath, el.btn_add_user)
        time.sleep(5)
        # 输入用姓名
        dr.send_keys(setting.el_xpath, el.add_w_name, name)
        # 输入用户名
        dr.send_keys(setting.el_xpath, el.add_w_user, user)
        # 输入密码
        dr.send_keys(setting.el_xpath, el.add_w_pw, password)


        workbook = xlrd.open_workbook(r'..\..\testdata.xlsx')
        sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始

        phone_v=PersistentData().getData("phone_updata")
        if phone_v=="Error":
            PersistentData().setData("phone_updata",1)
        phone_v=PersistentData().getData("phone_updata")

        phone_new=sheet1.cell(int(phone_v), 0).value #第2行 第0列
        PersistentData().setData("phone_updata",int(phone_v)+1,True)



        # 根据sheet索引或者名称获取sheet内容
        sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
        # 输入手机号
        dr.send_keys(setting.el_xpath, el.add_w_phone, str(int(phone_new)))
        time.sleep(10)
        # 输入邮箱
        dr.send_keys(setting.el_xpath, el.add_w_mail, mail)

        # 判断分站添加台湾or保利
        if work_type == 1:
            # 新增台湾店
            dr.click(setting.el_xpath, el.add_user_type_1)
            dr.click(setting.el_xpath, el.add_check_type_1)
        elif work_type == 2:
            # 新增保利店
            dr.click(setting.el_xpath, el.add_user_type_2)
            # dr.js('$(".ztree_2_ul li:nth-child(1) span:nth-child(1) ").click()')
            dr.click(setting.el_xpath, el.add_check_type_2)


        # 点击保存
        dr.click(setting.el_xpath, el.add_submit)
        time.sleep(5)
        # 搜索栏输入姓名
        dr.send_keys(setting.el_xpath, el.check_input, name)

        # 退出ifame标签
        dr.switch_to_frame_out()
        # 滚动条滚动到最上面
        dr.js("window.scrollTo(0,0)")
        # 进去iframe标签
        dr.switch_to_frame()

        # 点击搜索
        dr.click(setting.el_xpath, el.check_search)
        time.sleep(5)
        # 判断搜索是否有结果
        if dr.is_display(setting.el_xpath, el.check_list_one):
            # 获取搜索结果中的姓名
            text = dr.get_text(setting.el_xpath, el.check_list_one)
            # 断言是否新增成功
            self.assertEqual(name, text, self.data_user[0][4])

        else:
            # 断言新增系统用户失败
            self.fail(self.data_user[0][4])

    def tearDown(self):
        # 关闭dr
        # self.dr.quit()
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
