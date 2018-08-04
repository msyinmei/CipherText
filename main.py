import key_gen
import check_sig
import aesgcm
import decrypt
import send
import sign
import twilio

def main():
  print("Welcome to CipherText!")
  sender = str(input("Who is sending the message? "))
  receiver = str(input("Who is receiving the message? "))

  #Key Generation to obtain derived key from X25519 + HKDF
  derived_key = key_gen.handshake()

  #Message Encryption using derived_key as the key to AES GCM
  message = str(input("Please type the message you'd like to send: "))
  #Authentication needed here
  authentication = "authenticated but unencrypted, HMAC?"
  encrypted_packet = aesgcm.encrypt(derived_key, message, authentication)
  ciphertext = encrypted_packet[2]
  print(ciphertext)

  plaintext = aesgcm.decrypt(encrypted_packet[0], encrypted_packet[1], ciphertext, authentication)
  print(plaintext)

  # #Sign the Encrypted Message
  # sign.get_signable(ciphertext)

  # # check_sig.main()
  # # send.main()
  # # sign.main()

main()