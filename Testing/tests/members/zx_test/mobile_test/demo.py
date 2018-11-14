# coding=utf-8
import time
from ddt import ddt, data, unpack
import comallmobile
from core import constants
from setting.zx_test import setting
from setting.zx_test import el
from setting.zx_test.data import TestData

__author__ = 'zhangxue'

import unittest


@ddt
class MyTestCase(unittest.TestCase):

    d = TestData().get('demodata')

    def setUp(self):
        self.dr = comallmobile.ComallMobile(setting.desired_caps)


    @data(d[0])
    @unpack
    def test_something(self, name):

        # self.dr.click(constants.el_type_id, el.btn_index)
        location=self.dr.get_element(constants.el_type_id, el.btn_index).location
        login_button_location = [int(location['x'])+10, int(location['y']+5)]
        self.dr.tap([login_button_location])

        time.sleep(5)
        self.dr.switch_to_web()



        self.dr.send_keys(constants.el_type_xpath, el.et_input, name)

        self.dr.click(constants.el_type_id, el.btn_search)
        time.sleep(5)

        text = self.dr.get_text(constants.el_type_xpath, el.em_result)
        print text
        self.dr.assert_equal(text, name, '找不到。。。。', True, self.__class__.__name__)
        self.dr.switch_to_nat()
        self.dr.click_back()


        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
