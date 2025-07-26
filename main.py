# import necessary packages
import requests

# creating function for pokemon info
def get_info(name):
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    print(result)
    if result.status_code == 200:
        print("success!")
        data = result.json()
        return data
    else:
        print(f"failed to retrieve pokemon data error: {result.status_code}")
    return False

# prompt user for search
query = input()

# runs the search through the api
mon = get_info(f"{query}")
print(f"name: {mon['name']}")
print(f"id: {mon['id']}")