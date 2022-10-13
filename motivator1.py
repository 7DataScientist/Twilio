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
    # print(q_json['contents']['quotes'][0]['quote'])
    return q_json['contents']['quotes'][0]['quote']


# get_quote_of_the_day()