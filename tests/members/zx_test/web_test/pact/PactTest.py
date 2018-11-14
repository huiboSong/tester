import json
import requests
from pact import Consumer, Provider
import comall

from setting.zx_test import setting

pact = Consumer('Consumer2').has_pact_with(Provider('Provider2'), 'localhost', port=setting.port)

import unittest


class pact_test(unittest.TestCase):
    expected = {
             'state_code': '0',
             'msg': 'suss'
        }
    path = '/get/test'

    def test_pact(self):

        (pact
         .given('get_test')
         .upon_receiving('a_get_test')
         .with_request(method='get', path=self.path,headers=setting.pact_headers)
         .will_respond_with(200, body=self.expected))
        pact.setup()
        # result = requests.get("http://localhost:"+str(setting.port)+"/" + self.path, headers=setting.pact_headers).json()
        api = comall.ComallApi("http://localhost:"+str(setting.port)+"/" + self.path, setting.pact_headers)
        re_data = api.http_request("get")
        print re_data

        self.assertEqual(self.expected,re_data[0])


        pact.verify()


    def tearDown(self):
        with open('consumer2-provider2.json') as json_file:
            json_data = json.load(json_file)
        data = json.dumps(json_data)
        result = requests.put("http://10.90.28.4:19092/pacts/provider/Provider2/consumer/Consumer2/version/1.0.0",
                              headers={
                                  "content-type": "application/json"
                              }, data=data).json()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(pact_test)
    result = unittest.TextTestRunner(verbosity=2).run(suite)


