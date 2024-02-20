import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')

baseURL = 'https://api-between.vcnc.co.kr'
params = {
    'email':config['auth']['email'],
    'password':config['auth']['password'],
    'session[type]':'sessionType',
    'session[name]':'sessionName'
}

response = requests.get(baseURL + '/authentication/getAccessTokenV2', params=params)
accessToken = response.json()['access_token']
relationshipId = response.json()['relationship_id']
userId = response.json()['user_id']
accountId = response.json()['account_id']
print(accessToken)

headers = {
    'x-between-authorization':accessToken
}

response = requests.get(baseURL + '/info/endpoints', headers=headers)
print(response.json())

headers = {
    'x-between-authorization':accessToken,
}

response = requests.get(baseURL + '/'+relationshipId+'/views/status', headers=headers)
print(response.json())