def largest_integer(N: list[int]) -> list[int]:
    string_N = "".join(map(str, N))
    integer_N = int(string_N)
    final_integer = integer_N + 1
    string_final_integer = str(final_integer)

    final_integer_digits = []
    for digit in string_final_integer:
        final_integer_digits.append(int(digit))
    return final_integer_digits


N = list(map(int, input().split()))

print(largest_integer(N))
