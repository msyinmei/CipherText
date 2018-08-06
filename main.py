import key_gen
import aesgcm
from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes, hmac

def utf8len(s):
    return len(s.encode('utf-8'))

# def hash(key, message_to_hash):
#   h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
#   h.update(message_to_hash)
#   return h

def main():
  #Welcome
  print("Welcome to CipherText!")
  sender = str(input("Who is sending the message? "))
  receiver = str(input("Who is receiving the message? "))

  #Key Generation to obtain derived key from X25519 + HKDF
  derived_key = key_gen.handshake(sender)

  #Message Encryption using derived_key as the key to AES GCM
  message = str(input("Please type the message you'd like to send: "))
  message = (bytes(message, encoding='utf8') if not 
  isinstance(message, bytes) else message)
  
  #This is information associated to the user, authenticated with the key but not encrypted.
  associated_data = b"This could be the user_id, unique to the user from the company server"
  # hashing does not work:
  # associated_data = hash(derived_key, associated_data)

  aesgcm_packet, aesgcm_nonce, ciphertext = aesgcm.encrypt(derived_key, message, associated_data)
  print(sender, "sent", ciphertext)

  #check hash
  # associated_data = associated_data.finalize()
  plaintext = aesgcm.decrypt(aesgcm_packet, aesgcm_nonce, ciphertext, associated_data)
  print(receiver, "got", plaintext, "associated_data:", associated_data)

main()