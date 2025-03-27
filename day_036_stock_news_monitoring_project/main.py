# uncomment hashed lines in order to use in pythonanywhere

import os
import requests
import datetime
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_phone = os.environ.get("MY_PHONE")
temp_phone =os.environ.get("TEMP_PHONE")
apikey_alphavantage = os.environ.get("APIKEY_ALPHAVANTAGE")
apikey_newsapi =os.environ.get("APIKEY_NEWSAPI")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
COMPANY_SHORT_NAME ="Tesla"

def get_stock_info():
    parameters_alphavantage={
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK,
        "interval":"60min",
        "apikey":apikey_alphavantage,
    }
    request_alphavantage = requests.get(url="https://www.alphavantage.co/query", params=parameters_alphavantage)
    data_alphavantage = request_alphavantage.json()
    available_dates = list(data_alphavantage["Time Series (Daily)"].keys())
    day_ago = float(data_alphavantage["Time Series (Daily)"][available_dates[1]]["4. close"])
    two_days_ago =float(data_alphavantage["Time Series (Daily)"][available_dates[2]]["4. close"])
    percentage_difference = round((day_ago - two_days_ago)/day_ago*100,2)
    if percentage_difference > 5:
        percentage_difference ="Up"+str(percentage_difference)+"%"
        return percentage_difference
    elif percentage_difference < -5:
        percentage_difference ="Down "+str(percentage_difference*-1)+"%"
        return percentage_difference
    else:
        return False

def get_news():
    yesterday = datetime.datetime.today().date() - datetime.timedelta(days=1)
    parameters_newsapi = {
        "q": f"+{COMPANY_SHORT_NAME}",
        "apiKey": apikey_newsapi,
        "pageSize": 3,
        "language": "en",
        "from": yesterday,
        "sortBy": "popularity",
    }
    request_newsapi = requests.get(url="https://newsapi.org/v2/everything", params=parameters_newsapi)
    data_newsapi = request_newsapi.json()
    data_newsapi = data_newsapi["articles"]
    return data_newsapi

def send_alert(difference, tab):
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token)#, http_client=proxy_client)
    body = f"{COMPANY_SHORT_NAME} {difference}:\n"
    for news in tab:
         body +=f"\nHeadline:{news["title"]}\n"
    message = client.messages.create(
    from_=temp_phone,
    body=body,
    to=my_phone
    )
    print(message.status)


stock_info=get_stock_info()
if stock_info:
    send_alert(difference=stock_info,tab=get_news())