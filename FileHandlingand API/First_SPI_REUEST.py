import requests

url = "https://api.freeapi.app/api/v1/public/randomusers"

data = requests.get(url)
jsondata = data.json()
print(type(jsondata))


print(jsondata["data"]["data"][0]["login"]["password"])
