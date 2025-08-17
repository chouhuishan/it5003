def get_grid(r, c):
    grid = []
    for _ in range(r):
        row = []
        for j in range(c):
            row.append(int(input()))
        grid.append(row)
    return grid


r, c = map(int, input().split())
print(get_grid(r, c))
