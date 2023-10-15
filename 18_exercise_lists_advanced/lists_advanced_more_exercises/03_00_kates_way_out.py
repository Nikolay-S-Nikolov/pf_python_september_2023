def kate_position(maze: list):
    kate = "k"
    position_k_x = [maze.index(k) for k in maze if kate in k][0]
    position_k_y = [y.index(kate) for y in maze if kate in y][0]
    return position_k_x, position_k_y


def kate_way(maze: list):
    moves = 0
    exit_maze = False
    x, y = kate_position(maze)
    while True:
        if x in range(1, len(maze)) and maze[x - 1][y] == " ":
            maze[x - 1][y] = "k"
            moves += 1
            x = x - 1
        elif y in range(len(maze[0]) - 1) and maze[x][y + 1] == " ":
            maze[x][y + 1] = "k"
            moves += 1
            y = y + 1
        elif x in range(len(maze) - 1) and maze[x + 1][y] == " ":
            maze[x + 1][y] = "k"
            moves += 1
            x = x + 1
        elif y in range(1, len(maze[0])) and maze[x][y - 1] == " ":
            maze[x][y - 1] = "k"
            moves += 1
            y = y - 1
        else:
            break
    if x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1:
        moves += 1
        exit_maze = True
    if exit_maze:
        return f"Kate got out in {moves} moves"
    else:
        return f"Kate cannot get out"


number_of_row = int(input())
maze_list = [[n for n in input()] for s in range(number_of_row)]

result = kate_way(maze_list)
print(result)
