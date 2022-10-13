from twilio.rest import Client
from config import account_sid, auth_token,phone_number
from motivator1 import get_quote_of_the_day

def set_twilio_connection(account_sid,auth_token):
    """
    takes account_sid and account_token as parameter and returns client object
    :param account_sid:
    :param auth_token:
    :return:
    """
    client = Client(account_sid, auth_token)
    return client

def send_whatsapp_text(client):
    """
    takes quote and twilio client connection as parameters and returns message ID
    :param client:
    :return:
    """
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=get_quote_of_the_day(),
        to=phone_number
    )

    return message

# cli1 = set_twilio_connection(account_sid,auth_token)
# message= send_whatsapp_text(cli1)

# print(message.sid)

# To check key value pairs for Auth
# for item, value in os.environ.items():
#     print('{}: {}'.format(item, value))

