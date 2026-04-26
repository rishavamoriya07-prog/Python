# import requests

# response = requests.get("http://api.open-notify.org/astros")
# print(response.status_code)
# print(response.json())

# import json
# def printojs(obj):
#     data = json.dumps(obj, sort_keys=True, indent=3)
#     print(data)
# printojs(response.json())
import requests
import json
response = requests.get("https://api-server.dataquest.io/economic_data/countries")
data = json.loads(response.json())
print(f"total countries available :{len(data)}")
print(f"first country is {data[0]['long_name']}")
