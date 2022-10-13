from twilio.rest import Client
import os

account_sid = 'ACf3.................'
auth_token = '296e32..............'

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Creating my First mini Project',
    to='whatsapp:+919xxxxxxx'
)