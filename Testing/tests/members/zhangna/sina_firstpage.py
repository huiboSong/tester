# coding=utf-8
import unittest
# 引入主框架文件
import testgo
from ddt import ddt,unpack,data
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.zhangna import el
from setting.zhangna import setting
from setting.zhangna.data import TestData as dt
import time


@ddt
class TestCase(unittest.TestCase):

    d = dt().get("login")

    def setUp(self):
        # 启动浏览器
        self.dr = testgo.Hooli("chrome")
        self.dr.open(setting.sina_url)

    @data(d[0])
    @unpack
    def test_tt(self, username, password, message, my_email):
        dr = self.dr
        dr.until_page_load()
        # 输入用户名
        dr.send_keys("xpath", el.login_sinauser, username)
        time.sleep(1)
        # 输入密码
        dr.win_key("xpath", el.login_sinauser, "TAB")
        time.sleep(1)
        dr.send_keys("xpath", el.sina_login_pw_input, password)
        time.sleep(2)
        dr.click("xpath", el.login_submit_sinabt)
        time.sleep(3)

        first_name = dr.get_text("xpath", el.sina_login_success_show_username)
        self.assertEqual(my_email, first_name, message)


    def tearDown(self):
        self.dr.close()


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)