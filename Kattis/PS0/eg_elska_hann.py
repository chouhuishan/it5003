def number_petals_left(N: int) -> int:
    power = 1
    while power * 2 <= N:
        power *= 2
    petals_left = 2 * (N - power) + 1
    return petals_left


N = int(input())  # initial number of petals

print(number_petals_left(N))

#