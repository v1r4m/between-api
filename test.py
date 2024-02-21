import requests
import json
import websocket
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Process email and password.')
parser.add_argument('email', type=str, help='Email for authentication')
parser.add_argument('password', type=str, help='Password for authentication')
args = parser.parse_args()

baseURL = 'https://api-between.vcnc.co.kr'
params = {
    'email': args.email,
    'password': args.password,
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
def on_message(ws, message):
    print("Received message:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(wsapp, close_status_code, close_msg):
    # Because on_close was triggered, we know the opcode = 8
    print("on_close args:")
    if close_status_code or close_msg:
        print("close status code: " + str(close_status_code))
        print("close message: " + str(close_msg))

def on_open(ws):
    print("### Connection opened ###")
websocketApp = websocket.WebSocketApp('wss://ws-between.between.us:443/?timeout_millis=60000'+relationshipId+'/ws?access_token='+accessToken,
                                      on_message=on_message,
                                      on_error=on_error,
                                      on_close=on_close,
                                      on_open=on_open)
websocketApp.run_forever()