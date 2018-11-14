__author__ = 'sun'
import comall
import unittest
import time
from setting.swptest import setting
from setting.swptest import el
from setting.swptest.data import TestData
from ddt import ddt, data, unpack


@ddt
class Register(unittest.TestCase):
    register_data = TestData().get("wm_register")

    def setUp(self):
        self.dr = comall.Comall(setting.driver_type)
        self.dr.max_window()

    @data(register_data[0])
    @unpack
    def testRegister(self, mailorphone, userid, pwd, pwd2, validateCode):
        dr = self.dr
        dr.open(setting.womai_onlien_register_url)
        dr.send_keys("xpath", el.register_MailorPhone, mailorphone)
        dr.send_keys("xpath", el.register_loginid, userid)
        dr.send_keys("xpath", el.register_pwd, pwd)
        dr.send_keys("xpath", el.register_pwd2, pwd2)
        dr.send_keys("xpath", el.register_validateCode, validateCode)
        dr.click("xpath", el.register_registerbtn)

    def tearDown(self):
        dr = self.dr
       # dr.quit()
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Register)
    result = unittest.TextTestRunner(verbosity=2).run(suite)