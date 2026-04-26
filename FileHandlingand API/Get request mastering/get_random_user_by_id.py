import requests
def request_to_fetch_user(userId):

    url = (f"https://api.freeapi.app/api/v1/public/youtube/playlists")
    response = requests.get(url)
    print(response)
    data = response.json()
    print(data["data"]["data"][0]["snippet"]["title"])






id = int(input("please enter which user id for which you want the details"))
request_to_fetch_user(id)