from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def private_key(public_exponent, key_size):
  return rsa.generate_private_key(
    public_exponent = public_exponent,
    key_size = key_size,
    backend = default_backend()
    )


def main():
  print("key_gen")