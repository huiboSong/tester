# coding=utf-8
__author__ = "song"
__project__ = "hooli"
import testgo,hashlib,unittest
from setting.test_test import setting
from setting.test_test.data import TestData as dt
from ddt import ddt, data, unpack
import sys
type = sys.getfilesystemencoding()
@ddt
class login(unittest.TestCase):
    '''字符串拼接'''
    dict = setting.hooli_header
    value = dict.get('t')  + dict.get('v') + dict.get('c') + dict.get('Encryp-Token') + dict.get('l') + dict.get('apiVersion') + '#hoolihome#'
    key ="".join((lambda x:(x.sort(),x)[1])(list ('t'  + 'v' + 'c' + 'Encryp-Token' + 'apiVersion')))
    value1 = (key + value)
    def md5(str):
        '''md5加密方法'''
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    f = (md5(md5(value)).upper() + '#hoolihome#').upper()
    setting.hooli_header.update({'Encryp-Token': f})
    # m = dt().get("hooli")
    # @data(m[0])
    # @unpack
    # def test (self):
    #     request_url = setting.hooli_url + "napi/user/msg-login"
    #     request_body_json = {"params":{"mobile":13520843514,"countryId":'wewew',"password":123456}}
    #     test = test.hooliApi(request_url, setting.hooli_header)
    #     return_data = test.http_request("get", request_body_json)
    #     print (setting.hooli_header)
if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(login)
        result = unittest.TextTestRunner(verbosity=2).run(suite)

