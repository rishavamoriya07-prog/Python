import requests

url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/post"

headers = { "accept" : "application/json"}
payload = {
    "name": "Aman",
    "skill": "Python",
    "topic": "API learning",
    "progress": "Day 7"
}

data = requests.post(url, headers = headers, json = payload)
print(data.json())

# import requests

# url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/post"

# headers = {"accept": "application/json"}

# response = requests.post(url, headers=headers)

# print(response.json())