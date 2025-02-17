import smtplib as sm
import datetime as dt
import random

my_emile ="@gmail.com"
receiver_email = "@yahoo.com"
password = "something"

with open("quotes.txt","r") as data:
    quotes =data.readlines()
message="Subject:Quote for today\n\n"
message += random.choice(quotes)
now = dt.datetime.now()
weekday = now.weekday()
if weekday ==0 :
    with sm.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_emile, password=password)
        connection.sendmail(from_addr=my_emile, to_addrs=receiver_email, msg=message)





