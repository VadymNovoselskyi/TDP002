import requests

BASE_URL = "https://www.ida.liu.se/~TDP002/pokeapi/"


def do_request(url):
    response = requests.get(f"{BASE_URL}/{url}/")

    if not response.status_code == 200:
        raise Exception(f"Error getting {url}: {response}")

    return response.json()


def get_pokemon_info(pokemons_data, pokemon_name):
    url = None
    for info in pokemons_data:
        if info["name"] == pokemon_name:
            url = info["url"]
            break

    if url is None:
        raise Exception(f'Pokemon "{pokemon_name}" doesn\'t exist')
    return do_request(url)


def get_ability_flavor_text(url):
    flavor_text_entries = do_request(url)["flavor_text_entries"]
    flavor_text = None

    for flavor_text_entry in flavor_text_entries:
        if flavor_text_entry["language"]["name"] == "en":
            flavor_text = flavor_text_entry["flavor_text"]
            break

    if flavor_text is None:
        raise Exception(f"Cound't find flavor_text in english for {url}")
    return flavor_text


def main():
    pokemons_data = None
    while pokemons_data is None:
        try:
            pokemons_data = do_request("api/v2/pokemon")["results"]
        except Exception as e:
            print(f"Error getting pokemons_data")

    while True:
        try:
            pokemon_name = input("Enter a Pokémon name: ")
            pokemon_info = get_pokemon_info(pokemons_data, pokemon_name)
            pokemon_abilities = pokemon_info["abilities"]
            print(f"\n\n{pokemon_name} has {len(pokemon_abilities)} abilities \n\n")
            for ability_info in pokemon_abilities:
                print(f"Ability '{ability_info["ability"]["name"]}': ")
                print(f'{get_ability_flavor_text(ability_info["ability"]["url"])} \n')
        except Exception as e:
            print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
