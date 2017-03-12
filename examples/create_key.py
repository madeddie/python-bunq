#!/usr/bin/env python

# Use this code to generate a new RSA private key
#
# From the private key a public key can be retrieved at any time.
# Don't forget to store the output.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# output PEM encoded version of private key
print(private_key.private_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PrivateFormat.PKCS8,
  encryption_algorithm=serialization.NoEncryption()
).decode())

# output PEM encoded version public part of private key
print(private_key.public_key().public_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode())
