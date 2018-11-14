# coding=utf-8

import unittest
import time
from ddt import ddt, data, unpack
# 引入主框架文件
import comall
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.dongshasha import el
from setting.dongshasha import setting
from setting.dongshasha.data import TestData as dt

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class TestCase(unittest.TestCase):

    def setUp(self):
        """初始化方法，在所有test执行前执行"""
        # 初始化浏览器对象，从setting文件中的driver_type读取启动浏览器的类型（ff\firefox、chrome、ie、opera等）
        self.dr = comall.Comall(setting.driver_type)
        # 最大化浏览器窗口
        self.dr.max_window()
        # 打开后台登录地址
        self.dr.open(setting.login_url)
        time.sleep(5)
    def test_login(self):
        # 获得setUp初始化的对象
        dr = self.dr
        #首页点击登录，进入登录页面
        dr.click("xpath",el.beiguo_index_login_a)
        #登录页面，输入登录名
        dr.send_keys("xpath",el.beiguo_login_loginname_txt,"13503115675")
        #登录页面，输入密码
        dr.send_keys("xpath",el.beiguo_login_password_txt,"123456")
        #登录页面，点击登录按钮
        dr.click("xpath",el.beiguo_login_submit_btn)
        user_name = dr.get_text("xpath",el.beiguo_login_username_span)
        self.assertEqual("万马九天，您好!",user_name,"用户登录失败")




    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        pass

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)