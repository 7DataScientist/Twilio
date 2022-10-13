import requests

def get_quote_of_the_day():
    """
    - takes category as parameter and returns the quote of the day
    :return:
    """
    # the required first parameter of the 'get' method is the 'url':
    x = requests.get('https://quotes.rest/qod?language=en')
    # print the response in JSON
    q_json = x.json()
    print(q_json['contents']['quotes'][0]['quote'])


get_quote_of_the_day()



# Industry Practices

# Clean, modularised code
# Snake case as per PEP 8
# Config is Seperate
# Proper Documentation
# DRY - Don’t Repeat yourself

# System Features
# get_quote_of _the_day
# 	- takes category as parameter and returns the quote of the day
#
#       -    set_twilio_connection
# 		- takes account_sid and account_token as parameter and returns client object
#
#       - 	send_whatsapp_text
#       		- takes quote and twilio client connection as parameters and returns message ID
#
# background_cron_job
# 	- takes send_whatsapp_text as a job to execute everyday in background

