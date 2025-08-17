def get_score(n: int, matches: str) -> str:
    if n != len(matches):
        raise ValueError("n is not equal to the the number of matches")

    valid_matches, G_win, A_win = 0, 0, 0
    best_percentage, current_win_percentage = 0.0, 0.0
    best_G, best_A = 0, 0

    for k, char in enumerate(reversed(matches)):
        if char == "G":
            G_win += 1
            valid_matches += 1
        elif char == "A":
            A_win += 1
            valid_matches += 1
        else:
            continue

        if valid_matches > 0:
            current_win_percentage = G_win / valid_matches

            if (
                (current_win_percentage > best_percentage)  # better win percentage
                or (k == 0)  # first valid match
            ):
                best_percentage = current_win_percentage
                best_G, best_A = G_win, A_win

    return f"{best_G}-{best_A}"


# number of matches logged
n = int(input())
# sequence of characters which represents the results of the matches that was played
matches = input()

print(get_score(n, matches))
