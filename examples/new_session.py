#!/usr/bin/env python

# This code shows how to open a new session.
#
# Use a private key and accompanying installation token you
# received earlier.

from bunq import API
from pprint import pprint

# installation token
token = 'xxx'

# private part of rsa key pair
key_file = 'rsa_bunq.pem'

# key created in the app
api_key = 'xxx'

with open(key_file, 'rb') as f:
    rsa_key = f.read()

bunq_api = API(rsa_key, token)

r = bunq_api.query('session-server', {'secret': api_key})

# r.json()['Response'][1]['Token'] would work too, but I mistrust predefined
# order, never know when someone starts shuffling things around
if r.status_code == 200:
    pprint([x for x in r.json()['Response'] if list(x)[0] == 'Token'][0])
else:
    pprint(r.json()['Error'][0])
