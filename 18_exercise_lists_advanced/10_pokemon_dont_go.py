def increase_decrease_elements(pokemon_list: list, element: int) -> list:
    increased_decreased_pokemon_list = []
    for item in pokemon_list:
        if element < item:
            item -= element
        else:
            item += element
        increased_decreased_pokemon_list.append(item)
    return increased_decreased_pokemon_list


def pokemon_index_check(index: int, pokemon_list: list, caught_pokemon: int):
    if index < 0:
        element_to_be_removed = pokemon_list[0]
        increase_decreased_list = increase_decrease_elements(pokemon_list, element_to_be_removed)
        increase_decreased_list[0] = increase_decreased_list[-1]
    elif index > len(pokemon_list) - 1:
        element_to_be_removed = pokemon_list[-1]
        increase_decreased_list = increase_decrease_elements(pokemon_list, element_to_be_removed)
        increase_decreased_list[-1] = increase_decreased_list[0]
    else:
        element_to_be_removed = pokemon_list[index]
        increase_decreased_list = increase_decrease_elements(pokemon_list, element_to_be_removed)
        del increase_decreased_list[index]
    caught_pokemon += element_to_be_removed
    return caught_pokemon, increase_decreased_list


def catch_pokemon(pokemon_list: list) -> int:
    sum_removed_pokemons = 0
    while pokemon_list:
        index = int(input())
        sum_removed_pokemons, pokemon_list = pokemon_index_check(index, pokemon_list, sum_removed_pokemons)
    return sum_removed_pokemons


distance_to_pokemon = [int(dis) for dis in input().split()]
result = catch_pokemon(distance_to_pokemon)
print(result)
