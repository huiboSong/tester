# coding=utf-8
"""
家乐福（后台）通用操作

"""
import sys

from setting.hyptest import el
from setting.hyptest import setting

reload(sys)
sys.setdefaultencoding("utf-8")

def bg_login_success(dr, tc):

    # 打开后台登录地址
    dr.open(setting.bg_login_page)
    # 输入用户名,密码,验证码
    dr.send_keys("xpath", el.bg_login_name, "heyanping")
    dr.send_keys("xpath", el.bg_login_password, "qwer12345")
    dr.send_keys("xpath", el.bg_vertifycode, "")
    dr.click("xpath", el.bg_login_button)
    #判断是否登录成功
    bg_user_name = dr.get_text("xpath", el.bg_username)
    tc.assertEqual(bg_user_name, "heyanping", "后台登录成功")

