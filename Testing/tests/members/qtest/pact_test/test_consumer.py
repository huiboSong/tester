import atexit

from pact import Consumer, Provider

from logs.tests.members.qtest.pact_test.consumer import is_up


pact = Consumer('consumer').has_pact_with(Provider('provider'))
pact.start_service()
atexit.register(pact.stop_service)


def test_client():
    url = 'http://localhost:1234'
    pact.given(
        'a url'
    ).upon_receiving(
        'a request to that url'
    ).with_request(
        'get',
        '/'
    ).will_respond_with(200)

    with pact:
        assert is_up(url)
