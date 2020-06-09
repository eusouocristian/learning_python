# virtualenv => env2
from twilio.rest import Client
import os
import token_mobilio

# Criadas as variaveis no ambiente do sist. operacional para esconder sid e token do Twilio
# Essas informações estão no site do Twilio
# os.environ['account_sid'] = 'xxxxx'
# os.environ['auth_token'] = 'xxxxx'
token_mobilio.generate_token()
account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)

# SMS Message
# message = client.messages.create(from_='+12015810478',
#                                  body='teste',
#                                  to='+5551998034545')

# Whatsapp Message
message = client.messages.create(from_='whatsapp:+14155238886',
                                 body='Oi queridão',
                                 to='whatsapp:+555198034545')

print(message.sid)
