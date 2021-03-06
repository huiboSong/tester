# coding=utf-8


import unittest
import doctest

# 加载 module目录的所有测试脚本
from logs.tests.members.api_1_0.user_reg import apitest_login
import xmlrunner

import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

finder = doctest.DocTestFinder(verbose=False, exclude_empty=False)
suite = doctest.DocTestSuite(test_finder=finder)

# 把所有测试脚本加入测试套件suite（测试计划执行的脚本）
suite.addTest(unittest.makeSuite(apitest_login.user_reg))


# 生成xml测试报告
xmlrunner.XMLTestRunner(output='test-reports').run(suite)