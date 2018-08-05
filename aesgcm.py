import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

def encrypt(key, plaintext, associated_data):
  aesgcm = AESGCM(key)
  nonce = os.urandom(16) #never reuse a nonce with a key
  #associated_data is authenticated with the key but not encrypted.
  ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)
  return ([aesgcm, nonce, ciphertext])

def decrypt(aesgcm, nonce, ciphertext, associated_data):
  return aesgcm.decrypt(nonce, ciphertext, associated_data)