import base64 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# def RSA_private_key():
#   return rsa.generate_private_key(
#     public_exponent = 65537,
#     key_size = 2048,
#     backend = default_backend()
#     )

def rsa_encrypt(message, public_key):
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

