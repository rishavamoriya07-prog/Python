import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

random_name = requests.get(url)
data = random_name.json()
print(type(data))
print(data["data"]["name"]["last"])







