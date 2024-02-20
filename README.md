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
|relationship_id||your relationship's Id. same above.|
|account_id||I'm not sure what's the great differences between account_id and user_id; but I assume that account_id never changes, whereas user_id changes when you exchange your lover.|
|session_id||you don't need this in most cases.|
|expires_at||Unix Time; **This is very short, it is nearly impossible to manually call the api back with token unless you write a script.** I think it is about 1~2 seconds after the initial call.|
|access_before_dormant||?|

### 2. Get Endpoints
* method : `GET`
* url : /info/endpoints
```
curl --location --request GET 'https://api-between.vcnc.co.kr/info/endpoints' \
--header 'x-between-authentication: yourFancyToken' 
```

* request header

|header|value|remarks|
|--|---|--|
|x-between-authentication|yourFancyAccessToken||

* response example
```
{
	"message":[
		"between+ssl://msg-between.between.us:5683/?timeout_millis=420000",
		"between+ssl://msg-between.between.us:443/?timeout_millis=420000"
	],
	"websocket":[
		"wss://ws-between.between.us:443/?timeout_millis=60000"
	],
	"push":[
		"between+ssl://push-between.between.us:5683/?timeout_millis=900000",
		"between+ssl://push-between.between.us:443/?timeout_millis=900000"
	]
}
```
|parameter|value|remarks|
|--|--|--|
|message|||
|websocket|||
|push|||

### 3. some fun metadata
* method : `GET`
* url : '/`yourUser_id`/views/status
```
curl --location --request GET 'https://api-between.vcnc.co.kr/yourFancyRelationship_id/views/status' \
--header 'x-between-authentication: yourFancyToken' 
```
* request parameter

|header|value|remarks|
|--|---|--|
|x-between-authentication|yourFancyAccessToken||

* response example
```
{
	"relationship":{
		"id":"--",
		"members":[
			{
				"user_id":"--",
				"account_state":"ACTIVE_RELATIONSHIP",
				"account_id":"--"
			},
			{
				"user_id":"--",
				"account_state":"ACTIVE_RELATIONSHIP",
				"account_id":"--"
			}
		],
		"relationship_state":"ACTIVE",
		"used_premium_trial":false,
		"profile_photo_decoration":{
			"content":{
				"id":"default",
				"type":"EMPTY",
				"animated":false,
				"badge":false
			},
			"overrides_special_version":0
		},
		"created_time":1708241395996
	},
	"users":[
		{
			"id":"--",
			"gender":"MALE",
			"locale":"ko_KR",
			"timezone":32400000,
			"email":"--",
			"nickname":"--",
			"profile_photo":{
				"height":1773,
				"width":1773,
				"source":"--",
				"images":[
					{
						"height":1773,
						"width":1773,
						"source":"--"
					}
				],
				"created_time":0,
				"base_url":"--"
			},
			"placemark":{
				"city_name":"--",
				"timezone_name":"+09:00",
				"timezone_offset":32400000
			},
			"birthdate":"--",
			"birthdate_anniversary_id":"--",
			"holiday_countries":[
				"KR"
			],
			"relationship_id":"--",
			"account_id":"--",
			"relationship_state":"ACTIVE",
			"account_state":"ACTIVE_RELATIONSHIP",
			"email_confirmed":true
		},
		{
			"id":"--",
			"gender":"FEMALE",
			"locale":"ko-KR",
			"timezone":32400000,
			"email":"--@gmail.com",
			"nickname":"은진",
			"profile_photo":{
				"height":300,
				"width":300,
				"source":"https://d1g6iinm2hj5oi.cloudfront.net/profile/v3/bg_profile_placeholder_300.png",
				"images":[
					{
						"height":150,
						"width":150,
						"source":"https://d1g6iinm2hj5oi.cloudfront.net/profile/v3/bg_profile_placeholder_150.png"
					},
					{
						"height":300,
						"width":300,
						"source":"https://d1g6iinm2hj5oi.cloudfront.net/profile/v3/bg_profile_placeholder_300.png"
					}
				],
				"created_time":1707604736534,
				"is_default":true
			},
			"placemark":{
				"city_name":"서울특별시",
				"timezone_name":"+09:00",
				"timezone_offset":32400000
			},
			"birthdate":"1998-05-09",
			"birthdate_anniversary_id":"--",
			"holiday_countries":[
				"KR"
			],
			"relationship_id":"--",
			"account_id":"--",
			"relationship_state":"ACTIVE",
			"account_state":"ACTIVE_RELATIONSHIP",
			"email_confirmed":false
		}
	],
	"memory_count":2,
	"account":{
		"id":"--",
		"email":"--@gmail.com",
		"active_user_id":"--",
		"active_relationship_id":"--",
		"locale":"ko-KR",
		"timezone":32400000,
		"mcc":450,
		"country_code":"KR",
		"account_state":"ACTIVE_RELATIONSHIP",
		"email_confirmed":false,
		"email_validation_status":"VALID",
		"pin_enabled":true
	},
	"weathers":{
		"--":{
			"state":"FILLED",
			"weather_state":"CLOUDS",
			"celsius":9.0,
			"fahrenheit":49.0,
			"forecasts":[
				{
					"date":"2024-02-19",
					"weather_state":"RAIN",
					"max":{
						"c":10.0,
						"f":50.0
					},
					"min":{
						"c":3.0,
						"f":38.0
					},
					"hourly":[
						{
							"hour":12,
							"temperature":{
								"c":9.0,
								"f":49.0
							},
							"weather_state":"CLOUDS",
							"is_day":false,
							"time":1708311600000
						},
						{
							"hour":13,
							"temperature":{
								"c":10.0,
								"f":50.0
							},
							"weather_state":"CLOUDS",
							"is_day":false,
							"time":1708315200000
						},
						{
							"hour":14,
							"temperature":{
								"hour":23,
								"temperature":{
									"c":-3.0,
									"f":26.0
								},
								"weather_state":"CLEAR",
								"is_day":false,
								"time":1709301600000
							}
						]
					}
				]
			}
		},
		"title_anniversary":{
			"id":"--",
			"date":"--",
			"method":"CM_DAY_ONE",
			"description":"처음 만난 날",
			"as_title":true,
			"from":"--",
			"type":"DAY_WE_FIRST_MET",
			"recurrent":false
		},
		"account_preference":{
			"email_settings":{
				"disallow_promotion_email":false
			},
			"enable_login_notification":true,
			"enable_notification_ads":false,
			"enable_notification_ads_updated_at":1708309526256,
			"agree_personalized_marketing":false
		},
		"user_preference":{
			"push_settings":{
				"preview_message":true
			},
			"ad_settings":{
				"disable_notification_ads":false
			},
			"disable_notification_ads":false,
			"disable_inhouse_ads":false,
			"sticker_set_order":[
				"200",
				"424",
				"425",
				"426",
				"427",
				"202"
			]
		},
		"covers":{
			
		},
		"profile_photo_decoration":{
			"decoration_id":"DEFAULT",
			"use_special_day":false
		}
	}
```
* `--` is the one censored.