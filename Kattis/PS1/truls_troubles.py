def number_points(rallies: str) -> str:
    T_win_rally, H_win_rally, T_win_match, H_win_match = 0, 0, 0, 0

    for char in rallies:
        if char == "T":
            T_win_rally += 1
        else:
            H_win_rally += 1

        if T_win_rally >= 11 and T_win_rally - H_win_rally >= 2:
            T_win_match += 1
            T_win_rally = 0
            H_win_rally = 0

        elif H_win_rally >= 11 and H_win_rally - T_win_rally >= 2:
            H_win_match += 1
            H_win_rally = 0
            T_win_rally = 0

    return f"{T_win_rally}-{H_win_rally}"


rallies = input()
print(number_points(rallies))
