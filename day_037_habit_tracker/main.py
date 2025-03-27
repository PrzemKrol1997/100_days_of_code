import requests
import os
import datetime
TOKEN=os.environ.get("TOKEN")
USERNAME=os.environ.get("USERNAME")
ENDPOINT = "https://pixe.la/v1/users"
header={
    "X-USER-TOKEN":TOKEN,
}
def how_long():
    while True:
        try:
            time = str(input("How long in minutes have you been coding?:"))
            return time
        except ValueError:
            print("Wrong input try agin")

def enter_day():
    if len(input("Enter date(yyyyMMdd), or live empty for today: ")) != 8:
        today = datetime.datetime.now()
        today = str(today.date())
        today = today.replace("-","")
        return today

#create user
pos_data_create_account={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response = requests.post(url=endpoint, json=pos_data_create_account)
# print(response.text)

#create graph
pos_data_create_graph={
    "id":"codingtracker",
    "name":"Coding Tracker",
    "unit":"minutes",
    "type":"int",
    "color":"sora",
    "timezone":"Europe/Warsaw",
}
endpoint_graph =f"{ENDPOINT}/{USERNAME}/graphs"
# response = requests.post(headers=header,url=endpoint_graph, json=pos_data_create_graph)
# print(response.text)

#add pixel
date=enter_day()
minutes=how_long()

pos_data_add={
    "date":date,
    "quantity":minutes,
}

endpoint_graph_add_pixel =f"{ENDPOINT}/{USERNAME}/graphs/{pos_data_create_graph["id"]}"
# print(endpoint_graph_edit)
# response = requests.post(headers=header,url=endpoint_graph_add_pixel, json=pos_data_add)
# print(response.text)


#edit pixel
pos_data_edit={
    "quantity":minutes,
}

endpoint_graph_edit =f"{ENDPOINT}/{USERNAME}/graphs/{pos_data_create_graph["id"]}/{date}"
# response = requests.put(headers=header,url=endpoint_graph_edit, json=pos_data_edit)
# print(response.text)


#delete pixel
response = requests.delete(headers=header,url=endpoint_graph_edit)
print(response.text)
