def form_mine_map(num_rows: int) -> list[str]:
    mine_map = []
    for _ in range(num_rows):
        map_row = input()
        mine_map.append(map_row)
    return mine_map


def get_mine_positions(
    mine_map: list[str], num_rows: int, num_cols: int
) -> list[tuple[int, int]]:
    mine_coordinates = []
    for r in range(num_rows):
        for c in range(num_cols):
            if mine_map[r][c] == "*":
                mine_coordinates.append((r + 1, c + 1))

    return mine_coordinates


def print_mine_positions(coordinates: list[tuple[int, int]]) -> None:
    k = len(coordinates)
    print(k)
    for r, c in coordinates:
        print(r, c)


n, m = map(int, input().split())
mine_map = form_mine_map(n)
coordinates = get_mine_positions(mine_map, n, m)
print_mine_positions(coordinates)

# Time complexity = O(n * m)
