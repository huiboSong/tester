# coding=utf-8
from logs.tests.members.zx_test.test.decimaltest import DecimalTest

__author__ = 'zhangxue'

import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        dec=DecimalTest()
        print dec.add("10.8923654573", "15.94895676575", )
        print dec.sub("19.126456567657734", "20.8676574576484",9)
        print dec.mul("19.12657457634", "20.844567457684")
        print dec.divide("1", "3")
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
