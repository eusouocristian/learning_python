# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd3a00fc6a3c0b4f15e18b802e3aa631a'
auth_token = '92d5bbf16db76ea1c4f45561f732e35e'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+14155238886',
                              body='teste',
                              to='+5551998034545'
                          )

print(message.sid)
