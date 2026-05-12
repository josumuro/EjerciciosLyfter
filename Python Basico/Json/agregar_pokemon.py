import json


with open('pokemons.json', 'r') as f:
    pokemons = json.load(f)

# Pedir información del nuevo Pokémon
name = input("Nombre del Pokémon: ")
type_ = input("Tipo del Pokémon: ")
level = int(input("Nivel del Pokémon: "))

# Crear el diccionario del nuevo Pokémon
new_pokemon = {
    "name": name,
    "type": type_,
    "level": level
}


pokemons.append(new_pokemon)


with open('pokemons.json', 'w') as f:
    json.dump(pokemons, f, indent=4)

print("Pokémon agregado exitosamente.")