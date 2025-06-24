import requests

base_url =  "https://pokeapi.co/"

def get_pokemon_data(name):
    url = f"{base_url}api/v2/pokemon/{name.lower()}/"
    requests.get(url)
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(f"- {ability['ability']['name']}")
    else:
        print(f"Pokemon not found error {response.status_code}")

pokemon_name = "pikachu"
get_pokemon_data(pokemon_name)