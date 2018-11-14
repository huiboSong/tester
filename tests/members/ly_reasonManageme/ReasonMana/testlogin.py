# coding=utf-8

__author__ = 'lily'

import unittest
import time
# 引入主框架文件
import comall
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.ly_reasonManageme import el
from setting.ly_reasonManageme import setting
from setting.ly_reasonManageme import data


def login_success(dr,dc):

        dr.open(setting.login_page)
        time.sleep(1)
        # 检查登录输入框存在
        dr.until("xpath", el.login_user_edit)
        # 用户名输入
        dr.send_keys("xpath", el.login_user_edit,data.login_user)
        # 密码输入
        dr.send_keys("xpath", el.login_pw_edit, data.login_pw)
        # 点击登录按钮
        dr.click("xpath", el.login_submit_btn)
        time.sleep(2)
        # 检查是否登录成功
        login_name = dr.get_text("xpath", el.dashboard_top_name_span)
        dc.assertEqual(data.login_user, login_name, "login_error:登录用户名称校验失败")

# 下面是脚本单独调试所需代码

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login_success)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

