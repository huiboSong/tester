import atexit
import unittest
import json

import requests
from pact import Consumer, Provider

from logs.tests.members.qtest.pact_test.consumer import user


pact = Consumer('Consumer3').has_pact_with(Provider('Provider3'))
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("UpClass")

    def test_get_user(self):
        print("test_get_user")
        expected = {
            'username': 'UserA',
            'id': 123,
            'groups': ['Editors']
        }

        (pact
         .given('UserA exists and is not an administrator')
         .upon_receiving('a request for UserA')
         .with_request('get', '/users/UserA')
         .will_respond_with(200, body=expected))

        with pact:
            result = user('UserA')

        self.assertEqual(result, expected)

    def test_shipment_completions(self):
        print("test_shipment_completions")
        headers = {
            "content-type": "application/json",
            "access-token": "access-token"
        }
        path = '/targets/shipment/completions'
        expected = {
            'title': 'FY1718',
            'target_value': "20000",
            'completed': "96"
        }
        (pact
         .given('shipment')
         .upon_receiving('a request for shipment')
         .with_request(method='get', path=path, headers=headers)
         .will_respond_with(200, body=expected))

        with pact:
            result = requests.get("http://localhost:1234/" + path, headers=headers).json()

        self.assertEqual(result, expected)

    @classmethod
    def tearDownClass(cls):
        with open('consumer3-provider3.json') as json_file:
            json_data = json.load(json_file)
        data = json.dumps(json_data)
        result = requests.put("http://10.90.28.4:19092/pacts/provider/Provider3/consumer/Consumer3/version/1.0.0",
                              headers={
                                  "content-type": "application/json"
                              }, data=data).json()
        print("DownClass")


if __name__ == '__main__':
    unittest.main()
