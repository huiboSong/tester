# coding=utf-8

import  comall

from setting.cww_test import test_el
from setting.cww_test import setting

def test_login(dr, ww):
        # ww.open(setting.login_page)
        # 输入用户名
        dr.send_keys("xpath", test_el.Xuser_name, test_el.user_name)
        # 输入密码
        dr.send_keys("xpath", test_el.Xpassword, test_el.password)
        # 点击登录按钮
        dr.click("xpath", test_el.Xlogin_btn)
        # 检查登录是否成功
        user_name1 = dr.get_text("xpath", test_el.Xlogin_info)
        ww.assertEqual(user_name1, "heyanping", "后台登录成功")