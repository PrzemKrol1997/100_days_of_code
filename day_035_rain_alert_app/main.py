import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

weather_appid = os.environ.get("WEATHER_APPID")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_phone = os.environ.get("MY_PHONE")
temp_phone =os.environ.get("TEMP_PHONE")
parameters={
    "lat":50.0647,
    "lon":19.9450,
    "appid":weather_appid,
    "cnt": 4

}

will_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data = response.json()["list"]
for timestamp in range(0,4):
    if data[timestamp]["weather"][0]["id"]< 700:
        will_rain =True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
    from_=temp_phone,
    body = 'Bring an umbrella, it is going to rain today',
    to =my_phone
    )
    print(message.status)
