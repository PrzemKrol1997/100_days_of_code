import pandas

data = pandas.read_csv("Central_Park_Squirrel.csv")


primary_fur_color =data["Primary Fur Color"].value_counts()
primary_fur_color.to_csv("primary_fur_color.csv")

data = pandas.read_csv("primary_fur_color.csv")
