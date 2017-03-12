#!/usr/bin/env python

# This code demonstrates how to register a new public key.
#
# Don't forget to store the returned Installation Token.
# The server public rsa key can always be retrieved as long
# as you have your private key and the token.

from bunq import API
from pprint import pprint

# private part of RSA key pair
key_file = 'rsa_bunq.pem'

with open(key_file, 'rb') as f:
    rsa_key = f.read()

bunq_api = API(rsa_key, None)

# using the pubkey() helper function to get public part of key pair
public_key = bunq_api.pubkey().decode()

# you will most probably want to store the token that is returned
r = bunq_api.query('installation', {'client_public_key': public_key})
pprint(dict(r.request.headers))
print()
pprint(dict(r.headers))
print()
pprint(r.json())
