# coding=utf-8

import unittest
import time
from ddt import ddt, data, unpack
# 引入主框架文件
import comall
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.example import el
from setting.example import setting
from setting.example.data import TestData as dt

import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


@ddt
class Module(unittest.TestCase):
    d = dt().get("login")

    def setUp(self):
        """初始化方法，在所有test执行前执行"""
        # 初始化浏览器对象，从setting文件中的driver_type读取启动浏览器的类型（ff\firefox、chrome、ie、opera等）
        self.dr = comall.Comall(setting.driver_type)
        # 最大化浏览器窗口
        self.dr.max_window()
        time.sleep(1)

    @data(d[0])
    @unpack
    def test_first_case(self, user_name, user_pw, failed_msg):
        u"""xxx测试case，必须以test开头命名"""

        # 获得setUp初始化的对象
        dr = self.dr
        # 打开后台登录地址
        dr.open(setting.login_page)
        time.sleep(1)
        # 检查登录输入框存在
        dr.until("xpath", el.login_user_edit)
        # 用户名输入
        dr.send_keys("xpath", el.login_user_edit, user_name)
        # 密码输入
        dr.send_keys("xpath", el.login_pw_edit, user_pw)
        # 点击登录按钮
        dr.click("xpath", el.login_submit_btn)
        time.sleep(2)
        # 检查是否登录成功
        login_name = dr.get_text("xpath", el.dashboard_top_name_span)
        self.assertEqual(user_name, login_name, failed_msg)

    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Module)
    result = unittest.TextTestRunner(verbosity=2).run(suite)