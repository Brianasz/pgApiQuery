#!/usr/local/bin/python3

# MODULES

import requests

# VARIABLES

domain = input("Introduce your company domain: ")
authorization_token = input("Introduce your authentication token: ")

# AUTHENTICATION TO THE API
pagerduty_session = requests.Session()
pagerduty_session.headers.update({'Authorization': 'Token token=' + authorization_token, 'Accept': 'application/vnd.pagerduty=json;version=2'})
pagerduty_session.get('https://{domain}.pagerduty.com/users')

# ANOTHER AUTHENTICATION METHOD

headers = { 'Authorization': 'Token token={authorization_token}' }
response = requests.get('https://{domain}.pagerduty.com/api/v1/incidents'), headers=headers)
print response.status_code
#pg_api_session = pagerduty_session.get('https://{domain}.pagerduty.com/api/v1/incidents')
#print(pg_api_session.text)

# SEARCH PARAMETERS

#response = requests.get("https://{domain}.pagerduty.com/api/v1/incidents")
#print(response.status_code)
