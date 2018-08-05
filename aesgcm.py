import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt(key, message, auth):
  aesgcm = AESGCM(key)
  nonce = os.urandom(128//8)
  print("nonce:", type(nonce))
  ciphertext = aesgcm.encrypt(nonce, message, auth)
  return ([aesgcm, nonce, ciphertext])

def decrypt(aesgcm, nonce, ciphertext, auth):
  return aesgcm.decrypt(nonce, ciphertext, auth)