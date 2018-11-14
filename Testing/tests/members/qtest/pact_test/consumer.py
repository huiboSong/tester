import requests

def is_up(url):
    return requests.get(url).status_code == 200

def user(user_name):
    uri = 'http://localhost:1234/users/' + user_name
    return requests.get(uri).json()
