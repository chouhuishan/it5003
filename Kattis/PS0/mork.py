def when_to_bet(n: int, m: int) -> str:
    is_draw = (n == 0 or m == 0) or (n == 2 and m == 2)
    if is_draw:
        return "Jebb"
    else:
        return "Neibb"


n = int(input())  # number of goals
m = int(input())  # scoring flag

print(when_to_bet(n, m))

# Time complexity = O(1), read the inputs (2 integers)
