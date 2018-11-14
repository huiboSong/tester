#coding=utf-8
import time

from setting.zx_test import el, setting
from setting.zx_test import data


__author__ = 'Zx'


def login(dr):
    dr.open(setting.login_page)
    time.sleep(1)
    dr.until("xpath",el.login_user_edit)
    dr.send_keys("xpath",el.login_user_edit,data.TestData().get('user')[0][0])
    dr.send_keys("xpath",el.login_psw_edit,data.TestData().get('user')[0][1])
    dr.click("xpath",el.login_btn_login)
    time.sleep(2)

