import os
from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# def RSA_private_key():
#   return rsa.generate_private_key(
#     public_exponent = 65537,
#     key_size = 2048,
#     backend = default_backend()
#     )

def private_key():
  return X25519PrivateKey.generate()

def get_shared_key(privKey, peerPubKey):
  return privKey.exchange(peerPubKey)

#derivation function: HKDF
#https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/?highlight=HKDF#cryptography.hazmat.primitives.kdf.hkdf.HKDF
def get_derived_key(info, sharedKey):
  salt = os.urandom(16)
  return HKDF(
     algorithm=hashes.SHA256(),
     length=32,
     salt = b'the random salt value as bytes',
     info = b'users name',
     #I'd like to convert both into bytes. This is the dream:
     # salt=bytes(salt, encoding='utf8'),
     # info=bytes(info, encoding='utf8'),
     backend=default_backend()
 ).derive(sharedKey)

def handshake(sender_name):
  privkey_sender = private_key()
  pubkey_sender = privkey_sender.public_key()

  privkey_receiver = private_key()
  pubkey_receiver = privkey_receiver.public_key()

  shared_key = get_shared_key(privkey_sender, pubkey_receiver)
  derived_key = get_derived_key(sender_name, shared_key)
  return derived_key
