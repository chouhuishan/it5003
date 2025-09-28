def get_chronological_order(line: list[int]) -> list[int]:
    L = len(line)
    while L > 1:
        swapped = False
        for i in range(L - 1):
            if i < len(line) - 1 and line[i] > line[i + 1]:
                line[i], line[i + 1] = line[i + 1], line[i]
                swapped = True
                print(*line)
        if not swapped:
            break
        L -= 1


line = list(map(int, input().split()))
get_chronological_order(line)

# this is a classic bubble sort
# Time complexity = O(**2)
