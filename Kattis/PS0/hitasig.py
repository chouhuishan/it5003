def max_and_min_temp(n: int, temp: list[int]) -> tuple[int, int]:
    if n != len(temp):
        raise ValueError("n does not match list of temperatures")

    return max(temp), min(temp)


n = int(input())  # integer n
temp = list(map(int, input().split()))  # n integers of temperature

print(*max_and_min_temp(n, temp))

# Time complexity = O(n)
