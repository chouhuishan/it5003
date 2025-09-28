def if_robot_return_original_position(moves: str) -> bool:
    x, y = 0, 0
    for move in moves:
        if move == "R":
            x += 1
        elif move == "L":
            x -= 1
        elif move == "U":
            y += 1
        else:
            y -= 1
    return True if x == 0 and y == 0 else False


moves = input()
print(if_robot_return_original_position(moves))


def if_robot_return_original_position(moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


moves = input()
print(if_robot_return_original_position(moves))
