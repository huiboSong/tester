import atexit

import requests
from pact import Consumer, Provider


pact = Consumer('Consumer2').has_pact_with(Provider('Provider2'))
pact.start_service()
atexit.register(pact.stop_service)



def test_shipment_completions():
    print("testtest")
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
    pact.setup()
    result = requests.get("http://localhost:1234/" + path, headers=headers).json()
    pact.verify()

if __name__ == '__main__':
   test_shipment_completions();
   print("asdfasdfasdf")

