import requests
from datetime import datetime
import smtplib as sm
import time



MY_LAT = 50.0647
MY_LNG = 19.9450
EPSILON = 5
my_emile ="@gmail.com"
receiver_email = "@yahoo.com"
password = "something"

def check_iss_location():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()
    iss_lat = float(data["iss_position"]['latitude'])
    iss_lng = float(data["iss_position"]['longitude'])
    lat_difference = abs(abs(MY_LAT)-abs(iss_lat))
    lng_difference = abs(abs(MY_LNG)-abs(iss_lng))
    if  lat_difference <EPSILON and lng_difference < EPSILON:
        send_message()
        return False
    return True

def send_message():
    message = ("Subject:ISS is over you\n\n"
               "It is dark and the iss is over your head, you might want to check it out")
    with sm.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_emile, password=password)
        connection.sendmail(from_addr=my_emile, to_addrs=receiver_email, msg=message)
    print("message sent")


parameters ={
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted" : 0,
    "tzid" :"Europe/Warsaw",
}

program_on = True
while program_on:
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])-1
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])+1
    time_now = datetime.now()
    if sunset < time_now.hour <= sunrise:
        program_on = check_iss_location()
    time.sleep(60)









