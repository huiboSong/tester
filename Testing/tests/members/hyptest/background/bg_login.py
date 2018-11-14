# coding=utf-8

import unittest
import time
# 引入主框架文件
import comall

# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.hyptest import el
from setting.hyptest import setting

class bglogin(unittest.TestCase):
    def setUp(self):
        """初始化方法，在所有test执行前执行"""
        # 初始化浏览器对象，从setting文件中的driver_type读取启动浏览器的类型（ff\firefox、chrome、ie、opera等）
        self.dr = comall.Comall(setting.driver_type)
        time.sleep(1)
        # 最大化浏览器窗口
        self.dr.max_window()
        # 打开测试地址
        #self.dr.open(setting.bg_login_page)
        self.dr.open("http://172.31.1.251:8080/login")

    def test_first_case(self):
        """登录成功case"""
        # 获得setUp初始化的对象
        dr = self.dr
        # 输入用户名,密码,验证码
        dr.send_keys("xpath", el.bg_login_name, "heyanping")
        dr.send_keys("xpath", el.bg_login_password, "qwer12345")
        dr.send_keys("xpath", el.bg_vertifycode, "")
        dr.click("xpath", el.bg_login_button)
        #判断是否登录成功
        bg_user_name = dr.get_text("xpath", el.bg_username)
        self.assertEqual(bg_user_name, "heyanping", "后台登录成功")

    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        dr = self.dr
        dr.quit()

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(bglogin)
    result = unittest.TextTestRunner(verbosity=2).run(suite)