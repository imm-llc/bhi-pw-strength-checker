#!/usr/bin/env python3
import requests, json, hashlib
from sys import argv
# Tool to check PW hashes against Pwned Passwords

def main_func(password):
    

    password = password.encode('utf-8')

    PWHASH = hashlib.sha1(password).hexdigest().upper()
    PwndedHashPrefix = PWHASH[0:5]
    PwndedHashSuffix = PWHASH[5:]


    HEADERS = {'User-Agent': 'BHI Pwned PW Checker'}

    r = requests.get("https://api.pwnedpasswords.com/range/"+PwndedHashPrefix, headers=HEADERS)

    if r.status_code != 200:
        return "There was an error checking this password against Have I Been Pwned"


    for line in r.text.splitlines():
        hashSuffix, count = line.split(':')

        if hashSuffix == PwndedHashSuffix:
            return str(count)
        else:
            return 0

