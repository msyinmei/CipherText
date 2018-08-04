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
  #need to debug for python2, please uncomment for python3:
  #message = bytes(message, 'utf-8')
  
  #Authentication needed here
  authentication = b"authenticated but unencrypted, HMAC?"
  encrypted_packet = aesgcm.encrypt(derived_key, message, authentication)
  ciphertext = encrypted_packet[2]
  print(sender, "sent", ciphertext)

  plaintext = aesgcm.decrypt(encrypted_packet[0], encrypted_packet[1], ciphertext, authentication)
  print(receiver, "got", plaintext)

  # #Sign the Encrypted Message
  # sign.get_signable(ciphertext)

  # # check_sig.main()
  # # sign.main()

main()