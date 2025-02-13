# list = [1,2,3,4,5]
# new_list = [n for n in list[::2]]
# print(new_list)
#
# with open("file1.txt", mode="r") as file:
#     file1_data = file.readlines()
#
# with open("file2.txt", mode="r") as file:
#     file2_data = file.readlines()
#     file1_data =[int(n.strip()) for n in file1_data]
#     file2_data =[int(n.strip()) for n in file2_data]
# new_list =[]
#
#
# result = [i for i in file1_data if i in file2_data]
#
# print(result)
# import re
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in re.findall(r"\b\w+\b", sentence) }
#
# print (result)
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key:(value * 9/5) + 32 for (key,value) in weather_c.items() }


print(weather_f)