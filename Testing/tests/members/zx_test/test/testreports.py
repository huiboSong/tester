# coding=utf-8
__author__ = 'zhangxue'

import unittest


#测试用例

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    # def testCase1(self):
    #     self.assertEqual(2,2,"testError")
    #
    #
    # def testCase2(self):
    #     self.assertEqual(2,3,'<a href="IMG_7439.JPG">See picture</a>')
    #
    # def testCase3(self):
    #     self.assertEqual(2,5,"测试错误")

    def testCase4(self):
        self.assertEqual(2,1,"测试错误")

    def testCase5(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
