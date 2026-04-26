import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {"accept":"application/json"}
payload = {
    "name": "Aman",
    "skill": "Python",
    "topic": "API learning",
    "progress": "Day 7"
}

data = requests.put(url,headers = headers, json= payload)

# print(data.json())
print("Status Code:", data.status_code)   # check if 200 OK
print("Raw Text:", data.text)             # see raw response
print("JSON:", data.json())  