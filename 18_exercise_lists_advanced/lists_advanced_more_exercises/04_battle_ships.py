def is_ship(field: list, row: int, coll: int) -> bool:
    if field[row][coll] > 0:
        return True
    else:
        return False


def attacked_ship(field: list, row: int, coll: int):
    destroyed = False
    if is_ship(field, row, coll):
        field[row][coll] -= 1
        if field[row][coll] == 0:
            destroyed = True
    return field, destroyed


def war_completed(field: list, attacked_squares: list):
    destroyed_ships = 0
    for attacked in attacked_squares:
        position = attacked.split("-")
        row = int(position[0])
        coll = int(position[1])
        field, successful_attack = attacked_ship(field, row, coll)
        if successful_attack:
            destroyed_ships += 1
    return destroyed_ships


num_n = int(input())  # n representing the number of rows of the field
field_rows = [[int(n) for n in input().split()] for s in range(num_n)]
attacked_squares = input().split()
result = war_completed(field_rows, attacked_squares)
print(result)
