#!/usr/bin/env python

# This example uses a previously registered public key and related
# Installation token to create a new Session and retrieve the current
# Balance of the first account of the first user connected to the
# given api key

from bunq import API
from pprint import pprint

# installation token
i_token = 'xxxx'

# private part of rsa key pair
key_file = 'rsa_bunq.pem'

api_key = 'xxxx'

with open(key_file, 'rb') as f:
    rsa_key = f.read()

# we're using verification here, use the server_key belonging to the token used
server_key = '-----BEGIN PUBLIC KEY-----\nxxxxxx\n-----END PUBLIC KEY-----\n'
bunq_api = API(rsa_key, i_token, server_key=server_key)

# First create new session and retrieve its token, using installation token
# you could already have a session token you could use here instead
r = bunq_api.query('session-server', {'secret': api_key}, verify=True)
if r.status_code == 200:
    res = [x for x in r.json()['Response'] if list(x)[0] == 'Token'][0]
    bunq_api.token = res['Token']['token']

# Retrieve the id of the first user of this account
r = bunq_api.query('user', verify=True)
if r.status_code == 200:
    res = [x for x in r.json()['Response'] if list(x)[0] == 'UserPerson'][0]
    user_id = res['UserPerson']['id']

# Retrieve balance of first account of first user
r = bunq_api.query('user/%s/monetary-account-bank' % user_id, verify=True)
if r.status_code == 200:
    acc_type = 'MonetaryAccountBank'
    res = [x for x in r.json()['Response'] if list(x)[0] == acc_type][0]
    acc = res[acc_type]
    print('%s: %s %s' % (
        acc['description'],
        acc['balance']['value'],
        acc['balance']['currency']
    ))
