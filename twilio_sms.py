import AUTHKEYS
from twilio.rest import Client, TwilioRestClient

#In order to use twilio, please go to AUTHKEY_TEMPLATE.py to alter your keys first

# account_sid = AUTHKEYS.twilio_test_sid
# auth_token = AUTHKEYS.twilio_test_authtoken
account_sid = AUTHKEYS.twilio_sid
auth_token = AUTHKEYS.twilio_authtoken
from_num = AUTHKEYS.live_number
to_num = AUTHKEYS.yin_number
client = Client(account_sid, auth_token)


def test(body_message="testing"):
  message = client.messages.create(
              body=body_message,
              from_=body_message,
              to=to_num
            )
  print("message:", message)

def send(body_message):
  message = client.messages.create(
              body=body_message,
              from_=from_num,
              to=to_num
            )
  print("message:", message)

def main():
  continue_prompt = True
  while continue_prompt:
    program = int(input("Press 1 to run test, Press 2 to run send:"))
    if (program == 1):
      print("running test")
      test()
      continue_prompt = False
    elif (program == 2):
      print("running send")
      body_message = str(input("Type your message to send to " + str(to_num) + ":"))
      send(body_message)
      continue_prompt = False
    else:
      print("Please choose either 1 or 2")


#for demo purposes:
#twilio_sms.send(ciphertext)
#plaintext = twilio_sms.receive(ciphertext)
#twilio_sms.send(plaintext)
