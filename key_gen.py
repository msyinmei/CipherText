import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

#X25519 key generation
#https://github.com/pyca/cryptography/blob/master/src/cryptography/hazmat/primitives/asymmetric/x25519.py
#https://github.com/pyca/cryptography/blob/3cd630b325372c3ad05d9fb2ea816db13d9d8584/src/cryptography/hazmat/backends/openssl/backend.py#L1924 
def private_key():
  return X25519PrivateKey.generate()

#used in handshake, abstract method on X25519PrivateKey object
#https://github.com/pyca/cryptography/blob/3cd630b325372c3ad05d9fb2ea816db13d9d8584/src/cryptography/hazmat/primitives/asymmetric/x25519.py#L52
def get_shared_key(privKey, peerPubKey):
  return privKey.exchange(peerPubKey)

#used in handshake
#derivation function: HKDF
#https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/?highlight=HKDF#cryptography.hazmat.primitives.kdf.hkdf.HKDF
def get_derived_key(info, sharedKey):
  salt = os.urandom(16)
  return HKDF(
     algorithm=hashes.SHA256(),
     length=32,
     salt = salt,
     info = info,
     # python3:
     # salt=bytes(salt, encoding='utf8'),
     # info=bytes(info, encoding='utf8'),
     backend=default_backend()
 ).derive(sharedKey)

def handshake(sender_name):
  # In a real handshake the pubkey_receiver will be received from the
  # other party. For this example we'll generate some arbitrary private and public keys.
  # Note that in a DH handshake both peers must agree on a common set of parameters.
  privkey_sender = private_key()
  pubkey_sender = privkey_sender.public_key()

  privkey_receiver = private_key()
  pubkey_receiver = privkey_receiver.public_key()

  shared_key = get_shared_key(privkey_sender, pubkey_receiver)
  derived_key = get_derived_key(sender_name, shared_key)
  return derived_key
