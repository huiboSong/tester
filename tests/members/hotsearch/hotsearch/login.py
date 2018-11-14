# coding=utf-8

import sys
import time

# 引入主框架文件
import comall
import pyse
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hotsearch import el
from setting.hotsearch import setting
import setting.hotsearch.data as dat

def login_success(dr,dc):
    #打开后台登录页
    #dr=comall.Comall(setting.driver_type)
    dr.open(setting.back_page)
    time.sleep(1)
    dr.send_keys("xpath",el.login_user_edit,dat.login_name)
    dr.send_keys("xpath",el.login_pw_edit,dat.login_pw)
    dr.click("xpath",el.login_submit_btn)
    time.sleep(2)
    login_name=dr.get_text("xpath",el.dashboard_top_name_span)
    dc.assertEqual(dat.login_name,login_name,dat.suc_failed)

def area_select(dr):
    #首页地区选择
    dr.open(setting.front_page)
    time.sleep(1)
    dr.click("xpath",el.select_address_show)
    dr.click("xpath",el.select_city)
    dr.click("xpath",el.select_area)
    dr.click("xpath",el.start_shop_btn)
    time.sleep(1)

# if __name__ == "__main__":
#     login_success()



