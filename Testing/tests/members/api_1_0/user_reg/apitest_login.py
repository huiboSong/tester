# coding=utf-8

import unittest
import time
# 引入主框架文件
import testgo
import requests, json
# 引入配置文件（el=对象库，setting=配置文件,data=数据文件）
from setting.api_1_0 import el
from setting.api_1_0 import setting as set
from setting.api_1_0 import data


class user_reg(unittest.TestCase):
    def setUp(self):
        """初始化方法，在所有test执行前执行"""
        # 初始化接口测试类
        self.call = testgo.testApi()
        time.sleep(1)

    def test_verifyExistsUser_01(self):
        u"""用户注册接口-用户名已经存在接口-测试"""

        # 获得setUp初始化的对象
        call = self.call

        sign = True
        errormsg = []
        errorcasename = []
        datas = data.verifyExitsUser_data
        postparams = ''
        headers = call.get_headers()

        for i in range(1, len(datas)+1):
                getparams = data.get_param(i)
                verifyExitsUser_response = call.apicall("GET", set.base_url+'/user/verifyExitsUser', getparams, postparams, headers)
                print verifyExitsUser_response[2]
                try:
                    if verifyExitsUser_response[1] != 200:
                        sign = False
                        errormsg.append("请求发出后，服务器接收失败")
                    else:
                        if verifyExitsUser_response[0]['stateCode'] != data.get_stateCode(i):
                            sign = False
                            errorcasename.append(data.get_case_name(i))
                        else:
                            if verifyExitsUser_response[0]['stateCode'] == 0:
                                print u'用户名存在时，接口返回值正确'
                                print u"服务器返回信息为%s" % (verifyExitsUser_response[2])
                            if verifyExitsUser_response[0]['stateCode'] == 2:
                                if verifyExitsUser_response[0]['message'] != data.get_message(i):
                                    sign = False
                                    errorcasename.append(data.get_case_name(i))
                                    errormsg.append(verifyExitsUser_response[0]['message'])
                                else:
                                    print "当前Case名称为:%s" % (data.get_case_name(i))
                                    print u"服务器返回信息为:%s" % (verifyExitsUser_response[2])

                except Exception, e:
                    raise e

        if sign:
            print u"接口 /user/verifyExitsUser ———————————— OK"
        else:
            print u"接口 /user/verifyExitsUser ———————————— Failure"
        for cname in errorcasename:
            print cname

        assert sign


    def tearDown(self):
        """稀构方法，在所有tests执行完毕后，执行"""
        pass

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(user_reg)
    result = unittest.TextTestRunner(verbosity=2).run(suite)