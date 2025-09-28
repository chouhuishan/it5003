from math import ceil


def least_number_days(n: int, m: int, k: int, line: list[int]) -> int:
    if k < m:
        return ":("

    total_typos = sum(line)
    max_fixes_per_day = k // m

    return ceil(total_typos / max_fixes_per_day)


n, m, k = map(int, input().split())
line = map(int, input().split())

print(least_number_days(n, m, k, line))

# Time complexity = O(n) - sum the typos
