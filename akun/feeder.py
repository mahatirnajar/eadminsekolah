import requests
import json
from akun import config


def runWS(myobj):
    url = config.load('FEEDER_URL')
    x = requests.post(url, json=myobj)
    return json.loads(x.text)

def token():
    res = runWS({
        'act': 'GetToken',
        'username': config.load('FEEDER_USERNAME'),
        'password': config.load('FEEDER_PASSWORD')})
    return res['data']['token']


def get(act, filter='', limit='', offset=''):
    params = {'act': act, 'token': token(), 'filter': filter,
              'limit': limit, 'offset': offset}
    return runWS(params)


def insert(act, record):
    params = {'act': act, 'token': token(), 'record': record}
    return runWS(params)


def update(act, key, record):
    params = {'act': act, 'token': token(), 'key': key, 'record': record}
    return runWS(params)


def delete(act, key):
    params = {'act': act, 'token': token(), 'key': key}
    return runWS(params)
