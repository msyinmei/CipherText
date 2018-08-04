import AUTHKEYS
from twilio.rest import Client, TwilioRestClient

# account_sid = AUTHKEYS.twilio_test_sid
# auth_token = AUTHKEYS.twilio_test_authtoken
account_sid = AUTHKEYS.twilio_sid
auth_token = AUTHKEYS.twilio_authtoken
from_num = AUTHKEYS.live_number
to_num = AUTHKEYS.yin_number
client = Client(account_sid, auth_token)

message = client.messages.create(
            body='Hello there!',
            from_=from_num,
            to=to_num
          )

print("message:", message)