import base64 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def encrypt(message, public_key):
  cipher = public_key.encrypt(
      message,
      padding.OAEP(
        mgf=padding.MGF1(
          algorithm=hashes.SHA256()
          ),
        algorithm = hashes.SHA256(),
        label=None
        )
    )

  return str(base64.b64encode(cipher))

def main():
  print("encrypt")