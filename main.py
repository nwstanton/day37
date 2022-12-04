import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "nattynate"
TOKEN = "vbskdfjbkhjsdo"


user_params = {
    "token": "vbskdfjbkhjsdo" ,
    "username": "nattynate",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(response.text)
graph_id = "python0"
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"


graph_config = {
    "id": "python0",
    "name": "Bjj tracker",
    "unit": "Hr",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": "vbskdfjbkhjsdo"
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

today = datetime.now()


post_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how long did you do BJJ today?")
}

print(today.strftime("%Y%m%d"))
response = requests.post(url=graph_endpoint, json=post_pixel, headers=headers)
print(response.text)

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

put_pixel = {
    "quantity": "2.5"
}

#response = requests.put(url=update_endpoint, json=put_pixel, headers=headers)
#print(response.text)

#response = requests.delete(url=update_endpoint, headers=headers)