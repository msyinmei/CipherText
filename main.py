import key_gen
import aesgcm
import twilio_sms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac


def utf8len(s):
    return len(s.encode('utf-8'))

def hash(key, message_to_hash):
  h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
  h.update(message_to_hash)
  return h.finalize()

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

  print("type of message:", type(message))
  
  #This is just information associated to the user, authenticated with the key but not encrypted.
  associated_data = b"This is the user_id, unique to the user from the company server"
  authenticated_associated_data = hash(derived_key, associated_data)

  encrypted_packet = aesgcm.encrypt(derived_key, message, authenticated_associated_data)
  ciphertext = encrypted_packet[2]
  aesgcm_nonce = encrypted_packet[1]
  aesgcm_key = encrypted_packet[0]
  print(sender, "sent", ciphertext)
  
  #for demo purposes:
  #twilio_sms.send(ciphertext)
  #plaintext = twilio_sms.receive(ciphertext)
  #twilio_sms.send(plaintext)

  plaintext = aesgcm.decrypt(aesgcm_key, aesgcm_nonce, ciphertext, authenticated_associated_data)
  print(receiver, "got", plaintext)

main()