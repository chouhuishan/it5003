def number_petals_left(N: int) -> int:
    power = 1
    while power * 2 <= N:
        power *= 2
    petals_left = 2 * (N - power) + 1
    return petals_left


N = int(input())  # initial number of petals

print(number_petals_left(N))

# Time complexity = O(N) if stimulate subtask 3, but O(log N)/ O(1) formulaic solution is possible
