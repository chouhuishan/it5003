def get_total_steps(data: list[int]) -> tuple[int, int]:
    K = data[0]
    H = data[1:]
    steps = 0
    n = len(H)
    for i in range(1, n):
        x = H[i]
        j = i - 1
        while j >= 0 and H[j] > x:
            H[j + 1] = H[j]
            steps += 1
            j -= 1
        H[j + 1] = x
    return (K, steps)


P = int(input())  # number of data sets
results = []
for _ in range(P):
    data = list(map(int, input().split()))
    results.append(get_total_steps(data))
for k, steps in results:
    print(k, steps)
