# -*- coding: utf-8 -*-
import requests # HTTP request lib http://docs.python-requests.org/en 
import json

# RNS API
# Get vehicles types method 
# Works without authentication

print (" Vehicles types \n com.rnis.dictionary.action.list")

#url = 'https://api.rnis.mosreg.ru/ajax/request' # Production server. Swith the server in case of time out
url = 'https://dev-rnis.t1-group.ru/ajax/request' # Development server

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Subject': 'com.rnis.dictionary.action.list'
    }

auth = {
    "headers":{
        "version":"1.0",
        "requester":"web",
        "token":"",
        "meta":[]
        },
    "payload":{
        "dictionary":{
            "key":"vehicle_types"
            }
        }
    }

response = requests.post(url,headers=headers, json = auth) # Make the request

print(response) # Output server response code. 200 - OK, 500,504 etc. - error
print(json.loads(str(response.text))) # parse json payload
