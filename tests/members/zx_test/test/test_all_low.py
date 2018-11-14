# coding=utf-8
# zhangxue #
import HTMLTestRunnerCN

import unittest
import doctest
import sys

from logs.tests.members.zx_test.test import testreports

from logs.tests.members.zx_test.web_test.api_test import api_indexdata

reload(sys)
sys.setdefaultencoding("utf-8")

finder = doctest.DocTestFinder(verbose=False, exclude_empty=False)
suite = doctest.DocTestSuite(test_finder=finder)

# 添加TestCases------------------

suite.addTest(unittest.makeSuite(api_indexdata.Index_Data))

suite.addTest(unittest.makeSuite(testreports.MyTestCase))

# # 打开一个文件，将result写入此file中
filePath ='reports/resultnew.html'
fp = file(filePath,'wb')
# fp = open("reports/resultnew.html", 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
runner.run(suite)
fp.close()

# xmlrunner.XMLTestRunner(output='test-reports').run(suite)