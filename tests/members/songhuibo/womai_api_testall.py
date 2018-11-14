# # coding=utf-8
#
# import unittest
# import doctest
# import xmlrunner
#
# # 这是固定的,不用改,是用doctest搜索和查询test开头的方法
# finder = doctest.DocTestFinder(verbose=False, exclude_empty=False)
# suite = doctest.DocTestSuite(test_finder=finder)
#
# # 需要改的,加文件名和里面的类名
# # 引入这些文件(python的包)
# from tests.TestCase.api_1_0.Indeximport
# # 把这些包里的类加入到一个测试集合里面,这个集合是suite
# suite.addTest(unittest.makeSuite(_testcapi.ApiByNewGetIndexInfoTest))
# suite.addTest(unittest.makeSuite(_testcapi.songhuibo))
#
# # 生成xml测试报
# xmlrunner.XMLTestRunner(output='test-reports').run(suite)