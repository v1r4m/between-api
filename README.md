# between-api
* unofficial api document of [Between](https://between.us) from VCNC
* mainly reverse-engineered with `Requestly`
* I have nothing to do with VCNC Company, and this document is only for learning; Use these apis for your own risk.
* For chatting, you will need to set WebSocket Connection, or execute long-polling.
* Base URL : https://api-between.vcnc.co.kr

### 1. Authentication
* method : `GET`
* url : /authentication/getAccessTokenV2
```
curl --location --globoff --request GET \
'https://api-between.vcnc.co.kr/authentication/getAccessTokenV2?email=YourVeryFancyEmail%40YourEmail.com&password=YourVeryFancyPassword&session[type]=sessionType&session[name]=sessionName'
```
* request parameter

|parameter|value|remarks|
|--|--|--|
|email|your email address|Aware that you have to use `%40` instead of `@` since it is a curl command.
|password|your password|Not encrypted|
|session[type]|doesn't matter|ex)Windows. If you set the Between configuration to get an alarm when you get logged in on other devices, that device name can be this parameter's value, but I'm not 100% sure.|
|session[name]|doesn't matter|same above|
* response example
```
{
    "access_token": "SomeFancyAccessToken",
    "user_id": "SomeFancyId",
    "relationship_id": "MyLover'sID",
    "account_id": "SomeFancyAccountId",
    "session_id": "SomeFancySessionId",
    "expires_at": 1716104759760,
    "access_before_dormant": false
}
```

|parameter|value|remarks|
|--|--|--|
|access_token||you will need this in further api call, before the `expires_at` time.
|user_id||you will **mainly** use this id in your further api call.|
|relationship_id||your lover's Id. same above.|
|account_id||I'm not sure what's the great differences between account_id and user_id; but I assume that account_id never changes, whereas user_id changes when you exchange your lover.|
|session_id||you don't need this in most cases.|
|expires_at||Unix Time; **This is very short, it is nearly impossible to manually call the api back with token unless you write a script.** Although it's not accurate, I think it is about 1~2 seconds after the initial call.|
|access_before_dormant||?|

### 2. Get Endpoints