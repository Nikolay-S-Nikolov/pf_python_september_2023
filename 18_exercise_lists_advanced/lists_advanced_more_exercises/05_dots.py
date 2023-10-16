def all_dots(board: list):
    dots_position_list = []
    for row in range(len(board)):
        for coll in range(len(board[0])):
            if board[row][coll] == ".":
                dots_position_list.append([row, coll])
    return dots_position_list


def it_is_dot_near_visited(visited_board: list):
    for row in range(len(visited_board)):
        for coll in range(len(visited_board[0])):
            if visited_board[row][coll] == "Visited":
                if (row + 1) in range(len(visited_board)) \
                        and visited_board[row + 1][coll] == ".":
                    return True, row + 1, coll
                elif (row - 1) in range(len(visited_board)) \
                        and visited_board[row - 1][coll] == ".":
                    return True, row - 1, coll
                elif (coll + 1) in range(len(visited_board[0])) \
                        and visited_board[row][coll + 1] == ".":
                    return True, row, coll + 1
                elif (coll - 1) in range(len(visited_board[0])) \
                        and visited_board[row][coll - 1] == ".":
                    return True, row, coll - 1
    return False, 0, 0


def visited_counter(visited_board: list):
    counter = 0
    for row in range(len(visited_board)):
        for coll in range(len(visited_board[0])):
            if visited_board[row][coll] == "Visited":
                counter += 1
    return counter


def current_dot_count(board: list, dot, list_of_dots):
    [x, y] = dot
    v_board = board
    v_board[x][y] = "Visited"
    while True:
        if [x + 1, y] in list_of_dots and v_board[x + 1][y] == ".":
            v_board[x + 1][y] = "Visited"
        if [x - 1, y] in list_of_dots and v_board[x - 1][y] == ".":
            v_board[x - 1][y] = "Visited"
        if [x, y + 1] in list_of_dots and v_board[x][y + 1] == ".":
            v_board[x][y + 1] = "Visited"
        if [x, y - 1] in list_of_dots and v_board[x][y - 1] == ".":
            v_board[x][y - 1] = "Visited"
        it_is_dot, x, y = it_is_dot_near_visited(v_board)
        if it_is_dot:
            v_board[x][y] = "Visited"
        else:
            current_dots = visited_counter(v_board)
            for row in range(len(v_board)):
                for coll in range(len(v_board[0])):
                    if v_board[row][coll] == "Visited":
                        v_board[row][coll] = "."
            return current_dots


def max_dots(board: list):
    list_of_dots = all_dots(board)
    max_num_dots = 0
    for dots in list_of_dots:
        current_count = current_dot_count(board, dots, list_of_dots)
        if current_count > max_num_dots:
            max_num_dots = current_count
    return max_num_dots


num_n = int(input())
board_of_dots_and_dashes = [[n for n in input().split()] for s in range(num_n)]
result = max_dots(board_of_dots_and_dashes)
print(result)
