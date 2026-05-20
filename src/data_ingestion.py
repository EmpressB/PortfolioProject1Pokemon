import requests
import pandas as pd
import time


BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon(pokemon_id):
    url = BASE_URL + str(pokemon_id)
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def extract_pokemon_data(data):
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    
        return {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'],
        'weight': data['weight'],
        'type_1': data['types'][0]['type']['name'],
        'type_2': data['types'][1]['type']['name'] if len(data['types']) > 1 else None,
        'hp': stats['hp'],
        'attack': stats['attack'],
        'defense': stats['defense'],
        'special_attack': stats['special-attack'],
        'special_defense': stats['special-defense'],
        'speed': stats['speed'],
        'base_stat_total': sum(stats.values())
    }

def get_all_pokemon(start=1, end=1025):
    all_pokemon = []
    
    for pokemon_id in range(start, end + 1):
        print(f"Fetching Pokemon #{pokemon_id}...")
        data = fetch_pokemon(pokemon_id)
        
        if data:
            pokemon = extract_pokemon_data(data)
            all_pokemon.append(pokemon)
        
        time.sleep(0.2)
    
    return all_pokemon


def save_to_csv(data, filename="data/raw/pokemon_data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} Pokemon to {filename}")
    return df

if __name__ == "__main__":
    print("Starting Pokemon data collection...")
    all_pokemon = get_all_pokemon()
    df = save_to_csv(all_pokemon)
    print(df.head())