from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def get_signable(message):
  return (bytes(message, encoding='utf8') if not 
  isinstance(message, bytes) else message)

def get_signer(private_key):
  return private_key.signer(
      padding.PSS(
          mgf=padding.MGF1(hashes.SHA256()),
          salt_length=padding.PSS.MAX_LENGTH
      ),
      hashes.SHA256()
  )

def sign(signer, signable):
  print("before sign:", signable)
  signer.update(signable)
  print("after sign:", signable)

def get_signature(signer):
  signature = str(
      base64.b64encode(signer.finalize()),
      encoding='utf8'
  )
  return signature


def main():
  print("sign")