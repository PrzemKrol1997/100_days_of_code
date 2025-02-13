# # with open("weather_data.csv", mode="r") as file:
# #     data = file.readines()
# # print (data)
#
#
# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#         # temperatures = int(row[1])
import pandas
data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# celsius = data[data.day =="Monday"].temp[0]
# print(celsius)
# Fahrenheit = (celsius * 9/5) + 32
# print(Fahrenheit)

data_dict = {
    "students":["Amy", "James", "Przemek"],
    "scores":[76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
print(data[data.students == "Amy"])
data.to_csv("new_csv")