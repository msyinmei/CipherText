import key_gen
import aesgcm

def main():
  #Welcome
  print("Welcome to CipherText!")
  sender = str(input("Who is sending the message? "))
  receiver = str(input("Who is receiving the message? "))

  #Key Generation to obtain derived key from X25519 + HKDF
  derived_key = key_gen.handshake()

  #Message Encryption using derived_key as the key to AES GCM
  message = str(input("Please type the message you'd like to send: "))
  message = (bytes(message, encoding='utf8') if not 
  isinstance(message, bytes) else message)
  
  #Authentication needed here
  authentication = b"authenticated but unencrypted, HMAC?"
  encrypted_packet = aesgcm.encrypt(derived_key, message, authentication)
  ciphertext = encrypted_packet[2]
  print(sender, "sent", ciphertext)

  plaintext = aesgcm.decrypt(encrypted_packet[0], encrypted_packet[1], ciphertext, authentication)
  print(receiver, "got", plaintext)

main()