import key_gen
import check_sig
import encrypt
import decrypt
import send
import sign

def main():
  print("Welcome to CipherText!")

  #Key Generation
  sender = str(input("Who is sending the message? "))
  receiver = str(input("Who is receiving the message? "))
  print("Thank you! Let us now generate your public and private keys...")

  privkey_sender = key_gen.private_key(65537, 2048)
  pubkey_sender = privkey_sender.public_key()
  privkey_receiver = key_gen.private_key(65537, 2048)
  pubkey_receiver = privkey_receiver.public_key()

  print("privkeys", sender,":", privkey_sender, "/n", receiver ,":", privkey_receiver)
  print("pubkeys", sender,":", pubkey_sender, "/n",receiver,":", pubkey_receiver)

  #Message Encryption
  message = str(input("Please type the message you'd like to send: "))
  ciphertext = encrypt.encrypt(message, pubkey_receiver)
  print(ciphertext)


  # check_sig.main()
  # encrypt.main()
  # decrypt.main()
  # send.main()
  # sign.main()

main()