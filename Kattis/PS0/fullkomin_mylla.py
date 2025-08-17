# def get_who_lost_bet(N: int, S: str) -> str:
#     A_win_rounds = 0
#     H_win_rounds = 0

#     A_win_games = 0
#     H_win_games = 0

#     for char in S:
#         if char == "A":
#             A_win_games += 1
#         else:
#             H_win_games += 1

#         if A_win_games == 3 or H_win_games == 3:
#             if A_win_games == 3:
#                 A_win_rounds += 1
#             else:
#                 H_win_rounds += 1

#             if A_win_rounds == N:
#                 return "Hannes"
#             elif H_win_rounds == N:
#                 return "Arnar"

#             A_win_games = 0
#             H_win_games = 0

#     if H_win_rounds >= N:
#         return "Arnar"
#     else:
#         return "Hannes"


# N = int(input())  # number of rounds needed to win the bet
# S = input().strip()  # string describing who won each game

# print(get_who_lost_bet(N, S))


def get_who_lost_bet(N: int, S: str) -> str:
    A_win_rounds = 0
    H_win_rounds = 0

    A_win_games = 0
    H_win_games = 0

    for i in range(len(S)):
        if S[i] == "A":
            A_win_games += 1
        else:
            H_win_games += 1

        if A_win_games == 3:
            A_win_rounds += 1
            A_win_games = 0
            # NOTE: this is the difference from the first and second code. can reset
            #       within this branch, but have to rememeber when a round ends, both
            #       players' per round win counters should be reset, not just the one
            #       who lost or won.
            H_win_games = 0
        elif H_win_games == 3:
            H_win_rounds += 1
            H_win_games = 0
            # NOTE: this is the difference from the first and second code. TLDR, have to
            #       reset for both counters in each branch
            A_win_games = 0

    if A_win_rounds == N:
        return "Hannes"
    elif H_win_rounds == N:
        return "Arnar"


N = int(input())  # number of rounds needed to win the bet
S = input().strip()  # string describing who won each game

print(get_who_lost_bet(N, S))
