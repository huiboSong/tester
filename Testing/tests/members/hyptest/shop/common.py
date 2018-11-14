# coding=utf-8
"""
家乐福（前台）通用操作

"""
import time
import sys

from logs.tests.members.hyptest.shop import shop_common
from setting.hyptest import el
from setting.hyptest import setting
from setting.hyptest import data


reload(sys)
sys.setdefaultencoding("utf-8")

def login_success(dr, tc):

    # 打开前台登录地址
    shop_common.shop_area_select(dr)
    dr.open(setting.login_page)
    # 用户名输入
    dr.send_keys("xpath", el.shop_login_name, data.shop_user)
    # 密码输入
    dr.send_keys("xpath", el.shop_login_pw_edit, data.shop_pw)
    # 点击登录按钮
    dr.get_element("xpath", el.shop_login_button).click()
    time.sleep(2)
    dr.open(setting.login_page_index)
    # 检查是否登录成功
    login_name = dr.get_text("xpath", el.shop_login_top_name)
    tc.assertEqual(data.shop_user, login_name, "login_error:登录用户名称校验失败")



if __name__ == "__main__":
    login_success()