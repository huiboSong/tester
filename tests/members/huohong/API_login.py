# coding=utf-8
import comall
import unittest
from setting.huohong import setting
from setting.huohong import data
from setting.huohong  import el

class WomaiLoginApiTest(unittest.TestCase):

    myname = data.username
    mypwd = data.pwd

    print "1"
    def test_user_info_get(self):
        # 请求的uri拼写；api接口的通用uri放在config中保存
        request_uri = setting.api_uri + "/loginnew"
        print "2"
        # 请求的数据体
        request_body_data_json = {"username": self.myname,"password": self.mypwd}

        print setting.womaiapi_header
        # comallApi实例化
        womaiapi = comall.ComallApi(request_uri,setting.womaiapi_header)
        print "3"
        # 发送http请求，把处理后的数据返回给return_data
        return_data = womaiapi.http_request("post", request_body_data_json)
        print "hello"
        print return_data
        login_message = return_data[0]['userid']
        print "hello1"
        self.assertEqual("49740467", str(login_message), "successed")



        # 下面是脚本单独调试所需代码
        if __name__ == "__main__":
            suite = unittest.TestLoader().loadTestsFromTestCase(WomaiLoginApiTest)
            result = unittest.TextTestRunner(verbosity=2).run(suite)










