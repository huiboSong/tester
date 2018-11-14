# coding=utf-8
from setting.zx_test import setting
import comallmobile
from setting.zx_test import el

__author__ = 'zhangxue'

import time
import unittest

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class AppTest(unittest.TestCase):
    def setUp(self):

        self.dr = comallmobile.ComallMobile(setting.desired_caps)

    def test_dpApp(self):
        # 需要执行的case
        actM = self.dr.get_current_activity()
        # 切换到最新的web视图
        time.sleep(5)
        while (True):
            self.dr.switch_to_web()
            if (self.dr.is_element_exists('xpath',
                                          el.index_btn)):
                break
            else:
                self.dr.swipe_left()
                time.sleep(5)
        self.dr.switch_to_web()
        time.sleep(5)
        if (self.dr.is_element_exists('xpath',
                                      el.btn_no_login)):
            self.dr.click('xpath',
                          el.btn_no_login)
            # 登录开始
            # time.sleep(5)
            # self.dr.click('xpath', '/html/body/ion-nav-view/ion-view/ion-tabs/div/a[5]')
            # time.sleep(5)
            # self.dr.click('xpath',
            # '/html/body/ion-nav-view/ion-view/ion-tabs/ion-nav-view/ion-view/ion-content/div[1]/div/div[3]/div[1]/p')
            # time.sleep(5)
            # self.dr.send_keys('xpath',
            # '/html/body/div[3]/div[2]/ion-modal-view/ion-content/div[1]/form/div[1]/label[1]/input',
            # '18518915432')
            # time.sleep(2)
            # self.dr.send_keys('xpath',
            # '/html/body/div[3]/div[2]/ion-modal-view/ion-content/div[1]/form/div[1]/label[2]/input',
            # 'zx404521')
            # time.sleep(5)
            # self.dr.click('xpath', '/html/body/div[3]/div[2]/ion-modal-view/ion-content/div[1]/form/div[2]/button')
            # time.sleep(10)
            # self.dr.click('xpath', '/html/body/ion-nav-view/ion-view/ion-tabs/div/a[1]')
            # 登录结束

        self.dr.click('xpath',
                      el.limit_time_one)
        time.sleep(5)
        self.dr.click('xpath',
                      el.limit_time_list_one)

        time.sleep(5)
        self.dr.switch_to_nat()
        for i in range(1, 4, 1):
            self.dr.swipe_top()
            time.sleep(2)

        self.dr.switch_to_web()



        # self.find_toast("login",10,0.5,self.driver)
        # def tearDown(self):
        # self.driver.quit() #case执行完退出


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)  # 执行case集
