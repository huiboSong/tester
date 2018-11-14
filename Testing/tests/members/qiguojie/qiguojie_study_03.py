# coding = utf-8

import comall
import time
import unittest
import setting.qiguojie.setting as my_set
from setting.qiguojie import data
from setting.qiguojie import el


class QiGuoJieTest(unittest.TestCase):

    def setUp(self):
        self.dr = comall.Comall(my_set.driver_type)
        self.dr.open(my_set.local_url)
        self.dr.max_window()
        time.sleep(3)

    def test_next_window(self):
        qq = self.dr
        qq.click("xpath", el.localhost_open_window_a)

        qq.switch_next_window()

        qq.send_keys("xpath", "//*[@id='kw']", "qiguojie")

        qq.click("xpath", "//*[@id='su']")


    def tearDown(self):
        # qq = self.dr
        # qq.quit()
        pass


# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)