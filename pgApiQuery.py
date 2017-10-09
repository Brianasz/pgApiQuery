#!/usr/local/bin/python3

# MODULES

import requests

# VARIABLES

domain = input("Introduce your company domain: ")
authorization_token = input("Introduce your authentication token: ")


# SEARCH TO THE API
headers = {
  'Authorization': 'Token token={0}'.format(authorization_token),
  'Content-type': 'application/json',
}
payload = {
  'status':'resolved'
}

r = requests.get(
  'https://{0}.pagerduty.com/api/v1/incidents'.format(domain),
  headers=headers,
  params=payload,
)

print(r.status_code)
print(r.text)
