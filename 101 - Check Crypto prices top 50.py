from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests



# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#   # 'start':'1',
#   # 'limit':'50',
#   'name': "Ethereum",
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': '9bd9f1a9-8300-4ca6-86ab-b01975672b9f',
# }
#
# session = Session()
# session.headers.update(headers)
#
# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
#   for item in data:
#     print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)
#
# print("*********************")


def get_price():

    try:
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '9bd9f1a9-8300-4ca6-86ab-b01975672b9f',
        }
        session = Session()
        session.headers.update(headers)
        # make a request to the coinmarketcap api
        response1 = requests.get(url, headers=headers)
        response_json = response1.json()
        # extract the bitcoin price from the json data

        for i in range(0, 50):
            price = response_json['data'][i]
            print(i)
            print(price["name"])
            print("Kurs {} : ".format(1), price['quote']['USD']['price'])
    except Exception as e:
        print(e)

get_price()
