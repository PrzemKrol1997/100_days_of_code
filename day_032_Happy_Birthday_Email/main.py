import pandas
import smtplib as sm
import datetime as dt
import random

my_emile ="@gmail.com"
password = "something"

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")
now = dt.datetime.now()

for person in birthdays:
    if person["month"] == now.month and  person["day"] == now.day:
        receiver_email = person["email"]
        file_name = "letter_templates/" +"letter_" + str(random.randint(1,3))+".txt"
        with open(file_name, "r") as data:
            lines = data.readlines()
            wishes = "Subject:Best wishes\n\n"
            for line in lines:
                 wishes += line.replace("[NAME]",person["name"])
        with sm.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_emile, password=password)
            connection.sendmail(from_addr=my_emile, to_addrs=receiver_email, msg=wishes)



